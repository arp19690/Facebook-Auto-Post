#!/usr/bin/python

import urllib

import facebook
import warnings
import requests
import os


# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)


def get_app_access_token(fb_app_id, fb_app_secret):
    return facebook.get_app_access_token(fb_app_id, fb_app_secret)


def post_message_on_fb(fb_profile_id, oauth_access_token, json_data):
    facebook_graph = facebook.GraphAPI(oauth_access_token)

    message = json_data["message"]
    attachments_dict = get_attachments_dict(json_data, oauth_access_token)

    # Try to post something on the wall.
    try:
        fb_response = facebook_graph.put_wall_post(message=message,
                                                   attachment=attachments_dict,
                                                   profile_id=fb_profile_id)
        return True, fb_response
    except facebook.GraphAPIError as e:
        return False, 'Something went wrong: ' + str(e.message)


def post_photo_on_fb(oauth_access_token, json_data):
    image_file_path = 'tmpdata/' + str(json_data["id"]) + ".jpg"
    download_photo(json_data["full_picture"], image_file_path)
    fb_response = upload_photo(image_file_path, oauth_access_token, json_data["message"])
    remove_photo(image_file_path)
    return True, fb_response


def post_video_on_fb(profile_id, oauth_access_token, message, video_link):
    facebook_graph = facebook.GraphAPI(oauth_access_token)
    fb_response = facebook_graph.put_object(profile_id, "feed", message=message, link=video_link)
    return True, fb_response


def upload_photo(image_file_path, oauth_access_token, message=""):
    facebook_graph = facebook.GraphAPI(oauth_access_token)
    fb_response = facebook_graph.put_photo(image=open(image_file_path, 'rb'), message=message)
    return fb_response


def download_photo(source, destination):
    return urllib.urlretrieve(source, destination)


def remove_photo(destination):
    return os.remove(destination)


def get_image_url_on_id(photo_id, oauth_access_token):
    api_url = "https://graph.facebook.com/" + str(photo_id) + "?fields=images&access_token=" + oauth_access_token
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()["images"][0]["source"]
    else:
        return False


def get_timeline_posts(fb_page_id, since_timestamp, oauth_access_token,
                       get_fields="id,link,picture,source,message,created_time,full_picture,description",
                       limit=None, data_format="json"):
    api_url = "https://graph.facebook.com/v2.8/" + fb_page_id + "/feed?fields=" + get_fields + "&since=" + since_timestamp
    if limit is not None:
        api_url += "&limit=" + limit
    api_url += "&format=" + data_format + "&access_token=" + oauth_access_token

    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        return False


def get_attachments_dict(json_data, oauth_access_token):
    attachment_dict = {}

    if "full_picture" in json_data:
        image_file_path = 'tmpdata/' + str(json_data["id"]) + ".jpg"
        download_photo(json_data["full_picture"], image_file_path)
        upload_response = upload_photo(image_file_path, oauth_access_token)
        remove_photo(image_file_path)

        fb_image_url = get_image_url_on_id(upload_response["id"], oauth_access_token)
        attachment_dict["picture"] = fb_image_url

        if "source" in json_data:
            attachment_dict["link"] = json_data["link"]
        else:
            attachment_dict["link"] = fb_image_url

    if "message" in json_data:
        attachment_dict["caption"] = json_data["message"]
        attachment_dict["name"] = json_data["message"]
    elif "story" in json_data:
        attachment_dict["caption"] = json_data["story"]
        attachment_dict["name"] = json_data["story"][:255]

    if "description" in json_data:
        attachment_dict["description"] = json_data["description"]

    return attachment_dict

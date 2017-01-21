#!/usr/bin/python

import urllib

import facebook
import warnings
import requests
import os
import re
from config import BASE_DIR, FILTER_KEYWORDS, AMAZON_AFFILIATE_URL


# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)


def get_app_access_token(fb_app_id, fb_app_secret):
    return facebook.get_app_access_token(fb_app_id, fb_app_secret)


def get_long_lived_access_token(fb_app_id, fb_app_secret, access_token):
    api_url = "https://graph.facebook.com/v2.2/oauth/access_token?grant_type=fb_exchange_token&client_id=" + str(
        fb_app_id) + "&client_secret=" + str(fb_app_secret) + "&fb_exchange_token=" + str(access_token)
    response = requests.get(api_url)
    if response.status_code == 200:
        output = response.text.split("=")
        return output[1]
    else:
        return False


def post_message_on_fb(fb_profile_id, oauth_access_token, json_data, attachments=None):
    facebook_graph = facebook.GraphAPI(oauth_access_token)

    message = filter_text(json_data["message"])
    if attachments is None:
        attachments_dict = get_attachments_dict(json_data, oauth_access_token)
    else:
        attachments_dict = attachments

    # Try to post something on the wall.
    try:
        fb_response = facebook_graph.put_wall_post(message=filter_text(message),
                                                   attachment=attachments_dict,
                                                   profile_id=fb_profile_id)
        return True, fb_response
    except facebook.GraphAPIError as e:
        return False, 'Something went wrong: ' + str(e.message)


def post_child_attachments_message_on_fb(fb_profile_id, oauth_access_token, data_dict):
    facebook_graph = facebook.GraphAPI(oauth_access_token)

    message = filter_text(data_dict["message"])
    child_attachments_list=get_child_attachments_list()

    # Try to post something on the wall.
    try:
        fb_response = facebook_graph.put_wall_post(message=filter_text(message),
                                                   link=data_dict["link"],
                                                   child_attachments=child_attachments_list,
                                                   profile_id=fb_profile_id)
        return True, fb_response
    except facebook.GraphAPIError as e:
        return False, 'Something went wrong: ' + str(e.message)


def post_photo_on_fb(oauth_access_token, json_data):
    image_file_path = BASE_DIR + 'tmpdata/' + str(json_data["id"]) + ".jpg"
    download_photo(json_data["full_picture"], image_file_path)
    fb_response = upload_photo(image_file_path, oauth_access_token, filter_text(json_data["message"]))
    remove_photo(image_file_path)
    return True, fb_response


def post_video_on_fb(profile_id, oauth_access_token, message, video_link):
    facebook_graph = facebook.GraphAPI(oauth_access_token)
    fb_response = facebook_graph.put_object(profile_id, "feed", message=filter_text(message), link=video_link)
    return True, fb_response


def upload_photo(image_file_path, oauth_access_token, message=""):
    facebook_graph = facebook.GraphAPI(oauth_access_token)
    fb_response = facebook_graph.put_photo(image=open(image_file_path, 'rb'), message=filter_text(message))
    return fb_response


def download_photo(source, destination):
    return urllib.urlretrieve(source, destination)


def remove_photo(destination):
    return os.remove(destination)


def find_and_replace_url(message, replace_with_str=AMAZON_AFFILIATE_URL):
    new_str = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', replace_with_str, message)
    return new_str


def filter_text(message, replace_with=AMAZON_AFFILIATE_URL):
    message = find_and_replace_url(message, replace_with)
    for keyword in FILTER_KEYWORDS:
        message = message.replace(str(keyword), replace_with)
    return message


def get_image_url_on_id(photo_id, oauth_access_token):
    api_url = "https://graph.facebook.com/" + str(photo_id) + "?fields=images&access_token=" + oauth_access_token
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()["images"][0]["source"]
    else:
        return False


def create_feed_url(fb_page_id, since_timestamp, oauth_access_token,
                    get_fields="id,link,picture,source,message,created_time,full_picture,description,from",
                    limit=None, data_format="json"):
    api_url = "https://graph.facebook.com/v2.8/" + fb_page_id + "/feed?fields=" + get_fields + "&since=" + since_timestamp
    if limit is not None:
        api_url += "&limit=" + limit
    api_url += "&format=" + data_format + "&access_token=" + oauth_access_token
    return api_url


def fetch_data(api_url, data_list=[]):
    try:
        response = requests.get(api_url)
        data = response.json()
        data_list += data["data"]
        print(str(len(data_list)) + " results found")
        if "error" in data:
            raise Exception(data["error"]["message"])
        else:
            if 'paging' in data:
                if 'next' in data['paging']:
                    next_url = data['paging']['next']

                    # Running this function again
                    data_list = fetch_data(next_url, data_list)

            return data_list
    except Exception as e:
        print("An error occurred: " + str(e))
        return []

def get_child_attachments_list(data_dict):
    child_attachments_list = []
    if len(data_dict) > 0:
        for data in data_dict:
            child_attachments_list.append({
                    "link":data["link"],
                    "picture":data["picture"],
                    "name":filter_text(data["name"]),
                    "description":filter_text(data["description"]),
                })
    return child_attachments_list


def get_attachments_dict(json_data, oauth_access_token):
    attachment_dict = {}

    if "full_picture" in json_data:
        image_file_path = BASE_DIR + 'tmpdata/' + str(json_data["id"]) + ".jpg"
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
        attachment_dict["caption"] = filter_text(json_data["message"])
        attachment_dict["name"] = filter_text(json_data["message"])
    elif "story" in json_data:
        attachment_dict["caption"] = filter_text(json_data["story"])
        attachment_dict["name"] = filter_text(json_data["story"][:255])

        if "description" in json_data:
            attachment_dict["description"] = filter_text(json_data["description"])

    return attachment_dict

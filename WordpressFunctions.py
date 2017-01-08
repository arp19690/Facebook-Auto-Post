from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.posts import GetPosts
from facebookFunctions import post_message_on_fb
from helpers import mac_notify
import config


def get_attachments_dict(post_data):
    attachment_dict = {
        "name": post_data.title,
        "caption": post_data.title,
        "description": post_data.excerpt,
        "picture": post_data.thumbnail["link"],
        "link": post_data.link
    }
    return attachment_dict


def fetch_posts(wp_client, post_status="publish", post_limit=10):
    output_list = []
    posts = wp_client.call(GetPosts({'post_status': post_status, 'number': post_limit}))
    if len(posts) > 0:
        for post_data in posts:
            try:
                data_dict = get_attachments_dict(post_data)
                output_list.append(data_dict)
            except Exception as e:
                print("An error occurred: " + str(e))
                pass

    return output_list


wp = Client(config.WP_WEBSITE + "/xmlrpc.php", config.WP_USERNAME, config.WP_PASSWORD)
formatted_posts = fetch_posts(wp)
if len(formatted_posts) > 0 and len(config.WP_ACCESS_TOKENS_LIST) > 0:
    for data in config.WP_ACCESS_TOKENS_LIST:
        for post_data in formatted_posts:
            fb_post_message = post_data["name"]
            if "appended_message" in data:
                if data["appended_message"] is not None:
                    fb_post_message += "\n\n" + data["appended_message"]

            try:
                api_status, api_message = post_message_on_fb(data["profile_id"], data["access_token"],
                                                             {"message": fb_post_message}, post_data)

                if api_status:
                    print("Message successfully posted on " + data["name"] + "'s Timeline")
                else:
                    raise Exception, api_message
            except Exception as e:
                print("An error occurred: " + str(e))
                mac_notify(data["name"], e)
                pass

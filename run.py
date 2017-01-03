#!/usr/bin/python

from datetime import datetime, timedelta
import sys

from facebookFunctions import post_message_on_fb, get_timeline_posts, post_photo_on_fb
from config import access_tokens_list

reload(sys)
sys.setdefaultencoding('utf-8')

some_timestamp = datetime.now() - timedelta(days=10)
since_timestamp = str(some_timestamp.strftime('%Y-%m-%dT%H:%M'))
for data in access_tokens_list:
    new_posts = get_timeline_posts(data["from_profile_id"], since_timestamp, data["access_token"])
    if len(new_posts) > 0:
        for json_data in new_posts:

            if "message" not in json_data:
                message = "Urvashi Rautela #UrvashiRautela"
            else:
                message = json_data["message"].encode("utf-8")
                try:
                    unicode(message, "ascii")
                except UnicodeError:
                    message = unicode(message, "utf-8")
                else:
                    # value was valid ASCII data
                    pass
            json_data.update({"message": message})

            try:
                if "full_picture" in json_data:
                    post_photo_on_fb(data["access_token"], json_data)
                else:
                    api_status, api_message = post_message_on_fb(data["profile_id"], data["access_token"], json_data)
                    if api_status:
                        print("Message successfully posted on " + data["name"] + "'s Timeline")
                    else:
                        print(api_message)
            except Exception as e:
                print("An error occurred: " + str(e))
                pass

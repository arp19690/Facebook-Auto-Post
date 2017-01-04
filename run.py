#!/usr/bin/python

from datetime import datetime, timedelta
import sys

import os
import facebookFunctions as FFS
import config

reload(sys)
sys.setdefaultencoding('utf-8')


def mac_notify(title, message):
    os.system('terminal-notifier -title "' + str(title) + '" -message "' + str(message) + '"')
    return True


hours_input = config.DEFAULT_TIMEDELTA_HOURS
if len(sys.argv) > 1:
    script, hours_input = sys.argv

some_timestamp = datetime.now() - timedelta(hours=int(hours_input))
since_timestamp = str(some_timestamp.strftime('%Y-%m-%dT%H:%M'))
for data in config.ACCESS_TOKENS_LIST:
    new_posts = FFS.get_timeline_posts(data["from_profile_id"], since_timestamp, data["access_token"])
    # Reverse sorting the dictionary, since we want to post the last photo first so that it looks in an incremental order
    new_posts = sorted(new_posts, reverse=True)
    if len(new_posts) > 0:
        for json_data in new_posts:
            if "message" not in json_data:
                message = data["default_message"]
            else:
                message = json_data["message"].decode('ascii', 'ignore')
            json_data.update({"message": message})

            try:
                if "source" in json_data:
                    api_status, api_message = FFS.post_video_on_fb(data["profile_id"], data["access_token"], message,
                                                                   json_data["link"])
                elif "full_picture" in json_data:
                    api_status, api_message = FFS.post_photo_on_fb(data["access_token"], json_data)
                else:
                    api_status, api_message = FFS.post_message_on_fb(data["profile_id"], data["access_token"],
                                                                     json_data)

                if api_status:
                    print("Message successfully posted on " + data["name"] + "'s Timeline")
                else:
                    print(api_message)
                    mac_notify(data["name"], api_message)
            except Exception as e:
                print("An error occurred: " + str(e))
                mac_notify(data["name"], e)
                pass

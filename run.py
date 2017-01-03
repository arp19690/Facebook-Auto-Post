#!/usr/bin/python

from datetime import datetime, timedelta
import sys

import os
from facebookFunctions import post_message_on_fb, get_timeline_posts, post_photo_on_fb
import config

reload(sys)
sys.setdefaultencoding('utf-8')


def mac_notify(title, message):
    os.system('terminal-notifier -title "' + str(title) + '" -message "' + str(message) + '"')
    return True


some_timestamp = datetime.now() - timedelta(hours=config.DEFAULT_TIMEDELTA_HOURS)
since_timestamp = str(some_timestamp.strftime('%Y-%m-%dT%H:%M'))
for data in config.ACCESS_TOKENS_LIST:
    new_posts = get_timeline_posts(data["from_profile_id"], since_timestamp, data["access_token"])
    if len(new_posts) > 0:
        for json_data in new_posts:

            if "message" not in json_data:
                message = data["default_message"]
            else:
                message = json_data["message"].decode('ascii', 'ignore')

            if "source" in json_data:
                message += "\n" + str(json_data["link"])

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
                        mac_notify(data["name"], api_message)
            except Exception as e:
                print("An error occurred: " + str(e))
                mac_notify(data["name"], e)
                pass

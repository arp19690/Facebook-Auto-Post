#!/usr/bin/python

from datetime import datetime, timedelta
import sys

import os
import facebookFunctions as FFS
import config
from helpers import mac_notify

reload(sys)
sys.setdefaultencoding('utf-8')
os.environ['TZ'] = 'Europe/London'


def get_start_timestamp(filename=config.LAST_RUN_TIME_FILENAME, hours_input=config.DEFAULT_TIMEDELTA_HOURS):
    if (os.path.isfile(filename)):
        last_timestamp = str(open(filename, "r").read())
    else:
        some_timestamp = datetime.now() - timedelta(hours=int(hours_input))
        last_timestamp = str(some_timestamp.strftime('%Y-%m-%dT%H:%M'))
    return last_timestamp


def update_last_run_time(filename=config.LAST_RUN_TIME_FILENAME):
    if (os.path.isfile(filename)):
        os.remove(filename)

    last_timestamp = str(datetime.now().strftime('%Y-%m-%dT%H:%M'))
    with open(filename, "w") as f:
        f.write(str(last_timestamp))
    f.close()
    return True


def start_posting(since_timestamp, data):
    new_posts = FFS.get_timeline_posts(data["from_profile_id"], since_timestamp, data["access_token"])
    if len(new_posts) > 0:
        # Reverse sorting the dictionary, since we want to post the last photo first so that it looks in an incremental order
        new_posts = sorted(new_posts, reverse=True)
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
                    raise Exception(api_message)
            except Exception as e:
                print("An error occurred: " + str(e))
                mac_notify(data["name"], e)
                pass


start_timestamp = get_start_timestamp()

mac_notify("Facebook Auto Post", "Script has been started")
for tmpdata in config.ACCESS_TOKENS_LIST:
    start_posting(start_timestamp, tmpdata)

update_last_run_time()
mac_notify("Facebook Auto Post", "Script terminated")

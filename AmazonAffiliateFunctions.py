import json
import random

import requests
from config import AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST
from config import AMAZON_AFFILIATE_URL

MESSAGE_TEXT_LIST = ["some message"]
CHILD_ATTACHMENT_LIST = [
    {
        "name": "",
        "description": "",
        "picture": "",
        "link": "",
    },
    {
        "name": "",
        "description": "",
        "picture": "",
        "link": "",
    },
    {
        "name": "",
        "description": "",
        "picture": "",
        "link": "",
    },
    {
        "name": "",
        "description": "",
        "picture": "",
        "link": "",
    },
    {
        "name": "",
        "description": "",
        "picture": "",
        "link": "",
    },
]


def get_random_but_unique_num_in_list(limit=5):
    output_list = []
    for i in xrange(0, len(CHILD_ATTACHMENT_LIST)):
        random_int = random.randint(0, len(CHILD_ATTACHMENT_LIST) - 1)
        if len(output_list) < limit:
            if random_int not in output_list:
                output_list.append(random_int)
            else:
                output_list = get_random_but_unique_num_in_list(limit)

    return output_list


def get_child_attachments_list(
        random_num_list=get_random_but_unique_num_in_list()):
    output_list = []
    for i in random_num_list:
        tmp_dict = {
            "link": CHILD_ATTACHMENT_LIST[i]["link"],
            "picture": CHILD_ATTACHMENT_LIST[i]["picture"],
            "name": CHILD_ATTACHMENT_LIST[i]["name"],
            "description": CHILD_ATTACHMENT_LIST[i]["description"]
        }
        output_list.append(tmp_dict)
    return output_list


def start_posting(data_dict):
    for AAD in AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST:
        api_url = "https://graph.facebook.com/v2.8/" + AAD[
            "profile_id"] + "/feed?access_token=" + AAD["access_token"]

        status = requests.post(api_url, data_dict)
        if status.status_code == 200:
            print(
                "Messages successfully posted on " + str(
                    AAD["name"]) + "'s timeline")
        else:
            print("An error occurred")
            print(status.text)


post_data_dict = {
    "message": random.choice(MESSAGE_TEXT_LIST),
    "link": AMAZON_AFFILIATE_URL,
    "child_attachments": json.dumps(get_child_attachments_list()),
}
start_posting(post_data_dict)

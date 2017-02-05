import json
import random

import requests
from config import AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST
from config import AMAZON_AFFILIATE_URL

EXCLUDE_PROFILE_IDS = ["280228608801032"]

MESSAGE_TEXT_LIST = [
    "Looking for that perfect gift for your girl? What's better than a Victoria's Secret present. Make her feel special, get them now",
    "Let this Valentine's Day be a special one. Gift your girl from an exclusive range of Victoria Secret's products. Get them now",
    "You can still get your Valentine's Day gift on time. Shop from Victoria Secret's line of products and gift here a unique gift this year.",
    "Victoria Secret's cosmetics. Shop now and get amazing offers. Valentine's Day is just around the corner."
]

CHILD_ATTACHMENT_LIST = [
    {
        "name": "Victoria's Secret PURE SEDUCTION Fragrance Mist ",
        "description": "Pure Seduction Refreshing Body Mist",
        "picture": "http://ecx.images-amazon.com/images/I/51uUoJcZyML._SX522_.jpg",
        "link": "http://amzn.to/2kBUcPE",
    },
    {
        "name": "Victoria's Secret Fantasies Aqua Kiss",
        "description": "Play for a custom scent, with rain-kissed freesia and daisy",
        "picture": "http://ecx.images-amazon.com/images/I/51t%2B0rlleKL._SY679_.jpg",
        "link": "http://amzn.to/2kfhGJq",
    },
    {
        "name": "Victoria's Secret Noir Tease Glitter Train Case",
        "description": "With a mirror inside lid",
        "picture": "http://ecx.images-amazon.com/images/I/51VGuJZPF0L.jpg",
        "link": "http://amzn.to/2jQYTk2",
    },
    {
        "name": "Victoria's Secret Love Spell Fragrance",
        "description": "Seductive Amber Fragrance Mist",
        "picture": "http://ecx.images-amazon.com/images/I/81wP1miPxzL._SX522_.jpg",
        "link": "http://amzn.to/2lbmdLc",
    },
    {
        "name": "Victoria's Secret Unapologetic Fragrance Mist",
        "description": "Fresh maple water and warm vanilla",
        "picture": "http://ecx.images-amazon.com/images/I/51bgNfeRFPL._SY679_.jpg",
        "link": "http://amzn.to/2kfk3M4",
    },
    {
        "name": "Victoria Secret Pure Daydream Body Mist",
        "description": "Pure daydream mist",
        "picture": "http://ecx.images-amazon.com/images/I/51hkTTMe1nL._SX522_.jpg",
        "link": "http://amzn.to/2lbL6qg",
    },
    {
        "name": "Victoria's Secret Romantic Fragrance Lotion",
        "description": "Pink Petals & Solar Musk",
        "picture": "http://ecx.images-amazon.com/images/I/316TazZ80iL.jpg",
        "link": "http://amzn.to/2lbEU1n",
    },
    {
        "name": "Victoria's Secret Pure Seduction Lotion",
        "description": "Pamper your skin to give it a supple feel",
        "picture": "http://ecx.images-amazon.com/images/I/71yLSWJl2cL._SX522_.jpg",
        "link": "http://amzn.to/2kfydNt",
    },
    {
        "name": "Victoria's Secret Endless Love Fragrance Lotion",
        "description": "Nourishes skin with a light mix of Apple blossom",
        "picture": "http://ecx.images-amazon.com/images/I/51SNq6UT68L._SY679_.jpg",
        "link": "http://amzn.to/2kC1vH2",
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


def start_posting():
    for AAD in AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST:
        if AAD["profile_id"] not in EXCLUDE_PROFILE_IDS:
            api_url = "https://graph.facebook.com/v2.8/" + AAD[
                "profile_id"] + "/feed?access_token=" + AAD["access_token"]

            post_data_dict = {
                "message": random.choice(MESSAGE_TEXT_LIST),
                "link": AMAZON_AFFILIATE_URL,
                "child_attachments": json.dumps(get_child_attachments_list()),
            }

            status = requests.post(api_url, post_data_dict)
            if status.status_code == 200:
                print("Affiliate links successfully posted on " + str(
                    AAD["name"]) + "'s timeline")
            else:
                print("An error occurred")
                print(status.text)

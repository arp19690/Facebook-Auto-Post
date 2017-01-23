import json
import random

import requests
from config import AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST
from config import AMAZON_AFFILIATE_URL
from helpers import mac_notify

MESSAGE_TEXT_LIST = [
    "Huge offers on Amazon.\nGreat quality products at affordable prices.\nGet now\n\n" + AMAZON_AFFILIATE_URL
]

CHILD_ATTACHMENT_LIST = [
    {
        "name": "Digital Cameras, Lenses",
        "description": "Special offers on digital cameras and lenses. Get now!",
        "picture": "https://www.bhphotovideo.com/images/images2000x2000/canon_0591c003_eos_rebel_t6i_dslr_1116101.jpg",
        "link": "http://amzn.to/2jRmt4o",
    },
    {
        "name": "LED and LCD TVs",
        "description": "Get upto 50% off on Televisions. Limited Stock.",
        "picture": "http://ecx.images-amazon.com/images/I/71tgJV3LpML._SL1000_.jpg",
        "link": "http://amzn.to/2kiluLg",
    },
    {
        "name": "iPhones at lowest prices. Big savings on Apple products",
        "description": "iPhones starting at Rs. 10,000. Amazing discounts on exchange. Get Now!",
        "picture": "http://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/M/MY/MMY32/MMY32_AV1_SILVER?wid=1000&hei=1000&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=1472245951991",
        "link": "http://amzn.to/2kh8Hod",
    },
    {
        "name": "Fashion Sale. Big Brands starting @ 499",
        "description": "Enjoy big cashbacks and offers on Clothing and accessories. Amazon Fashin Sale is here.",
        "picture": "http://www.thegogle.com/wp-content/uploads/2016/11/fashion13.jpg",
        "link": "http://amzn.to/2jfp7Qf",
    },
    {
        "name": "Shoes for Women. Upto 70% off",
        "description": "Big brands on sale. Offer only for a limited period. Shop now.",
        "picture": "http://cdn2.secure-e.com/bridalshoes.com.au/prodimg/2015/06/1054_harper-ruby-new_2048_1363.jpg",
        "link": "http://amzn.to/2kizPHm",
    },
    {
        "name": "Microwave Ovens starting just @ 4,090",
        "description": "Buy microwave ovens at super cheap prices. Buy now.",
        "picture": "http://www.lg.com/in/images/microwave-ovens/md05265523/gallery/Large-940x620_0000146.jpg",
        "link": "http://amzn.to/2kjoFCv",
    },
    {
        "name": "Fashion Jewellery & accessories for every occasion",
        "description": "Get fashionable. Get trendy. Show now.",
        "picture": "https://picscelb.files.wordpress.com/2014/07/western-wedding-bridal-new-fashion-for-girls-women-by-royal-jewelley-1.jpg",
        "link": "http://amzn.to/2jIqpln",
    },
    {
        "name": "Buy Furniture @ Amazon",
        "description": "Discover the Latest Furniture Designs Online",
        "picture": "http://www.homezguru.com/wp-content/uploads/2015/05/keens-furniture-beersbridge.jpg",
        "link": "http://amzn.to/2kjfuSv",
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
            print("Affiliate links successfully posted on " + str(
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
mac_notify("Affiliate links", "Posted to all the pages successfully")

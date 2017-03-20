import config
import requests
import json


def post_now():
    url = "https://api.bufferapp.com/1/updates/create.json"
    data_dict = {
        "access_token": config.BUFFER_ACCESS_TOKEN,
        "text": "Sample test",
        "shorten": True,
        "profile_ids": ["57b2dc47ec2002a372d671b3"],
        # "profile_ids": ["5799071fe7e3d76978261b12"],
        "media": {
            "thumbnail": "http://www.technicaltextile.net/businessleads/ProductImages/6017_15_191.jpg",
            "picture": "http://www.technicaltextile.net/businessleads/ProductImages/6017_15_191.jpg",
            "photo": "http://www.technicaltextile.net/businessleads/ProductImages/6017_15_191.jpg",
            "link": "https://www.threadcrafts.in",
            "description": "test img desc"
        }
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded;"}
    tmp = requests.post(url, data=data_dict, headers=headers)
    print(tmp.status_code)
    print(tmp.text)


post_now()

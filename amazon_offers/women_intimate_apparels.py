from config import AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST
from config import AMAZON_AFFILIATE_URL
from amazon_offers import helpers as AMZ_helpers

EXCLUDE_PROFILE_IDS = ["280228608801032"]

MESSAGE_TEXT_LIST = [
    "Looking for that perfect gift for your girl? What's better than a Victoria's Secret present. Make her feel special, get them now",
    "Let this Valentine's Day be a special one. Gift your girl from an exclusive range of Victoria Secret's intimate apparels. Get them now",
    "You can still get your Valentine's Day gift on time. Shop from Victoria Secret's line of intimate apparels and gift here a unique gift this year.",
    "Victoria Secret's intimate apparels. Shop now and get amazing offers. Valentine's Day is just around the corner."
]

CHILD_ATTACHMENT_LIST = [
    {
        "name": "Front-Closure Pushup Bra",
        "description": "Underwired for extra support, Pushup Pads for that Awesome Look",
        "picture": "http://ecx.images-amazon.com/images/I/61Um%2BLpqpBL._UX522_.jpg",
        "link": "http://amzn.to/2jQOXap",
    },
    {
        "name": "Non Wired Push-Up Strapless Bra",
        "description": "Comes with translucent straps with sliders for adjustment",
        "picture": "http://ecx.images-amazon.com/images/I/71QqPMSoNAL._UX522_.jpg",
        "link": "http://amzn.to/2jOZnw6",
    },
    {
        "name": "Nightwear Babydoll Dress with Panty",
        "description": "ultimate in romance and luxury",
        "picture": "http://ecx.images-amazon.com/images/I/61H5RzNaGSL._UY550_.jpg",
        "link": "http://amzn.to/2jQWExb",
    },
    {
        "name": "Satin Babydoll Dress",
        "description": "Made from a sheer mesh,satin and lace",
        "picture": "http://ecx.images-amazon.com/images/I/71k-6sEW9uL._UY550_.jpg",
        "link": "http://amzn.to/2lbB20A",
    },
    {
        "name": "Multipurpose Front-Closure Women's Push-up Bra",
        "description": "Pushup T-shirt Seamless Cups Bra",
        "picture": "http://ecx.images-amazon.com/images/I/41LSFj6OpmL.jpg",
        "link": "http://amzn.to/2jQUcqE",
    },
    {
        "name": "Red & Black Lingerie Nightdress with G-string",
        "description": "A perfect sexy nightwear lingerie for those cuddling sessions under the sheets",
        "picture": "http://ecx.images-amazon.com/images/I/61gFiDHFpQL._UX466_.jpg",
        "link": "http://amzn.to/2jR0Wot",
    },
    {
        "name": "Red Crotchless Thong",
        "description": "Kaamastra - Sex positive!",
        "picture": "http://ecx.images-amazon.com/images/I/61iP06pdadL._UX522_.jpg",
        "link": "http://amzn.to/2kffNMZ",
    },
    {
        "name": "Padded Nonwired Demi Cup Bra",
        "description": "Seamless cups for 'No show look'",
        "picture": "http://ecx.images-amazon.com/images/I/91%2BxRJujcuL._UX522_.jpg",
        "link": "http://amzn.to/2kC3o6D",
    },
    {
        "name": "Purple Nightwear Nightdress Lingerie",
        "description": "See-through Nightwear",
        "picture": "http://ecx.images-amazon.com/images/I/41Q-4IzYrpL._UX425_.jpg",
        "link": "http://amzn.to/2jP2KmK",
    },
    {
        "name": "2 Piece Bra and Panty",
        "description": "Sexy Nightwear",
        "picture": "http://ecx.images-amazon.com/images/I/81%2Bn4xlQTKL._UY550_.jpg",
        "link": "http://amzn.to/2lbJA7y",
    },
]


def start_posting():
    AMZ_helpers.post_on_fb(AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST,
                           CHILD_ATTACHMENT_LIST,
                           MESSAGE_TEXT_LIST,
                           AMAZON_AFFILIATE_URL,
                           EXCLUDE_PROFILE_IDS)

from config import AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST
from config import AMAZON_AFFILIATE_URL
from amazon_offers import helpers as AMZ_helpers

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


def start_posting():
    AMZ_helpers.post_on_fb(AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST,
                           CHILD_ATTACHMENT_LIST,
                           MESSAGE_TEXT_LIST,
                           AMAZON_AFFILIATE_URL,
                           EXCLUDE_PROFILE_IDS)

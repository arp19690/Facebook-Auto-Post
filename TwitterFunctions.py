from TwitterAPI import TwitterAPI
from config import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, \
    TWITTER_ACCESS_TOKEN_KEY, TWITTER_ACCESS_TOKEN_SECRET
from facebookFunctions import download_photo, remove_photo, BASE_DIR
from amazon_offers.threadaffiliates import functions


def post_status_on_twitter(tweet_message, media_list=list()):
    api = TwitterAPI(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
                     TWITTER_ACCESS_TOKEN_KEY, TWITTER_ACCESS_TOKEN_SECRET)

    media_dict = None
    if len(media_list) > 0:
        media_dict = dict()
        for tmp_media in media_list:
            file = open(tmp_media, 'rb')
            media_data = file.read()
            media_dict.update({'media[]': media_data})

    r = api.request('statuses/update_with_media', {'status': tweet_message},
                    media_dict)
    return r


def post_multiple_tweets(tweets_list):
    for tweet_dict in tweets_list:
        tweet_message = tweet_dict[
                            "name"] + " @ " + functions.get_currency_symbol(
            tweet_dict["product_currency"]) + tweet_dict[
                            "price"] + ". Visit " + tweet_dict[
                            "threadcrafts_buy_link"]
        img_destination = BASE_DIR + 'tmpdata/' + tweet_dict["name"] + ".jpg"
        download_photo(tweet_dict["picture"], img_destination)
        post_status_on_twitter(tweet_message, media_list=[img_destination])
        remove_photo(img_destination)

    return True

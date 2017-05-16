import sys

from config import THREADAFFILIATES_FB_DETAILS
import helpers
import pymysql

reload(sys)
sys.setdefaultencoding('utf8')

WEBSITE_BASE_URL = "https://www.threadcrafts.in"


def get_db_connection():
    db = pymysql.connect(THREADAFFILIATES_FB_DETAILS["host"],
                         THREADAFFILIATES_FB_DETAILS["user"],
                         THREADAFFILIATES_FB_DETAILS["pass"],
                         THREADAFFILIATES_FB_DETAILS["name"])
    return db


def execute_query(sql, db=get_db_connection()):
    cursor = db.cursor()
    cursor.execute(sql)
    results = helpers.dictfetchall(cursor)
    cursor.close()
    return results


def get_post_message_list():
    message_list = [
        "Threadcrafts Store. Products exclusively handpicked for you.",
        "Exclusive range of products available only at Threadcrafts Store",
        "Amazing offers only on Threadcrafts Store",
        "Grab 'em before they are gone. Shop now.",
        "Great Indian Sale !!!",
    ]
    return message_list


def fetch_products(limit="0,20"):
    # Fetching a random category from products table
    product_data_sql = "SELECT product_category_id FROM products WHERE product_status = 1 ORDER BY rand() LIMIT 0,1"
    product_data_result = execute_query(product_data_sql)
    category_id = product_data_result[0]["product_category_id"]

    # Now fetching realted products for that particular category
    sql = "SELECT * FROM products WHERE product_status = 1 AND product_category_id = " + str(
        category_id) + " ORDER BY rand() LIMIT " + str(limit)
    data = execute_query(sql)
    output_list = list()
    if len(data) > 0:
        for tmpdata in data:
            post_data_dict = {
                "name": str(tmpdata["product_title"].decode('string_escape')),
                "price": str(int(tmpdata["product_price_min"])),
                "description": "Starts at Rs. " + str(
                    int(tmpdata["product_price_min"])),
                "picture": tmpdata["product_image_url"],
                "link": tmpdata["product_url_long"],
                "threadcrafts_buy_link": str(
                    WEBSITE_BASE_URL + "/buy-now/" + tmpdata[
                        "product_url_key"]),
            }
            output_list.append(post_data_dict)
    return output_list

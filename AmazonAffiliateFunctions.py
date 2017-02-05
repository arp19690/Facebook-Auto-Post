from config import AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST
from config import AMAZON_AFFILIATE_URL
from helpers import mac_notify
from amazon_offers import helpers as AMZ_helpers

from amazon_offers import general_links as GL
from amazon_offers import victoria_secret_cosmetics as VCS
from amazon_offers import women_intimate_apparels as WIP

# Posting Amazon Affiliate links - General Categories
print("Current Task: Posting General Amazon Links")
AMZ_helpers.post_on_fb(AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST,
                       GL.CHILD_ATTACHMENT_LIST,
                       GL.MESSAGE_TEXT_LIST,
                       AMAZON_AFFILIATE_URL)

# Posting Amazon Affiliate links - Victoria Secret Cosmetics
print("\nCurrent Task: Victoria Secret Cosmetics Links")
AMZ_helpers.post_on_fb(AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST,
                       VCS.CHILD_ATTACHMENT_LIST,
                       VCS.MESSAGE_TEXT_LIST,
                       AMAZON_AFFILIATE_URL,
                       VCS.EXCLUDE_PROFILE_IDS)

# Posting Amazon Affiliate links - Women Intimate Apparels
print("\nCurrent Task: Women Intimate Apparels Links")
AMZ_helpers.post_on_fb(AMAZON_AFFILIATE_DEALS_ACCESS_TOKENS_LIST,
                       WIP.CHILD_ATTACHMENT_LIST,
                       WIP.MESSAGE_TEXT_LIST,
                       AMAZON_AFFILIATE_URL,
                       WIP.EXCLUDE_PROFILE_IDS)

mac_notify("Affiliate links",
           "All promotional links have been posted successfully")

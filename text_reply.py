#====================================================
# text_reply.py
# YIHAN LINE BOT

# Created by YIHAN HISAO on May 21, 2021.
# Copyright © 2021 YIHAN HSIAO. All rights reserved.
#====================================================

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import json

#---------------- custom module ----------------
import text_push as text_push
import RSSfeed as RSSfeed
import tools as tools

from config import *
#---------------- global variables ----------------
user_status = "tutorial" # set user's usage status, default = tutorial, other = common_using
#---------------------------------------------------

        
        

def text_reply_message(user_message):
    #---------------------- Info recording ---------------------
    ## website name = ??
    ## site url = user_message
    ## article titles = web_info[nth article]['title']
    ## published dates = web_info[nth article]['published']
    ## articles' urls = web_info[nth article]['links'][0]['href']
    ## image to show = ??
    #-----------------------------------------------------------

    web_info = RSSfeed.findRSS( user_message ) # get website info
    # for i in range( len(web_info) ):
    #     print( web_info[i]['published'] ) # publish date of the article
    #     print( web_info[i]['title'] ) # title of the article
    #     print( web_info[i]['links'][0]['href'] ) # link of the article
    json_file_name = "newfile.json"
    tools.create_tracker_card_json(web_info, json_file_name, user_message) # use web info to modify the card's info

    FlexMessage = json.load( open("./json/"+json_file_name, 'r', encoding = 'utf-8') )
    output_message = FlexSendMessage( 'web', FlexMessage )
    return output_message

    # if( (user_message == "test") or (user_message == "Test") ):
    #     output_message = "This is a test."

    # elif(user_message == "profile"):
    #     FlexMessage = json.load( open("./json/card.json", 'r', encoding = 'utf-8') )
    #     output_message = FlexSendMessage( 'profile', FlexMessage )
    #     return output_message
    # else:  
    #     output_message = user_message  

    return TextSendMessage(text=output_message)
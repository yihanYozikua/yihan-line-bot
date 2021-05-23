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
import bot_functions as bot_functions

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

    return_message_array = []
    
    # user send new URL
    return_message_array = bot_functions.add_new_tracker( user_message )

    # if the user is in "tutorial status", then also reply the guiding text
    if (user_status == "tutorial"):
        return_message_array.append( TextSendMessage(text="已成功將網誌加入追蹤！請按上則訊息中的「按我看文章列表」以查看最新文章 ") )

    
    return return_message_array # because the amount of reply sometimes > 1, so return the array type

    # if( (user_message == "test") or (user_message == "Test") ):
    #     output_message = "This is a test."

    # elif(user_message == "profile"):
    #     FlexMessage = json.load( open("./json/card.json", 'r', encoding = 'utf-8') )
    #     output_message = FlexSendMessage( 'profile', FlexMessage )
    #     return output_message
    # return TextSendMessage(text=output_message)


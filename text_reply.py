#====================================================
# text_reply.py
## decide the response according to the input text
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
import requests
import re

#---------------- custom module ----------------
import text_push as text_push
import RSSfeed as RSSfeed
import tools as tools
import bot_functions as bot_functions

from config import *

#---------------- global variables ----------------

# set user's usage status, default = tutorial, other = common_using
user_status = "tutorial" 

# key words for detecting what action is it
action_key_word = [".*文章列表.*", ".*查看追蹤列表.*", ".*取消追蹤.*"] 
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


    ### Add_new_tracker
    if( requests.get(user_message).status_code == 200 ):
        # user send new URL
        return_message_array = bot_functions.add_new_tracker( user_message )

        # if the user is in "tutorial status", then also reply the guiding text
        if (user_status == "tutorial"):
            return_message_array.append( TextSendMessage(text="已成功將網誌加入追蹤！請按上則訊息中的「按我看文章列表」以查看最新文章 ") )
    
    
    ### Show_articles_card
    # elif( user_message == action_key_word[0] ):
        

    ### Show_tracker_list
    # elif( user_message == action_key_word[1] ):

    ### Delete_tracker
    # elif( user_message == action_key_word[2] ):
    
    

    
    return return_message_array # because the amount of reply sometimes > 1, so return the array type


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
    try:
        ### 加入追蹤 Add_new_tracker
        if requests.get( user_message ).status_code == 200:
            # user send new URL
            return_message_array = bot_functions.add_new_tracker( user_message )

            # if the user is in "tutorial status", then also reply the guiding text
            if (user_status == "tutorial"):
                return_message_array.append( TextSendMessage(text="已成功將網誌加入追蹤！") )
                return_message_array.append( TextSendMessage(text="請按上上則訊息中的「按我看文章列表」以查看最新文章") )

    except requests.exceptions.RequestException as e: # typeof(URL) != URL
        
        ### 查看最新文章 Show_articles_card =================================
        if( tools.analyze_text(user_message, action_key_word[0]) ):
            # split the "user_message" to get which website that user want to get
            ### split user_message ###

            # call function to get articles' cards
            return_message_array = bot_functions.show_articles_card( user_message )

            # if the user is in "tutorial status", then also reply the guiding text
            if (user_status == "tutorial"):
                return_message_array.append( TextSendMessage(text="成功看到這個網誌的最新文章列表囉！") )
                return_message_array.append( TextSendMessage(text="請按以下按鈕以查看追蹤清單",
                                                            quick_reply=QuickReply(items=[
                                                                            QuickReplyButton(
                                                                                action=MessageAction(
                                                                                    label="查看追蹤列表", 
                                                                                    text="查看追蹤列表"))
                                            ])) )
        

        ### 查看追蹤列表 Show_tracker_list =================================
        elif( tools.analyze_text(user_message, action_key_word[1]) ):
            
            # if the user is in "tutorial status", then also reply the guiding text
            if (user_status == "tutorial"):
                return_message_array.append( TextSendMessage(text="成功看到列表了！以上這些就是您目前已追蹤的網誌唷～") )
                return_message_array.append( TextSendMessage(text="請按上則訊息中的「取消追蹤」以取消追蹤此網誌") )
        

        ### 取消追蹤 Delete_tracker =================================
        elif( tools.analyze_text(user_message, action_key_word[2]) ):
            

            # if the user is in "tutorial status", then also reply the guiding text
            if (user_status == "tutorial"):
                return_message_array.append( TextSendMessage(text="已成功刪除一個追蹤項目！") )
                return_message_array.append( TextSendMessage(text="恭喜呀～您已完成試用！現在，試著加入自己想追蹤的網誌吧～") )


        ### 不認識的指令 Exception Handler
        else:
            return_message_array.append( TextSendMessage(text="咦這個指令沒看過耶"))

    return return_message_array # because the amount of reply sometimes > 1, so return the array type

        


        
            

    
    
    # ### Add_new_tracker
    # if( requests.get(user_message).status_code == 200 ):
    #     # user send new URL
    #     return_message_array = bot_functions.add_new_tracker( user_message )

    #     # if the user is in "tutorial status", then also reply the guiding text
    #     if (user_status == "tutorial"):
    #         return_message_array.append( TextSendMessage(text="已成功將網誌加入追蹤！請按上則訊息中的「按我看文章列表」以查看最新文章 ") )
    
    
    

    
    

    
    


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
#---------------- end of define module ----------------

def create_card_json(web_info, json_file_name, user_message):
    with open("./json/website_card.json", "r") as ffrom, open("./json/"+json_file_name, "w") as to:
        to_insert = json.load(ffrom)

        ### modify json info by user's input
        to_insert["hero"]["action"]["uri"] = user_message
        to_insert["body"]["action"]["uri"] = user_message
        to_insert["body"]["contents"][0]["text"] = "new WEBSITE NAME"
        to_insert["body"]["contents"][1]["text"] = user_message
        to_insert["body"]["contents"][2]["contents"][1]["action"]["uri"] = web_info[0]['links'][0]['href']
        to_insert["body"]["contents"][2]["contents"][1]["contents"][0]["text"] = web_info[0]['title']
        to_insert["body"]["contents"][2]["contents"][1]["contents"][1]["text"] = web_info[0]['published']
        to_insert["body"]["contents"][2]["contents"][2]["action"]["uri"] = web_info[1]['links'][0]['href']
        to_insert["body"]["contents"][2]["contents"][2]["contents"][0]["text"] = web_info[1]['title']
        to_insert["body"]["contents"][2]["contents"][2]["contents"][1]["text"] = web_info[1]['published']


        json.dump( to_insert, to )

        
        

def text_reply_message(user_message):
    ## website name = ??
    ## site url = user_message
    ## article titles = web_info[nth article]['title']
    ## published dates = web_info[nth article]['published']
    ## articles' urls = web_info[nth article]['links'][0]['href']
    ## image to show = ??

    web_info = RSSfeed.findRSS( user_message ) # get website info
    for i in range( len(web_info) ):
        print( web_info[i]['published'] ) # publish date of the article
        print( web_info[i]['title'] ) # title of the article
        print( web_info[i]['links'][0]['href'] ) # link of the article
    json_file_name = "newfile.json"
    create_card_json(web_info, json_file_name, user_message)

    ### use web info to modify the card's info
    

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
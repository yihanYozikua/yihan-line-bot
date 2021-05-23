#====================================================
# main.py
# YIHAN LINE BOT

# Created by YIHAN HISAO on May 21, 2021.
# Copyright © 2021 YIHAN HSIAO. All rights reserved.
#====================================================

from typing import Text
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from PIL import Image
from io import StringIO

import requests
import random
import json

#---------------- custom module ----------------
import text_push as text_push
import text_reply as text_reply
import RSSfeed as RSSfeed
import tools as tools

from config import *
#---------------- line settings ----------------
# Channel Access Token
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(CHANNEL_SECRET)
#---------------------------------------------------

app = Flask(__name__)


# monitor all the Post Requests come from /callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    # print("============= BODY =============")
    # print(body)
    # print("================================")
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# handle messages
@handler.add(MessageEvent)
def handle_message(event):
    # print(event)
    event_json = json.loads(str(event))

    # PARAMETERS
    # userId = event_json["source"]["userId"] # get user id
    userId = event.source.user_id   # get user's id
    line_bot_api.get_profile(userId) # get user's profile ## displayName | language | pictureUrl | userId
    start_tutorial_key_word = ".*開始試用.*"
    reply_message_arr = [] # make sure that the reply_message_array always be empty when init

    if event.message.type == "sticker":
        reply_message_arr.append(StickerSendMessage(
            package_id='11537',
            sticker_id=str(random.randint(52002734,52002773))
        ))
        line_bot_api.reply_message(event.reply_token, reply_message_arr) 


    elif event.message.type == "text":
        try: # typeof(URL) = URL
            req = requests.get( event.message.text )
            if req.status_code == 200:
                print("req = 200")
                user_message = event.message.text
                # reply_message_arr.append( text_reply.text_reply_message(user_message) )
                reply_message_arr = text_reply.text_reply_message(user_message)
            else:
                print("not exist")
                reply_message_arr.append( TextSendMessage(text="Oops找不到網站耶😨 請再檢查一下這個連結是否真的存在～～") )
                
        except requests.exceptions.RequestException as e: # typeof(URL) != URL
            # analyze if the input text = tutorial
            start_tutorial_or_not = tools.analyze_text( event.message.text, str(start_tutorial_key_word) )
            if start_tutorial_or_not: # input text = tutorial
                print("start tutorial")
                # start tutorial
                reply_message_arr.append( TextSendMessage(text="若您使用的是電腦，請您移至手機版操作唷！") )
                reply_message_arr.append( TextSendMessage(text='請按下以下按鈕以加入範例網誌URL',
                                                          quick_reply=QuickReply(items=[
                                                                        QuickReplyButton(
                                                                            action=MessageAction(
                                                                                label="按我加入網誌URL", 
                                                                                text="https://chloe981219.medium.com/"))
                                        ])))
            else:
                print("action try")
                # reply_message_arr.append( TextSendMessage(text="這個不是正確的URL唷，請再檢查一下這個連結是否真的存在～～") )
                reply_message_arr = text_reply.text_reply_message( event.message.text )

        line_bot_api.reply_message(event.reply_token, reply_message_arr)
        
        

        
        

    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
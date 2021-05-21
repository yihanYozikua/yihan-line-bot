#====================================================
# main.py
# YIHAN LINE BOT

# Created by YIHAN HISAO on May 21, 2021.
# Copyright © 2021 YIHAN HSIAO. All rights reserved.
#====================================================

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
import math
import time
import datetime

#---------------- custom module ----------------
import text_push as text_push
import text_reply as text_reply

#---------------- custom import ----------------
# from mykey import *
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
    print("============= BODY =============")
    print(body)
    print("================================")
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
    print(event)

    if event.message.type == "sticker":
        output_message = StickerSendMessage(
            package_id='11537',
            sticker_id=str(random.randint(52002734,52002773))
        )
        # output_message = TextSendMessage("u sends me a sticker")
        line_bot_api.reply_message(event.reply_token, output_message) 

    elif event.message.type == "text":
        user_message = event.message.text 
        output_message = text_reply.text_reply_message(user_message)
        line_bot_api.reply_message(event.reply_token, output_message)

    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
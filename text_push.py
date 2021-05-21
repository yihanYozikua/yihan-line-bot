#====================================================
# text_push.py
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

#---------------- self define variables ----------------
# from mykey import *
from config import *
#---------------- line settings ----------------
# Channel Access Token
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

TARGET_PUSH_ID = PUSH_TARGET_ID

#---------------------------------------------------

def text_push_message(msg):
	output_message = TextSendMessage(text=msg)
	line_bot_api.push_message(TARGET_PUSH_ID, output_message)


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

#---------------- self define module ----------------
import text_push as text_push
import json

#---------------- end of define module ----------------

def text_reply_message(user_message):
    if( (user_message == "test") or (user_message == "Test") ):
        output_message = "This is a test."

    elif(user_message == "profile"):
        FlexMessage = json.load( open("./json/card.json", 'r', encoding = 'utf-8') )
        output_message = FlexSendMessage( 'profile', FlexMessage )
        return output_message
    else:  
        output_message = user_message  

    return TextSendMessage(text=output_message)
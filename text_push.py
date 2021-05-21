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


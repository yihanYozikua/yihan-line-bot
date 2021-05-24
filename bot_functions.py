#====================================================
# bot_functions.py
## main functions of this bot
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
import re

#---------------- custom module ----------------
import text_push as text_push
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

# trigger by existing "URL"
def add_new_tracker( web_url ): # return a "FlexMssage" 
  web_info = RSSfeed.findRSS( web_url ) # get website info
  # json_file_name = "new.json" # new json file inorder to store new tracker info
  json_file_name = tools.create_tracker_card_json(web_info, web_url) # create new tracker card

  return_array = []
  FlexMessage = json.load( open("./json/website_list_cards/"+json_file_name, 'r', encoding = 'utf-8') )
  return_array.append( FlexSendMessage( 'web', FlexMessage ) )
  return return_array

# trigger by text "{Website name}文章列表"
def show_articles_card( web_name ):
  return_array = []

  ### Show articles' cards ###
  FlexMessage = tools.create_articles_card()
  return_array.append( FlexSendMessage( 'articles', FlexMessage ) )
  
  return return_array

# trigger by text "查看追蹤列表"
def show_tracker_list():
  return

# trigger by text "取消追蹤{Website name}"
def delete_tracker():
  ### Check if the user really want to delete the tracker, or he/she just makes a mistake
    ### if confirm "delete"

    ### else
  return
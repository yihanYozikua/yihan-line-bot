#====================================================
# user_db_manipulate.py
## manipulate user's DB
### CREATE
### MODIFY
### DELETE
### QUERY

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
import os

#---------------- custom module ----------------
import text_reply as text_reply
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


def create_db( userId ): # INIT create a json file to record user's data
  with open("./json/template_card/user_DB_template.json", "r") as template_json, open("./json/userDB/"+userId+".json", "w") as user_json:
    temp_json = json.load(template_json)
    temp_json["userId"] = userId
    temp_json["userName"] = line_bot_api.get_profile(userId).display_name

    json.dump( temp_json, user_json )

def modify_db():
  return

def delete_db():
  return

def query_db():
  return
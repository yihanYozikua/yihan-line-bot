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

# INIT create a json file to record user's data
def create_db( userId ): 
  with open("./json/template_card/user_DB_template.json", "r") as template_json, open("./json/userDB/"+userId+".json", "w") as user_json:
    temp_json = json.load(template_json)
    temp_json["userId"] = userId
    temp_json["userName"] = line_bot_api.get_profile(userId).display_name

    json.dump( temp_json, user_json )


# modify specific key's value
def modify_db( userId, key, new_value ):
  origin_file = "./json/userDB/"+userId+".json"
  new_file = "./json/userDB/"+userId+"_new.json"

  with open(origin_file, "r") as origin:
    origin_modify = json.load(origin)
    origin_modify[key] = new_value
  with open(origin_file, 'w') as new:
    json.dump(origin_modify, new)


# delete specific key and value
def delete_db( userId, key ):
  origin_file = "./json/userDB/"+userId+".json"
  
  with open(origin_file) as data_file:
    data = json.load(data_file)

  data.pop(key)

  with open(origin_file, 'w') as data_file:
    data = json.dump(data, data_file)

  # with open(origin_file, "r") as origin:
  #   origin_modify = json.load(origin)
  
  # ## delete element
  # for element in origin_modify:
  #   element.pop(key, None)
  
  # with open(origin_file, "w") as new:
  #   json.dump(origin_modify, new)


def addElement_db():
  return


# find the value of specific key
def query_db( userId, key ):
  with open("./json/userDB/"+userId+".json", "r") as jjson:
    jsonObj = json.load(jjson)
    value = jsonObj[key]
  return value

# user_db_manipulate.modify_db( "U1f3104a8e5bbe8ccf1c08e1412285500", "userName", "垂垂" )
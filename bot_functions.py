#====================================================
# bot_functions.py
## 4 functions of this bot
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
import user_db_manipulate as user_db_manipulate

from config import *
#---------------- line settings ----------------
# Channel Access Token
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(CHANNEL_SECRET)
#---------------------------------------------------

app = Flask(__name__)

# trigger by existing "URL" 
def add_new_tracker( web_url, userId ): # return a "FlexMssage" 
  return_array = []

  web_info = RSSfeed.findRSS( web_url ) # get website info
  if web_info == {}:
    return_array.append( TextSendMessage(text="Oops抱歉，這個網頁沒辦法追蹤耶😰") )
    return return_array
  
  ###================= insert new data to user's db =================
  crawl = tools.crwaling_web(web_url)
  web_name = crawl.title.get_text()
  web_image = crawl.find( "meta", property="og:image" ) # web_image["content"]
  if web_image is None:
    web_image = crawl.find_all( "link", rel="icon" )[-1]["href"]
  else:
    web_image = web_image["content"]

  tracker_to_insert = {
    "web_name": web_name,
    "web_url": web_url,
    "img_show": web_image,
    "articles": [
      {
      "title": web_info[0]['title'],
      "publish_date": web_info[0]['published'],
      "web_host_url": web_url,
      "article_url": web_info[0]['links'][0]['href'],
      # "summary": web_info[0]['summary']
      },
      {
      "title": web_info[1]['title'],
      "publish_date": web_info[1]['published'],
      "web_host_url": web_url,
      "article_url": web_info[1]['links'][0]['href'],
      # "summary": "texttexttexttexttexttexttexttexttexttexttexttext"
      }
    ]
  }
  user_db_manipulate.addElement_db( userId, "tracker_list", tracker_to_insert)
  ###================= insert new data to user's db END =================

  ###================= create new tracker card ==========================
  json_file_name = tools.create_tracker_card_json(web_info, web_url, userId) # create new tracker card

  
  FlexMessage = json.load( open("./json/userDB/"+userId+"/"+json_file_name, 'r', encoding = 'utf-8') )
  return_array.append( FlexSendMessage( 'web', FlexMessage ) )
  return return_array

# trigger by text "{Website name}文章列表"
def show_articles_card( web_name, userId ):
  return_array = []



  ### Show articles' cards ###
  FlexMessage = tools.create_articles_card(web_name, userId)
  return_array.append( FlexSendMessage( 'articles', FlexMessage ) )
  
  return return_array

# trigger by text "查看追蹤列表"
def show_tracker_list( userId ):
  # show tracker list (carousel)
  carousel_container = {
      "type": "carousel",
      "contents":[
      ]
  }
  for file in (os.listdir("./json/userDB/"+userId)):
      with open("./json/userDB/"+userId+"/"+file, "r") as bubble:
          bubble_data = json.load(bubble)
          carousel_container = tools.generate_carousel_cards(userId, carousel_container, bubble_data)
  return carousel_container

# trigger by text "取消追蹤{Website name}"
def delete_tracker( userId, web_name ):
  ### Check if the user really want to delete the tracker, or he/she just makes a mistake
    ### if confirm "delete"

    ### else
  
  ### Remove element inside the user's data(DB) ===========
  origin_file = "./json/userDB/"+userId+".json"
  
  with open(origin_file) as data_file:
    data = json.load(data_file)

  for element in data["tracker_list"]:
    print(element)
    if element["web_name"] == web_name:
      data["tracker_list"].remove(element)

  with open(origin_file, 'w') as data_file:
    data = json.dump(data, data_file)

  ### Delete card(.json) inside ".json/userDB/<userId>/" ===========
  os.remove("./json/userDB/"+userId+"/"+web_name+".json")

  return
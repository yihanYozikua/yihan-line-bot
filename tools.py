#====================================================
# tools.py
## commonly used tool functions
# YIHAN LINE BOT

# Created by YIHAN HISAO on May 21, 2021.
# Copyright © 2021 YIHAN HSIAO. All rights reserved.
#====================================================

import json
import requests
import random
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import os

from werkzeug.exceptions import RequestURITooLarge



def crwaling_web(web_url):
    # random choose header
    header_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]
    user_agent = random.choice(header_list)
    headers = {'User-Agent': user_agent}
    crawl_1 = urllib.request.Request(url=web_url, headers=headers)
    crawl = BeautifulSoup(urllib.request.urlopen(crawl_1), 'html.parser')

    return crawl

def create_tracker_card_json(web_info, web_url, userId):
  ### get user's data(DB)
  with open("./json/userDB/"+userId+".json", "r") as data:
    userData = json.load(data)
    # find the latest data
    index = len(userData["tracker_list"]) - 1
    user_tracker_latest = userData["tracker_list"][index]

  ### extract web title by crawling
  crawl = crwaling_web(web_url)
  web_name = crawl.title.get_text() # title of the website(HTML)

  json_file_name = web_name + ".json"

  with open("./json/template_card/website_card_template.json", "r") as ffrom, open("./json/userDB/"+userId+"/"+json_file_name, "w") as to:
    to_insert = json.load(ffrom)

    web_image = crawl.find( "meta", property="og:image" ) # web_image["content"]
    if web_image is None:
      web_image = crawl.find_all( "link", rel="icon" )[-1]["href"]
      to_insert["hero"]["url"] = web_image
    else:
      to_insert["hero"]["url"] = web_image["content"]

    to_insert["hero"]["action"]["uri"] = user_tracker_latest["web_url"] # web_url
    to_insert["body"]["action"]["uri"] = user_tracker_latest["web_url"] # web_url
    to_insert["body"]["contents"][0]["text"] = user_tracker_latest["web_name"] #web_name
    to_insert["body"]["contents"][1]["text"] = user_tracker_latest["web_url"] # web_url1
    to_insert["body"]["contents"][2]["contents"][1]["action"]["uri"] = user_tracker_latest["articles"][0]["article_url"] # article1's URL
    to_insert["body"]["contents"][2]["contents"][1]["contents"][0]["text"] = user_tracker_latest["articles"][0]["title"] # article1's title
    to_insert["body"]["contents"][2]["contents"][1]["contents"][1]["text"] = user_tracker_latest["articles"][0]["publish_date"] #article1's date
    to_insert["body"]["contents"][2]["contents"][2]["action"]["uri"] = user_tracker_latest["articles"][1]["article_url"]
    to_insert["body"]["contents"][2]["contents"][2]["contents"][0]["text"] = user_tracker_latest["articles"][1]["title"]
    to_insert["body"]["contents"][2]["contents"][2]["contents"][1]["text"] = user_tracker_latest["articles"][1]["publish_date"]


    json.dump( to_insert, to )
  
  return json_file_name

def create_articles_card(userId):
  ### get user's data(DB)
  with open("./json/userDB/"+userId+".json", "r") as data:
    userData = json.load(data)
    # find the latest data
    index = len(userData["tracker_list"]) - 1
    user_tracker_latest = userData["tracker_list"][index]



  with open( "./json/template_card/carousel_card_template.json", "r" ) as ffrom:
    output_json = json.load(ffrom)

    ### modify the info showing on the card of the 1st article
    output_json["contents"][0]["body"]["action"]["uri"] = "https://note.com/monotaro_note" # article url
    output_json["contents"][0]["body"]["contents"][0]["action"]["uri"] = "https://chloe981219.medium.com/" # website url
    output_json["contents"][0]["body"]["contents"][0]["contents"][0]["text"] = "name" # website name
    output_json["contents"][0]["body"]["contents"][1]["contents"][0]["text"] = "title" # Article title
    output_json["contents"][0]["body"]["contents"][1]["contents"][1]["text"] = "date" # publish date
    output_json["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][0]["text"] = "summary"

    
  ### return json object
  return output_json

def analyze_text( input_text, pattern ): # find if the input text is matched to the pattern
  if re.fullmatch( pattern, input_text ):
    print("matched!")
    analysis = True
    return analysis

def find_files(filename, search_path):
  search_result = []
  # Walking through top-down from the root
  for root, dir, files in os.walk(search_path):
    if filename in files:
      search_result.append(os.path.join(root, filename))
  if len( search_result ) > 0:
    result = True
  else:
    result = False
    
  return result

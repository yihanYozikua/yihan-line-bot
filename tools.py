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

from werkzeug.exceptions import RequestURITooLarge



def create_tracker_card_json(web_info, web_url):
    ### extract web title by crawling
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
    web_name = crawl.title.get_text() # title of the website(HTML)

    json_file_name = web_name + ".json"

    with open("./json/website_card.json", "r") as ffrom, open("./json/website_list_cards/"+json_file_name, "w") as to:
        to_insert = json.load(ffrom)

        web_image = crawl.find( "meta", property="og:image" ) # web_image["content"]
        if web_image is None:
          web_image = crawl.find_all( "link", rel="icon" )[-1]["href"]
          to_insert["hero"]["url"] = web_image
        else:
          to_insert["hero"]["url"] = web_image["content"]

        ### modify json info by user's input
        # if web_image is None:
        #   return #=== do nothing ===
        # elif web_image:
        #   to_insert["hero"]["url"] = web_image["content"]
        to_insert["hero"]["action"]["uri"] = web_url
        to_insert["body"]["action"]["uri"] = web_url
        to_insert["body"]["contents"][0]["text"] = web_name
        to_insert["body"]["contents"][1]["text"] = web_url
        to_insert["body"]["contents"][2]["contents"][1]["action"]["uri"] = web_info[0]['links'][0]['href']
        to_insert["body"]["contents"][2]["contents"][1]["contents"][0]["text"] = web_info[0]['title']
        to_insert["body"]["contents"][2]["contents"][1]["contents"][1]["text"] = web_info[0]['published']
        to_insert["body"]["contents"][2]["contents"][2]["action"]["uri"] = web_info[1]['links'][0]['href']
        to_insert["body"]["contents"][2]["contents"][2]["contents"][0]["text"] = web_info[1]['title']
        to_insert["body"]["contents"][2]["contents"][2]["contents"][1]["text"] = web_info[1]['published']


        json.dump( to_insert, to )
    
    return json_file_name

def analyze_text( input_text, pattern ): # find if the input text is matched to the pattern
  if re.fullmatch( pattern, input_text ):
    print("matched!")
    analysis = True
    return analysis


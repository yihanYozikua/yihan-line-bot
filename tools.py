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

from werkzeug.exceptions import RequestURITooLarge



def create_tracker_card_json(web_info, json_file_name, user_message):
    with open("./json/website_card.json", "r") as ffrom, open("./json/"+json_file_name, "w") as to:
        to_insert = json.load(ffrom)

        ### modify json info by user's input
        to_insert["hero"]["action"]["uri"] = user_message
        to_insert["body"]["action"]["uri"] = user_message
        to_insert["body"]["contents"][0]["text"] = "new WEBSITE NAME"
        to_insert["body"]["contents"][1]["text"] = user_message
        to_insert["body"]["contents"][2]["contents"][1]["action"]["uri"] = web_info[0]['links'][0]['href']
        to_insert["body"]["contents"][2]["contents"][1]["contents"][0]["text"] = web_info[0]['title']
        to_insert["body"]["contents"][2]["contents"][1]["contents"][1]["text"] = web_info[0]['published']
        to_insert["body"]["contents"][2]["contents"][2]["action"]["uri"] = web_info[1]['links'][0]['href']
        to_insert["body"]["contents"][2]["contents"][2]["contents"][0]["text"] = web_info[1]['title']
        to_insert["body"]["contents"][2]["contents"][2]["contents"][1]["text"] = web_info[1]['published']


        json.dump( to_insert, to )

def analyze_text( input_text, pattern ): # find if the input text is matched to the pattern
  if re.fullmatch( pattern, input_text ):
    print("matched!")
    analysis = True
    return analysis


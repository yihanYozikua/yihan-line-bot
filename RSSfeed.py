#====================================================
# RSSfeed.py
## find RSS url
## parse the RSS url

# YIHAN LINE BOT

# Created by YIHAN HISAO on May 21, 2021.
# Copyright © 2021 YIHAN HSIAO. All rights reserved.
#====================================================
import requests
import json
import feedparser


def findRSS( site_url ):
  ### Find RSS url
  my_params = {'url':site_url}
  r = requests.get('https://feedsearch.dev/api/v1/search', params=my_params)
  j = json.loads(r.text)
  RSS_url = j[0]["self_url"]  

  ### Find keys and values
  NewsFeed = feedparser.parse(RSS_url)
  return NewsFeed['entries']

import requests
import json
import feedparser


def findRSS( site_url ):
  ### Find RSS url
  my_params = {'url':site_url}
  r = requests.get('https://feedsearch.dev/api/v1/search', params=my_params)
  j = json.loads(r.text)
  print("length of = ")
  print( len(j) )
  # if len(j) > 1:
  #   RSS_url = j[1]["self_url"]
  # else:
  #   RSS_url = j[0]["self_url"]
  # print( RSS_url )
  RSS_url = j[0]["self_url"]
  

  ### Find keys and values
  NewsFeed = feedparser.parse(RSS_url)
  # print(NewsFeed)
  # print( len(NewsFeed['entries']) )
  # print( NewsFeed['entries'] )

  # for i in range( len(NewsFeed['entries']) ):
  #   print( NewsFeed['entries'][i]['published'] ) # publish date of the article
  #   print( NewsFeed['entries'][i]['title'] ) # title of the article
  #   print( NewsFeed['entries'][i]['links'][0]['href'] ) # link of the article
    # print( NewsFeed['entries'][i]['summary_detail']['value'] ) # summary of the article
  # print( NewsFeed['feed']['updated'] )
  # print( NewsFeed['entries'][0]['published'] )

  # print("=================================")
  return NewsFeed['entries']



# if __name__ == "__main__":
#   findRSS('https://medium.com/@chloe981219')
  # findRSS('https://note.com/monotaro_note')
  # findRSS('https://medium.com/')
  # findRSS('https://www.willstyle.co.jp/')

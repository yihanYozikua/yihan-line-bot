# 💌 網頁追蹤器YI  (LINE Bot)💌
> **Blog TrackerYI**
<!-- ## Table of Contents -->
> * [Dev Tools](#dev-tools)
> * [Files Description](#files-description)
> * [Reference](#reference)
> * [Features Demo](#features-demo)

Since searching online becomes the most common method to gain information or knowledge, web pages are inseparable from our daily lives.
Blog is one of the web pages. Medium, news, iThome, ..., there are more and more blogs we would like to read and subscribe, and each one has its "subscription button" for us to press. Soon after we press the button, the blog will start to send newsletter frantically to our Email until we finally can't stand it and want to unsubscribe.
Therefore, in this LINE Bot, I try to make the user can subscribe them all in only one place, unsubscribe easily, and say goodbye to annoying newsletters!

---
There are **4 features** in this LINE Bot:
1. Add Blog tracker
2. Check the latest articles
3. Check the tracking list
4. Cancel tracking (Delete tracker)

---

From now on, you no longer need to endure annoying newsletters and inconvenient ways to unsubscribe, **Welcome play!**
```
LINE@: @847kutjv
```
![](https://i.imgur.com/t1bSRu9.png)





## Dev Tools
* **Python3.8**
* **LINE Bot**：LINE Official Message API
* **Flask**：Backend
* **[Feedsearch API](https://feedsearch.dev/)**：Find blog's RSS feed url
* **[Feedparser](https://pythonhosted.org/feedparser/)**：Parse the RSS blog
* **[BeautifulSoup(bs4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**：Web Crawler


## Files Description
* **main.py**：Handler, link to Port
* **text_reply.py**：Decide the response according to the user's input text
* **text_push.py**：Push message, unused
* **bot_function.py**：Implement the main 4 features of this LINE Bot
* **RSSfeed.py**：Find RSS url and parse it
* **tools.py**：Basic tool functions which are commonly used
* **user_db_manipulate.py**：Basic manipulations of DB

## Reference
* [LINE Bot Python SDK](https://github.com/line/line-bot-sdk-python)
* [LINE Message API Documentation](https://developers.line.biz/en/docs/messaging-api/)

## Features Demo
### Add Blog tracker
<div>
     <img src="https://i.imgur.com/GpNklLz.jpg" alt="Add-Blog-tracker" width="50%" height="50%"/> 
</div>

### Check the latest articles
<div>
     <img src="https://i.imgur.com/oXer4eg.png" alt="check-latest-articles" width="50%" height="50%"/> 
</div>

### Check the tracking list
<div>
     <img src="https://i.imgur.com/G9BEOAU.png" alt="chech-tracking-list" width="50%" height="50%"/> 
</div>

### Cancel tracking (Delete tracker)
<div>
     <img src="https://i.imgur.com/hBQTqOi.png" alt="cancel-tracking" width="50%" height="50%"/> 
</div>

### Exception Handler
#### Avoid repeating add
<div>
 <img src="https://i.imgur.com/uWr4qHW.png" alt="avoid-repeating-add" width="50%" height="50%"/> 
</div>

#### Guide to enter the correct keywords
<div>
 <img src="https://i.imgur.com/Aw6RR5D.png" alt="guide-enter-correct" width="50%" height="50%"/> 
</div>

#### Error remind
<div>
 <img src="https://i.imgur.com/vKPcE1T.png" alt="error-remind" width="50%" height="50%"/> 
</div>

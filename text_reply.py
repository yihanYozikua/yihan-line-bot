#====================================================
# text_reply.py
# YIHAN LINE BOT

# Created by YIHAN HISAO on May 21, 2021.
# Copyright © 2021 YIHAN HSIAO. All rights reserved.
#====================================================

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#---------------- self define module ----------------
import text_push as text_push
import json

#---------------- end of define module ----------------

def text_reply_message(user_message):
    if( (user_message == "test") or (user_message == "Test") ):
        output_message = "This is a test."
    elif((user_message == "image") or (user_message == "img")):
        output_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/GcHBHJQ.jpg',
            preview_image_url='https://i.imgur.com/GcHBHJQ.jpg'
        )
        return output_message
    elif(user_message == "audio"):
        output_message = AudioSendMessage(
            original_content_url='https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3',
            duration=3000
        )
        return output_message
    elif(user_message == "show"):
        output_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/qk5dlO9.jpg',
                image_aspect_ratio='rectangle',
                image_size='cover',
                image_background_color='#FFFFFF',
                title='YIHAN HSIAO',
                text='Please select',
                default_action=URIAction(
                    label='view detail',
                    uri='https://github.com/yihanYozikua'
                ),
                actions=[
                    PostbackAction(
                        label='postback',
                        display_text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    LocationAction(
                        label='location'
                    ),
                    DatetimePickerAction(
                        label='Select date',
                        data='storeId=12345',
                        mode='datetime',
                        initial="2018-12-25T00:00",
                        min='2017-01-24T23:59',
                        max='2018-12-25T00:00'
                    )
                ]
            )
        )
        return output_message
    
    elif(user_message == "profile"):
        FlexMessage = json.load( open("./json/card.json", 'r', encoding = 'utf-8') )
        output_message = FlexSendMessage( 'profile', FlexMessage )
        return output_message
    else:  
        output_message = user_message  

    return TextSendMessage(text=output_message)
from re import search
import time
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from internet_check import main2

error_area = []

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('QIsD3hg2VgTge6iTh/bSfUjUOgMdPlBCPXlTtG/5bOfeq2PqAVufvH192wO/XgxlrmRV7Vnrk630vS9EbYq+XnyHoCzNFD+VH67TgIT77eCTylU28zpbo/f++TVrL5QNP5jBo4225ZREsD2eeZFxXgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7725e2081253d481db9edd9273be30f0')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'



# def push_warning():
#     global error_area
#     ans = ''
#     user_id =  'U33dcbe139d669eb71298956ab6e24a08'
#     line_bot_api.push_message(user_id, 
#             TextSendMessage(text="123"))
    # for i in range(197):
    #     ip,name,status,ping = main2(i)
    #     if ip != 'None':
    #         ans  = ans  + name + '--目前網路無法使用'+ '\n'
    # line_bot_api.push_message('<to>', 
    #         TextSendMessage(text=ans))
    # print('done')
    
                        
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'start':
        user_id =  event.source.user_id
        line_bot_api.push_message(user_id, 
                TextSendMessage(text="123"))
        print(123)
        ans = main2()
        line_bot_api.push_message(user_id, 
            TextSendMessage(text=ans))
        print('done')



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

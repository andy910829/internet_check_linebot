# from flask_ngrok import run_with_ngrok
# from flask import Flask, request

# # 載入 LINE Message API 相關函式庫
# from linebot import LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import MessageEvent, TextMessage, TextSendMessage

# # 載入 json 標準函式庫，處理回傳的資料格式
# import json

# app = Flask(__name__)

# @app.route("/", methods=['POST'])
# def linebot():
#     body = request.get_data(as_text=True)                    # 取得收到的訊息內容
#     try:
#         json_data = json.loads(body)                         # json 格式化訊息內容
#         access_token =  ''
#         secret = ''
#         line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確
#         handler = WebhookHandler(secret)                     # 確認 secret 是否正確
#         signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
#         handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
#         msg = json_data['events'][0]['message']['text']      # 取得 LINE 收到的文字訊息
#         tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
#         line_bot_api.reply_message(tk,TextSendMessage(msg))  # 回傳訊息
#         print(msg, tk)                                       # 印出內容
#     except:
#         print(body)                                          # 如果發生錯誤，印出收到的內容
#     return 'OK'                 # 驗證 Webhook 使用，不能省略
# if __name__ == "__main__":
#   run_with_ngrok(app)           # 串連 ngrok 服務
#   app.run()

# @app.route("/", methods=['POST'])
# def linebot():
#     body = request.get_data(as_text=True)                    # 取得收到的訊息內容
#     try:
#         json_data = json.loads(body)                         # json 格式化訊息內容
#         access_token =  ''
#         secret = ''
#         line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確
#         handler = WebhookHandler(secret)                     # 確認 secret 是否正確
#         signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
#         handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
#         msg = json_data['events'][0]['message']['text']      # 取得 LINE 收到的文字訊息
#         tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
#         line_bot_api.reply_message(tk,TextSendMessage(msg))  # 回傳訊息
#         print(msg, tk)                                       # 印出內容
#     except:
#         print(body)                                          # 如果發生錯誤，印出收到的內容
#     return 'OK'    
# def linebot(request):
#     try:
#         access_token = ''
#         secret = ''
#         body = request.get_data(as_text=True)
#         json_data = json.loads(body)
#         line_bot_api = LineBotApi(access_token)
#         handler = WebhookHandler(secret)
#         signature = request.headers['X-Line-Signature']
#         handler.handle(body, signature)
#         msg = json_data['events'][0]['message']['text']
#         tk = json_data['events'][0]['replyToken']
#         line_bot_api.reply_message(tk,TextSendMessage(msg))
#         print(msg, tk)
#     except:
#         print(request.args)
#     return 'OK'


# def push_warning():
#     global error_area
#     ans = ''
#     user_id =  ''
#     line_bot_api.push_message(user_id, 
#             TextSendMessage(text="123"))
#     for i in range(197):
#         ip,name,status,ping = main2(i)
#         if ip != 'None':
#             ans  = ans  + name + '--目前網路無法使用'+ '\n'
#     line_bot_api.push_message('<to>', 
#             TextSendMessage(text=ans))
#     print('done')


# while True:
        #     line_bot_api.push_message(user_id, 
        #                 TextSendMessage(text="123"))
        #     print('123')
        #     await wait_for(line_bot_api.push_message(  # 回復傳入的訊息文字
        #                     user_id,
        #                     TemplateSendMessage(
        #                         alt_text='Buttons template',
        #                         template=ButtonsTemplate(
        #                             title='學校網路測試',
        #                             text='點下面按鈕開始測試',
        #                             actions=[
        #                                 MessageTemplateAction(
        #                                     label='開始測試',
        #                                     text='開始測試'
        #                                 )
        #                             ]
        #                         )
        #                     )
        #                 ))
        #if event.message.text == 'test':

       # global count
        # thread_list = []
        # if event.message.text != 'start':
        # thread_list.append(threading.Thread(target = reply, args = (user_id, event.message.text)))
        # thread_list[count].start()
        # count+=1
       
        # line_bot_api.reply_message(event.reply_token, 
        #     TextSendMessage(text=checker.ans))

#     while True:
#         print('123')
#         # if reply_message == 'start':
#         #     line_bot_api.push_message(                          # 回復傳入的訊息文字
#         #                     user_id,
#         #                     TemplateSendMessage(
#         #                         alt_text='Buttons template',
#         #                         template=ButtonsTemplate(
#         #                             title='學校網路測試',
#         #                             text='點下面按鈕開始測試',
#         #                             actions=[
#         #                                 MessageTemplateAction(
#         #                                     label='開始測試',
#         #                                     text='開始測試'
#         #                                 )
#         #                             ]
#         #                         )
#         #                     )
#         #                 )
#         if reply_message == '開始測試':
#             line_bot_api.push_message(user_id, 
#             TextSendMessage(text=checker.ans))
#             line_bot_api.push_message(                          # 回復傳入的訊息文字
#                             user_id,
#                             TemplateSendMessage(
#                                 alt_text='Buttons template',
#                                 template=ButtonsTemplate(
#                                     title='學校網路測試',
#                                     text='點下面按鈕開始測試',
#                                     actions=[
#                                         MessageTemplateAction(
#                                             label='開始測試',
#                                             text='開始測試'
#                                         )
#                                     ]
#                                 )
#                             )
#                         )
#         else:
#             pass


    # line_bot_api.push_message(                          # 回復傳入的訊息文字
    #                         user_id,
    #                         TemplateSendMessage(
    #                             alt_text='Buttons template',
    #                             template=ButtonsTemplate(
    #                                 title='學校網路測試',
    #                                 text='點下面按鈕開始測試',
    #                                 actions=[
    #                                     MessageTemplateAction(
    #                                         label='開始測試',
    #                                         text='開始測試'
    #                                     )
    #                                 ]
    #                             )
    #                         )
    #                     )
    # line_bot_api.reply_message(event.reply_token, 
    #         TextSendMessage(text='掃描中...'))

# line_bot_api.reply_message(event.reply_token, 
            #     TextSendMessage(text=checker.ans))
            # time.sleep(3)
            # line_bot_api.push_message(                          # 回復傳入的訊息文字
            #                 user_id,
            #                 TemplateSendMessage(
            #                     alt_text='Buttons template',
            #                     template=ButtonsTemplate(
            #                         title='學校網路測試',
            #                         text='點下面按鈕開始測試',
            #                         actions=[
            #                             MessageTemplateAction(
            #                                 label='開始測試',
            #                                 text='開始測試'
            #                             )
            #                         ]
            #                     )
            #                 )
            #             )
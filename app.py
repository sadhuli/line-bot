from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 設定你的Channel Access Token和Channel Secret
line_bot_api = LineBotApi('Fza9JYs3h+FBnArGLOw1BuCmyuHZjwyh9M7/0Dcjmtz6mtfTFBeWjeGec2ENzMKW+q7z7pJ4NpKSiWAn7sYECcL4Es0dODXCO/fQM0jlTw14P8/CCCCCCCCCU機機組5p 4t89/1O/w1cDnyilFU=')
handler = WebhookHandler('44861cf5ff1c9b69bdbf1f15cb01b309')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    reply_text = f"你說了: {text}"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))

if __name__ == "__main__":
    app.run()

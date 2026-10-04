import os
import time
from flask import Flask, request, abort
from fuzzywuzzy import process
from rivescript import RiveScript
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
app = Flask(__name__)
bot = RiveScript()
bot.load_file("data.rive")
bot.sort_replies()
factory = StemmerFactory()
stemmer = factory.create_stemmer()
line_bot_api = LineBotApi('API_KEY')
handler = WebhookHandler('Channel')
matching = ['example string 1', 'example string 2', 'example string 3']
def time_to_int(t):
    t = t.replace(' ', '').replace('-', '').replace(':', '')
    return time.mktime(datetime.strptime(t, "%Y%m%d%H%M%S").timetuple())
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
    msg_stem = stemmer.stem(text)
    fuzzy_result = process.extractOne(msg_stem, matching)
    if isinstance(event.source, SourceUser):
        userId = event.source.user_id
        app.logger.info("User ID: " + userId)
    reply = bot.reply("localuser", fuzzy_result[0])
    if reply == '[ERR: No Reply Matched]':
        reply = 'Maaf Saat ini IslamicBot belum faham apa yang anda maksud, silahkan gunakan pertanyaan yang benar'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
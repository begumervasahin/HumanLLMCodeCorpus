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
LINE_API_KEY = 'API_KEY'
LINE_CHANNEL_SECRET = 'Channel'
line_bot_api = LineBotApi(LINE_API_KEY)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
matching_phrases = ['example string 1', 'example string 2', 'example string 3']
def time_to_int(t):
    t = t.replace(' ', '').replace('-', '').replace(':', '')
    return time.mktime(time.strptime(t, "%Y%m%d%H%M%S"))
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: %s", body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    stemmed_text = stemmer.stem(text)
    matched_phrase, match_score = process.extractOne(stemmed_text, matching_phrases)
    user_id = event.source.user_id if isinstance(event.source, SourceUser) else 'unknown'
    app.logger.info("User ID: %s, Message: %s, Stemmed: %s, Matched: %s (%d%%)",
                    user_id, text, stemmed_text, matched_phrase, match_score)
    reply = bot.reply("localuser", matched_phrase)
    if reply == '[ERR: No Reply Matched]':
        reply = 'Maaf Saat ini IslamicBot belum faham apa yang anda maksud, silahkan gunakan pertanyaan yang benar'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
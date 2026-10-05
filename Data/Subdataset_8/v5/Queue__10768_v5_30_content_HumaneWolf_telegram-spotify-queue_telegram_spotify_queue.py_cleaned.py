from configparser import ConfigParser
from datetime import datetime
import logging
from queue import Queue
import spotipy
import spotipy.util as sputil
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from threading import Lock, Timer
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s :\t%(message)s')
config = ConfigParser()
config.read('config.ini')
users = {}
music_queue = Queue()
now_playing = None
np_lock = Lock()
token = sputil.prompt_for_user_token(
    'SpotMain',
    'app-remote-control streaming',
    client_id=config['spotify']['client_id'],
    client_secret=config['spotify']['client_secret'],
    redirect_uri=config['spotify']['client_redirect']
)
if not token:
    logging.error('Failed to get token!')
spotify = spotipy.Spotify(auth=token)
def auth_guard(cb):
    def check_token(bot, update, *args, **kwargs):
        global sp_oauth, spotify
        token_info = sp_oauth.get_cached_token()
        if not token_info or sp_oauth.is_token_expired(token_info):
            token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        token = token_info['access_token']
        spotify = spotipy.Spotify(auth=token)
        cb(bot, update, *args, **kwargs)
    return auth_guard
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.search_result = None
    def __str__(self):
        return f'<User: {self.name} - {self.id}>'
class Song:
    def __init__(self, uri, artist, title, length, suggested_by):
        self.uri = uri
        self.artist = artist
        self.title = title
        self.length = length
        self.suggested_by = suggested_by
    def __str__(self):
        return f'<Song: {self.artist} - {self.title} ({self.uri})>'
def perform_search(user, text):
    s = spotify.search(q=text, limit=1, type='track')
    if len(s['tracks']['items']) == 0:
        return None
    song = s['tracks']['items'][0]
    artist = 'Unknown'
    if len(song['artists']) != 0:
        artist = song['artists'][0]['name']
    return Song(
        uri=song['uri'],
        artist=artist,
        title=song['name'],
        length=song['duration_ms'] / 1000,
        suggested_by=user
    )
def handle_song_change():
    global now_playing
    np_lock.acquire()
    try:
        logging.info('Song change handling triggered.')
        if music_queue.empty():
            now_playing = None
            pause()
        else:
            next_song = music_queue.get()
            now_playing = next_song
            play_song(next_song)
            t = Timer(next_song.length, handle_song_change)
            t.start()
    finally:
        np_lock.release()
def queue_song(song):
    music_queue.put(song)
    logging.info(f'Added to queue: {song}')
    if now_playing is None:
        handle_song_change()
def play_song(song):
    spotify.start_playback(uris=[song.uri])
def pause():
    spotify.pause_playback()
def get_user(message):
    user_id = message.from_user.id
    username = message.from_user.username
    try:
        return users[user_id]
    except KeyError:
        logging.info(f'Added user {username} ({user_id})')
        user = User(user_id, username)
        users[user_id] = user
        return user
def confirm_song(bot, update):
    user = get_user(update.message)
    if user.search_result is None:
        update.message.reply_text('You have no active search results. Send me a message to search for a song.')
    else:
        queue_song(user.search_result)
        update.message.reply_text(f'{user.search_result.artist} - {user.search_result.title} has been queued. There are approx. {music_queue.qsize()} songs in the queue.')
        user.search_result = None
def start(bot, update):
    get_user(update.message)
    update.message.reply_text('Hi! You can send me a song and/or artist name to search for music, then add it to the queue!')
def on_message(bot, update):
    user = get_user(update.message)
    song = perform_search(user, update.message.text)
    if song is None:
        update.message.reply_text('Sorry, but I couldn\'t find any results for your search.')
    else:
        user.search_result = song
        update.message.reply_text(f'I found a song:\n{song.artist} - {song.title}\nEnter (or tap) /confirm to add it to the queue, or just send a message to search again!')
tg_updater = Updater(config['telegram']['token'])
dispatcher = tg_updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', start))
dispatcher.add_handler(CommandHandler('confirm', auth_guard(confirm_song)))
dispatcher.add_handler(MessageHandler(Filters.text, auth_guard(on_message)))
if __name__ == '__main__':
    tg_updater.start_polling()
    logging.info('Bot is nearly ready.')
    tg_updater.idle()
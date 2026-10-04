from configparser import ConfigParser
import logging
from queue import Queue
from datetime import datetime
import spotipy
import spotipy.util as sputil
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from threading import Lock, Timer
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s :\t%(message)s')
config = ConfigParser()
config.read('config.ini')
users = {}
music_queue = Queue()
now_playing = None
np_lock = Lock()
def authenticate_spotify():
    token = sputil.prompt_for_user_token(
        'SpotMain',
        'app-remote-control streaming',
        client_id=config['spotify']['client_id'],
        client_secret=config['spotify']['client_secret'],
        redirect_uri=config['spotify']['client_redirect']
    )
    if not token:
        logging.error('Failed to get token!')
        sys.exit(1)
    return spotipy.Spotify(auth=token)
spotify = authenticate_spotify()
def auth_guard(callback):
    def wrapper(update, context):
        global spotify
        token_info = spotify.auth_manager.get_cached_token()
        if not token_info or spotify.auth_manager.is_token_expired(token_info):
            token_info = spotify.auth_manager.refresh_access_token(token_info['refresh_token'])
        spotify = spotipy.Spotify(auth=token_info['access_token'])
        callback(update, context)
    return wrapper
class User:
    def __init__(self, user_id, name):
        self.id = user_id
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
    result = spotify.search(q=text, limit=1, type='track')
    if not result['tracks']['items']:
        return None
    song = result['tracks']['items'][0]
    artist = song['artists'][0]['name'] if song['artists'] else 'Unknown'
    return Song(
        uri=song['uri'],
        artist=artist,
        title=song['name'],
        length=song['duration_ms'] / 1000,
        suggested_by=user
    )
def handle_song_change():
    global now_playing
    with np_lock:
        logging.info('Handling song change.')
        if music_queue.empty():
            now_playing = None
            pause_playback()
        else:
            next_song = music_queue.get()
            now_playing = next_song
            play_song(next_song)
            Timer(next_song.length, handle_song_change).start()
def queue_song(song):
    music_queue.put(song)
    logging.info(f'Added to queue: {song}')
    if now_playing is None:
        handle_song_change()
def play_song(song):
    spotify.start_playback(uris=[song.uri])
def pause_playback():
    spotify.pause_playback()
def get_user(message):
    user_id = message.from_user.id
    username = message.from_user.username
    if user_id not in users:
        logging.info(f'Added user {username} ({user_id})')
        users[user_id] = User(user_id, username)
    return users[user_id]
def confirm_song(update, context):
    user = get_user(update.message)
    if not user.search_result:
        update.message.reply_text('You have no active search results. Send me a message to search for a song.')
        return
    queue_song(user.search_result)
    update.message.reply_text(
        f'{user.search_result.artist} - {user.search_result.title} has been queued. '
        f'There are approximately {music_queue.qsize()} songs in the queue.'
    )
    user.search_result = None
def start_command(update, context):
    get_user(update.message)
    update.message.reply_text('Hi! You can send me a song and/or artist name to search for music, then add it to the queue!')
def handle_message(update, context):
    user = get_user(update.message)
    song = perform_search(user, update.message.text)
    if not song:
        update.message.reply_text('Sorry, but I couldn\'t find any results for your search.')
    else:
        user.search_result = song
        update.message.reply_text(
            f'I found a song:\n{song.artist} - {song.title}\n'
            f'Enter (or tap) /confirm to add it to the queue, or just send a message to search again!'
        )
def setup_bot():
    tg_updater = Updater(config['telegram']['token'])
    dispatcher = tg_updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', start_command))
    dispatcher.add_handler(CommandHandler('confirm', auth_guard(confirm_song)))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, auth_guard(handle_message)))
    return tg_updater
if __name__ == '__main__':
    tg_updater = setup_bot()
    tg_updater.start_polling()
    logging.info('Bot is ready.')
    tg_updater.idle()
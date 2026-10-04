import argparse
import functools
import os
import socketio
import threading
from qmgr import QueueManager
parser = argparse.ArgumentParser(description='Karafun fair scheduler.')
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='Enable logging')
parser.add_argument('--hide-singers', action='store_true', help='Hide who queued each song')
parser.add_argument('channel', help='Karafun session ID')
args = parser.parse_args()
sio = socketio.Client(logger=args.verbose)
mtx = threading.Lock()
qm = QueueManager(args.hide_singers)
def mlock(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        with mtx:
            return f(*args, **kwargs)
    return inner
@sio.event
@mlock
def connect():
    if args.verbose:
        print('Connection established')
    sio.emit('authenticate', {
        'login': 'fair scheduler',
        'channel': args.channel,
        'role': 'participant',
        'app': 'karafun',
        'socket_id': None,
    })
@sio.event
@mlock
def loginAlreadyTaken():
    if args.verbose:
        print('Login already taken')
    sio.emit('authenticate', {
        'login': f'fair scheduler {os.getpid()}',
        'channel': args.channel,
        'role': 'participant',
        'app': 'karafun',
        'socket_id': None,
    })
@sio.event
@mlock
def permissions(data):
    if args.verbose:
        print('Permissions received:', data)
@sio.event
@mlock
def preferences(data):
    if args.verbose:
        print('Preferences received:', data)
    if not data.get('askSingerName'):
        print('You must turn on "Ask singer\'s name when adding to queue" in the Karafun remote control settings for the scheduler to work.')
        sio.disconnect()
@sio.event
@mlock
def status(data):
    if args.verbose:
        print('Status received:', data)
queue_handle_timer = threading.Timer(999.0, lambda: None)
@sio.event
@mlock
def queue(data):
    if args.verbose:
        print('Queue received:', data)
    @mlock
    def handle():
        action = qm.reconcile(data)
        if action:
            print('Sending:', action)
            sio.emit(action[0], action[1])
    global queue_handle_timer
    queue_handle_timer.cancel()
    queue_handle_timer = threading.Timer(0.3, handle)
    queue_handle_timer.start()
@sio.event
@mlock
def serverUnreacheable():
    print('Server unreachable. Try restarting the Karafun App?')
    sio.disconnect()
@sio.event
@mlock
def disconnect():
    print('Disconnected from server.')
sio.connect(f'https:
sio.wait()
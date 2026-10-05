import argparse
import functools
import os
import socketio
import threading
from qmgr import QueueManager
QUEUE_HANDLE_INTERVAL = 0.3
TIMER_CANCEL_DELAY = 999.0
parser = argparse.ArgumentParser(description='Karafun fair scheduler.')
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='enable logging')
parser.add_argument('--hide-singers', action='store_true', help='hide who queued each song')
parser.add_argument('channel', help='karafun session id')
args = parser.parse_args()
sio = socketio.Client(logger=args.verbose)
mutex = threading.Lock()
queue_manager = QueueManager(args.hide_singers)
def mutex_lock(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        with mutex:
            return func(*args, **kwargs)
    return inner
@sio.event
@mutex_lock
def connect():
    if args.verbose:
        print('Connection established')
    emit_authentication()
@sio.event
@mutex_lock
def loginAlreadyTaken():
    if args.verbose:
        print('Login already taken')
    emit_authentication(f'fair scheduler {os.getpid()}')
@sio.event
@mutex_lock
def permissions(data):
    if args.verbose:
        print('Permissions received ', data)
@sio.event
@mutex_lock
def preferences(data):
    if args.verbose:
        print('Preferences received ', data)
    if not data['askSingerName']:
        print('You must turn on "Ask singer\'s name when adding to queue" in the Karafun remote control settings in order for the scheduler to work.')
        sio.disconnect()
@sio.event
@mutex_lock
def status(data):
    if args.verbose:
        print('Status received ', data)
queue_handle_timer = threading.Timer(TIMER_CANCEL_DELAY, lambda: None)
@sio.event
@mutex_lock
def queue(data):
    if args.verbose:
        print('Queue received ', data)
    global queue_handle_timer
    queue_handle_timer.cancel()
    queue_handle_timer = threading.Timer(QUEUE_HANDLE_INTERVAL, handle_queue)
    queue_handle_timer.start()
@sio.event
@mutex_lock
def serverUnreachable():
    print('Server unreachable. Try restarting the Karafun App?')
    sio.disconnect()
@sio.event
@mutex_lock
def disconnect():
    print('Disconnected from server.')
def emit_authentication(login='fair scheduler', role='participant'):
    sio.emit('authenticate', {
        'login': login,
        'channel': args.channel,
        'role': role,
        'app': 'karafun',
        'socket_id': None,
    })
def handle_queue():
    action = queue_manager.reconcile(data)
    if action:
        print('Sending ', action)
        sio.emit(action[0], action[1])
sio.connect('https:
sio.wait()
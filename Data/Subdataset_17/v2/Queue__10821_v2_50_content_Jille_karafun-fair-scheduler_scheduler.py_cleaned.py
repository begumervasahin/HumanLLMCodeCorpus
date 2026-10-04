import argparse
import functools
import os
import socketio
import threading
from qmgr import QueueManager
def setup_argument_parser():
    parser = argparse.ArgumentParser(description='Karafun fair scheduler.')
    parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='enable logging')
    parser.add_argument('--hide-singers', action='store_true', help='hide who queued each song')
    parser.add_argument('channel', help='Karafun session ID')
    return parser.parse_args()
def setup_socket_client(verbose):
    return socketio.Client(logger=verbose)
def mlock(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        with mtx:
            return f(*args, **kwargs)
    return inner
@mlock
def on_connect():
    if args.verbose:
        print('Connection established')
    sio.emit('authenticate', {
        'login': 'fair scheduler',
        'channel': args.channel,
        'role': 'participant',
        'app': 'karafun',
        'socket_id': None,
    })
@mlock
def on_login_already_taken():
    if args.verbose:
        print('Login already taken')
    sio.emit('authenticate', {
        'login': f'fair scheduler {os.getpid()}',
        'channel': args.channel,
        'role': 'participant',
        'app': 'karafun',
        'socket_id': None,
    })
@mlock
def on_permissions(data):
    if args.verbose:
        print('Permissions received: ', data)
@mlock
def on_preferences(data):
    if args.verbose:
        print('Preferences received: ', data)
    if not data['askSingerName']:
        print('You must enable "Ask singer\'s name when adding to queue" in the Karafun remote control settings for the scheduler to work.')
        sio.disconnect()
@mlock
def on_status(data):
    if args.verbose:
        print('Status received: ', data)
@mlock
def on_queue(data):
    if args.verbose:
        print('Queue received: ', data)
    @mlock
    def handle_queue():
        action = qm.reconcile(data)
        if action:
            print('Sending action: ', action)
            sio.emit(action[0], action[1])
    global queue_handle_timer
    queue_handle_timer.cancel()
    queue_handle_timer = threading.Timer(0.3, handle_queue)
    queue_handle_timer.start()
@mlock
def on_server_unreachable():
    print('Server unreachable. Try restarting the Karafun App?')
    sio.disconnect()
@mlock
def on_disconnect():
    print('Disconnected from server.')
def main():
    global args, sio, mtx, qm, queue_handle_timer
    args = setup_argument_parser()
    sio = setup_socket_client(args.verbose)
    mtx = threading.Lock()
    qm = QueueManager(args.hide_singers)
    queue_handle_timer = threading.Timer(999.0, lambda: None)
    sio.on('connect', on_connect)
    sio.on('loginAlreadyTaken', on_login_already_taken)
    sio.on('permissions', on_permissions)
    sio.on('preferences', on_preferences)
    sio.on('status', on_status)
    sio.on('queue', on_queue)
    sio.on('serverUnreachable', on_server_unreachable)
    sio.on('disconnect', on_disconnect)
    sio.connect(f'https:
    sio.wait()
if __name__ == '__main__':
    main()
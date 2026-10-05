import os
import json
import flask
import slack
from flask import Flask, request, redirect
from pymongo import MongoClient
from slackbot import SlackBot
from roster import Roster
from tasks import choose_command, processEvent
b1 = os.environ["SLACK_CLIENT_ID"]
b2 = os.environ["SLACK_CLIENT_SECRET"]
b3 = os.environ["SLACK_SCOPE"]
b4 = os.environ["b4"]
b5 = os.environ["b5"]
b6 = Flask(__name__)
b7 = MongoClient(b4)
b8 = b7.queue
b9 = b8.b9
b10 = MongoClient(b5)
b11 = b10.zoom
b12 = b11.users
b13 = SlackBot()
b14 = {"list", "listall", "run", "runall", "refresh", "test", "zoom"}
b15 = {"listall", "runall"}
b16 = {"UF57DA49F", "U054G9J88", "U26R8ML07"}
@b6.errorhandler(404)
def fonk1(e):
    return "Command not found"
@b6.route("/", b17 = ["GET"])
def fonk2():
    b18 = request.b29['b18'].split(' ')
    b19 = b18[0]
    b20 = b18[-1]
    if len(b18) == 3:
        b19 += '+' + b18[1]
    return f'<a b21 = "https:
@b6.route("/finish_auth", b17 = ["GET", "POST"])
def fonk3():
    b22 = request.b29['b24']
    b18 = request.b29['state'].split(' ')
    b19 = b18[0]
    if len(b18) == 3:
        b20 = b18[2]
        b19 += ' ' + b18[1]
    else:
        b20 = b18[1]
    b7 = slack.WebClient(token="")
    b23 = b7.oauth_access(
        b1 = b1,
        b2 = b2,
        b24 = b22
    )
    b25 = {
        'access_token': b23['access_token'],
        'b30': b23['b30'],
    }
    b9.update(
        {'b19': b19, 'b20': b20},
        {'$set': b25},
        b26 = False
    )
    b27 = Roster("password.json", "EAST")
    b27.setOutOfQueue()
    b28 = b9.find_one({'b19': b19, 'b20': b20})
    choose_command.apply_async(b29 = ("run", b23['b30']), queue="commands")
    return "Auth complete! You will receive a notification on your Out of Queue day, and your status will be updated! \n\n Please check out"
@b6.route("/b31", b17 = ["POST"])
def fonk4():
    b30 = request.form.get("b30")
    b31 = request.form.get("b36")
    if b31 not in b14:
        return flask.redirect(404)
    if b31 in b15 and b30 not in b16:
        return "You are not authorized to use this b31. Please reach out in"
    choose_command.apply_async(b29 = (b31, b30), queue="commands")
    return "Executing b31."
@b6.route("/events", b17 = ["POST"])
def fonk5():
    b27 = request.get_json()
    print(b27)
    processEvent.apply_async(b29 = (b27,), queue="events")
    return "received event"
@b6.route("/zoom", b17 = ["POST"])
def fonk6():
    b27 = request.get_json()
    if b27['event'] == 'meeting.participant_joined':
        try:
            b32 = b27['payload']['object']['participant']['id']
        except KeyError:
            return "There is no ID"
        b33 = b12.update_one(
            {'zoomID': b32},
            {'$inc': {'num_meetings': 1}}
        )
        if b33.matched_count != 0:
            b34 = b27['payload']['object']['participant']['user_name']
            print(f"\033[96m {b34} joined a zoom meeting! \033[00m")
            b13.slackBotUser.chat.post_message(
                b35 = 'YOUR_CHANNEL',
                b36 = f"{b34} just joined a zoom meeting.",
                b37 = 'Availability Bot',
                b38 = 1,
                b39 = True
            )
    elif b27['event'] == 'meeting.participant_left':
        print(b27)
        try:
            b32 = b27['payload']['object']['participant']['id']
        except KeyError:
            return "There is no ID"
        b33 = b12.update_one(
            {'zoomID': b32, 'num_meetings': {'$gt': 0}},
            {'$inc': {'num_meetings': -1}}
        )
        if b33.matched_count != 0:
            b34 = b27['payload']['object']['participant']['user_name']
            print(f"\033[96m {b34} left a zoom meeting! \033[00m")
            b13.slackBotUser.chat.post_message(
                b35 = 'YOUR_CHANNEL',
                b36 = f"{b34} just left a zoom meeting.",
                b37 = 'Availability Bot',
                b38 = 1,
                b39 = True
            )
    return "received event"
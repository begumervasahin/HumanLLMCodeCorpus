import os
import slack
import flask
import json
from flask import Flask, request
from pymongo import MongoClient
from slackbot import SlackBot
from roster import Roster
from tasks import choose_command, processEvent
client_id = os.environ["SLACK_CLIENT_ID"]
client_secret = os.environ["SLACK_CLIENT_SECRET"]
oauth_scope = os.environ["SLACK_SCOPE"]
CONNECT_STRING = os.environ["CONNECT_STRING"]
ZOOM_MONGO = os.environ["ZOOM_MONGO"]
app = Flask(__name__)
client = MongoClient(CONNECT_STRING)
db = client.queue
employees = db.employees
zoomDBClient = MongoClient(ZOOM_MONGO)
zdb = zoomDBClient.zoom
zoomUsers = zdb.users
slack_bot = SlackBot()
COMMANDS = {"list", "listall", "run", "runall", "refresh", "test", "zoom"}
PRIVILEGED_COMMANDS = {"listall", "runall"}
PRIVILEGED_USERS = {"UF57DA49F", "U054G9J88", "U26R8ML07"}
@app.errorhandler(404)
def page_not_found(e):
    return "Command not found", 404
@app.route("/", methods=["GET"])
def pre_install():
    name_parts = request.args['name'].split(' ')
    first_name = name_parts[0]
    last_name = name_parts[-1]
    if len(name_parts) == 3:
        first_name += '+' + name_parts[1]
    return f'<a href="https:
@app.route("/finish_auth", methods=["GET", "POST"])
def post_install():
    auth_code = request.args['code']
    name_parts = request.args['state'].split(' ')
    first_name = name_parts[0]
    if len(name_parts) == 3:
        last_name = name_parts[2]
        first_name += ' ' + name_parts[1]
    else:
        last_name = name_parts[1]
    client = slack.WebClient(token="")
    response = client.oauth_access(client_id=client_id, client_secret=client_secret, code=auth_code)
    person = {
        'access_token': response['access_token'],
        'user_id': response['user_id'],
    }
    employees.update_one(
        {'first_name': first_name, 'last_name': last_name},
        {'$set': person},
        upsert=True
    )
    roster = Roster("password.json", "EAST")
    roster.setOutOfQueue()
    completed = employees.find_one({'first_name': first_name, 'last_name': last_name})
    choose_command.apply_async(args=("run", response['user_id']), queue="commands")
    return "Auth complete! You will receive a notification on your Out of Queue day, and your status will be updated!"
@app.route("/command", methods=["POST"])
def exec_command():
    user_id = request.form.get("user_id")
    command = request.form.get("text")
    if command not in COMMANDS:
        return "Command not found", 404
    if command in PRIVILEGED_COMMANDS and user_id not in PRIVILEGED_USERS:
        return "You are not authorized to use this command."
    choose_command.apply_async(args=(command, user_id), queue="commands")
    return "Executing command."
@app.route("/events", methods=["POST"])
def events():
    event_data = request.get_json()
    print(event_data)
    processEvent.apply_async(args=(event_data,), queue="events")
    return "Received event"
@app.route("/zoom", methods=["POST"])
def zoom():
    event_data = request.get_json()
    if event_data['event'] == 'meeting.participant_joined':
        handle_zoom_event(event_data, 'joined')
    elif event_data['event'] == 'meeting.participant_left':
        handle_zoom_event(event_data, 'left')
    return "Received event"
def handle_zoom_event(event_data, action):
    try:
        cur_user = event_data['payload']['object']['participant']['id']
    except KeyError:
        return "There is no ID"
    if action == 'joined':
        match = zoomUsers.update_one({'zoomID': cur_user}, {'$inc': {'num_meetings': 1}})
    elif action == 'left':
        match = zoomUsers.update_one({'zoomID': cur_user, 'num_meetings': {'$gt': 0}}, {'$inc': {'num_meetings': -1}})
    if match.matched_count != 0:
        user_name = event_data['payload']['object']['participant']['user_name']
        action_text = "joined" if action == 'joined' else "left"
        print(f"\033[96m {user_name} {action_text} a zoom meeting! \033[00m")
        slack_bot.slackBotUser.chat.post_message(channel='
if __name__ == "__main__":
    app.run(debug=True)
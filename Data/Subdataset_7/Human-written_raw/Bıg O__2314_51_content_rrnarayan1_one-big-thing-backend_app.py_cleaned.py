import firebase_admin
from firebase_admin import firestore
import flask
from flask import request
import pandas as pd
from flask_cors import CORS
import numpy as np
from Teams import get_team_by_id
from Games import get_game, get_opp_game, get_games_stats, get_games_info_by_team_and_season
from Score import _get_scores, _get_default_data
b1 = flask.Flask(__name__)
b2 = CORS(b1)
firebase_admin.initialize_app()
b3 = firestore.client()
b4 = {
  "22016": "16-17Reg",
  "42016": "16-17Playoffs",
  "22017": "17-18Reg",
  "42017": "17-18Playoffs",
  "22018": "18-19Reg"
}
b5 = ['FGM', 'FGA', 'FG_PCT', 'FG3M','FG3A', \
'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', \
'AST','STL', 'BLK', 'TOV', 'PTS']
@b1.route('/')
def fonk1():
    return "Hello World"
@b1.route('/b9')
def fonk2():
    b6 = request.args.get('seasonId')
    b7 = request.args.get('teamId')
    b8 = request.args.get('gameId')
    if (not b6 or not b7 or not b8):
        return flask.abort(400)
    b9 = get_game(b3, b6, b7, b8)
    if not b9:
        return flask.abort(404)
    return flask.jsonify(b9)
@b1.route('/score')
def fonk3():
    b6 = request.args.get('seasonId')
    b7 = request.args.get('teamId')
    b8 = request.args.get('gameId')
    b10 = request.args.get('b10')
    b11 = request.args.get('b11')
    if (not b6 or not b7 or not b8):
        return flask.abort(400)
    b9 = get_game(b3, b6, b7, b8)
    b12 = get_opp_game(b3, b6, b7, b8)
    if (not b9):
        return flask.abort(404)
    b13 = get_team_by_id(b3, b9[u"TEAM_ID"])
    b14 = get_team_by_id(b3, b12[u"TEAM_ID"])
    if (not b13 or not b14):
        return flask.abort(404)
    if (not b10):
        b15 = int(b9[u"SEASON_ID"])
        b10, b11 = _get_default_data(b15, b9)
    if (b11 = = "before" and b9[u"SEASON_ID"] != b10):
        return flask.abort(422)
    b16 = get_games_stats(b3, b10, b11, b7, b9)
    if (not b16):
        return flask.abort(404)
    b17 = _get_scores(b16, b9)
    b17["b13"]=b13
    b17["b14"]=b14
    return flask.jsonify(b17)
@b1.route('/b20')
def fonk4():
    b6 = request.args.get('seasonId')
    b7 = request.args.get('teamId')
    b18 = request.args.get('withOBT')
    b19 = request.args.get('withSummary')
    if (not b6 or not b7):
        return flask.abort(400)
    b20 = get_games_info_by_team_and_season(b3, b6, b7, b18, b19)
    return flask.jsonify(b20)
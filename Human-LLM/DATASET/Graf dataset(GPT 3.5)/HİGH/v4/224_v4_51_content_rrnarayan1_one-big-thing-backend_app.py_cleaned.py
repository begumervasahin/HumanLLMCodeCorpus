import firebase_admin
from firebase_admin import firestore
import flask
from flask import request, jsonify, abort
import pandas as pd
from flask_cors import CORS
from Teams import get_team_by_id
from Games import get_game, get_opp_game, get_games_stats, get_games_info_by_team_and_season
from Score import _get_scores, _get_default_data
b1 = flask.Flask(__name__)
CORS(b1)
firebase_admin.initialize_app()
b2 = firestore.client()
b3 = {
    "22016": "16-17Reg",
    "42016": "16-17Playoffs",
    "22017": "17-18Reg",
    "42017": "17-18Playoffs",
    "22018": "18-19Reg"
}
b4 = ['FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                   'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']
@b1.route('/')
def fonk1():
    return "Hello World"
@b1.route('/b8')
def fonk2():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b7 = request.args.get('gameId')
    if not b5 or not b6 or not b7:
        return abort(400)
    b8 = get_game(b2, b5, b6, b7)
    if not b8:
        return abort(404)
    return jsonify(b8)
@b1.route('/score')
def fonk3():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b7 = request.args.get('gameId')
    b9 = request.args.get('b9')
    b10 = request.args.get('b10')
    if not b5 or not b6 or not b7:
        return abort(400)
    b8 = get_game(b2, b5, b6, b7)
    b11 = get_opp_game(b2, b5, b6, b7)
    if not b8:
        return abort(404)
    b12 = get_team_by_id(b2, b8[u"TEAM_ID"])
    b13 = get_team_by_id(b2, b11[u"TEAM_ID"])
    if not b12 or not b13:
        return abort(404)
    if not b9:
        b14 = int(b8[u"SEASON_ID"])
        b9, b10 = _get_default_data(b14, b8)
    if b10 = = "before" and b8[u"SEASON_ID"] != b9:
        return abort(422)
    b15 = get_games_stats(b2, b9, b10, b6, b8)
    if not b15:
        return abort(404)
    b16 = _get_scores(b15, b8)
    b16["b12"] = b12
    b16["b13"] = b13
    return jsonify(b16)
@b1.route('/b19')
def fonk4():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b17 = request.args.get('withOBT')
    b18 = request.args.get('withSummary')
    if not b5 or not b6:
        return abort(400)
    b19 = get_games_info_by_team_and_season(b2, b5, b6, b17, b18)
    return jsonify(b19)
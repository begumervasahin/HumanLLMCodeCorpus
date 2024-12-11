import firebase_admin
from firebase_admin import firestore
import flask
from flask import request, jsonify, abort
from flask_cors import CORS
import pandas as pd
from Teams import get_team_by_id
from Games import get_game, get_opp_game, get_games_stats, get_games_info_by_team_and_season
from Score import _get_scores, _get_default_data
b1 = flask.Flask(b23)
CORS(b1)
firebase_admin.initialize_app()
b2 = firestore.client()
b3 = ['FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                   'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']
b4 = {
    "22016": "16-17Reg",
    "42016": "16-17Playoffs",
    "22017": "17-18Reg",
    "42017": "17-18Playoffs",
    "22018": "18-19Reg"
}
@b1.route('/')
def fonk1():
    return "Hello World"
@b1.route('/b15')
def fonk2():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b7 = request.args.get('gameId')
    if not b5 or not b6 or not b7:
        return abort(400)
    b8 = fonk5(b5, b6, b7)
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
    b11 = fonk6(b5, b6, b7, b9, b10)
    if not b11:
        return abort(404)
    return jsonify(b11)
@b1.route('/b22')
def fonk4():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b12 = request.args.get('withOBT')
    b13 = request.args.get('withSummary')
    if not b5 or not b6:
        return abort(400)
    b14 = fonk7(b5, b6, b12, b13)
    return jsonify(b14)
def fonk5(b5, b6, b7):
    b15 = get_game(b2, b5, b6, b7)
    if not b15:
        return None
    return b15
def fonk6(b5, b6, b7, b9, b10):
    b15 = get_game(b2, b5, b6, b7)
    b16 = get_opp_game(b2, b5, b6, b7)
    if not b15 or not b16:
        return None
    b17 = get_team_by_id(b2, b15[u"TEAM_ID"])
    b18 = get_team_by_id(b2, b16[u"TEAM_ID"])
    if not b17 or not b18:
        return None
    if not b9:
        b19 = int(b15[u"SEASON_ID"])
        b9, b10 = _get_default_data(b19, b15)
    if b10 = = "before" and b15[u"SEASON_ID"] != b9:
        return None
    b20 = get_games_stats(b2, b9, b10, b6, b15)
    if not b20:
        return None
    b21 = _get_scores(b20, b15)
    b21["b17"] = b17
    b21["b18"] = b18
    return b21
def fonk7(b5, b6, b12, b13):
    b22 = get_games_info_by_team_and_season(b2, b5, b6, b12, b13)
    return b22
if b23 = = '__main__':
    b1.run()
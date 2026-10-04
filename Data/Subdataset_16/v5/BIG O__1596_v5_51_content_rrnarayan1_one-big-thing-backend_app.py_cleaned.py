import firebase_admin
from firebase_admin import firestore
import flask
from flask import request, jsonify, abort
import pandas as pd
from flask_cors import CORS
import numpy as np
from Teams import get_team_by_id
from Games import get_game, get_opp_game, get_games_stats, get_games_info_by_team_and_season
from Score import _get_scores, _get_default_data
b1 = flask.Flask(b22)
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
b4 = [
    'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
    'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS'
]
@b1.route('/')
def fonk1():
    return "Hello World"
@b1.route('/b12')
def fonk2():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b7 = request.args.get('gameId')
    if not (b5 and b6 and b7):
        abort(400, b8 = "Missing required parameters: seasonId, teamId, gameId")
    b9 = get_game(b2, b5, b6, b7)
    if not b9:
        abort(404, b8 = "Game not found")
    return jsonify(b9)
@b1.route('/score')
def fonk3():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b7 = request.args.get('gameId')
    b10 = request.args.get('b10')
    b11 = request.args.get('b11')
    if not (b5 and b6 and b7):
        abort(400, b8 = "Missing required parameters: seasonId, teamId, gameId")
    b12 = get_game(b2, b5, b6, b7)
    b13 = get_opp_game(b2, b5, b6, b7)
    if not b12:
        abort(404, b8 = "Game not found")
    b14 = get_team_by_id(b2, b12["TEAM_ID"])
    b15 = get_team_by_id(b2, b13["TEAM_ID"])
    if not (b14 and b15):
        abort(404, b8 = "Team or Opponent b14 not found")
    if not b10:
        b16 = int(b12["SEASON_ID"])
        b10, b11 = _get_default_data(b16, b12)
    if b11 = = "before" and b12["SEASON_ID"] != b10:
        abort(422, b8 = "Invalid b11 for the given season ID")
    b17 = get_games_stats(b2, b10, b11, b6, b12)
    if not b17:
        abort(404, b8 = "No b12 stats found")
    b18 = _get_scores(b17, b12)
    b18["b14"] = b14
    b18["b15"] = b15
    return jsonify(b18)
@b1.route('/games')
def fonk4():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b19 = request.args.get('withOBT')
    b20 = request.args.get('withSummary')
    if not (b5 and b6):
        abort(400, b8 = "Missing required parameters: seasonId, teamId")
    b21 = get_games_info_by_team_and_season(b2, b5, b6, b19, b20)
    return jsonify(b21)
if b22 = = '__main__':
    b1.run(b23 = True)
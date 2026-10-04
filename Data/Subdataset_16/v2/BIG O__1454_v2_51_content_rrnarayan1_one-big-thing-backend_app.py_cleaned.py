import firebase_admin
from firebase_admin import firestore
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from Teams import get_team_by_id
from Games import get_game, get_opp_game, get_games_stats, get_games_info_by_team_and_season
from Score import _get_scores, _get_default_data
b1 = Flask(b21)
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
    'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA',
    'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS'
]
@b1.route('/')
def fonk1():
    return "Hello World"
@b1.route('/game')
def fonk2():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b7 = request.args.get('gameId')
    if not b5 or not b6 or not b7:
        return abort(400, b8 = "Missing required parameters.")
    b9 = get_game(b2, b5, b6, b7)
    if not b9:
        return abort(404, b8 = "Game not found.")
    return jsonify(b9)
@b1.route('/score')
def fonk3():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b7 = request.args.get('gameId')
    b10 = request.args.get('b10')
    b11 = request.args.get('b11')
    if not b5 or not b6 or not b7:
        return abort(400, b8 = "Missing required parameters.")
    b9 = get_game(b2, b5, b6, b7)
    b12 = get_opp_game(b2, b5, b6, b7)
    if not b9 or not b12:
        return abort(404, b8 = "Game b10 not found.")
    b13 = get_team_by_id(b2, b9["TEAM_ID"])
    b14 = get_team_by_id(b2, b12["TEAM_ID"])
    if not b13 or not b14:
        return abort(404, b8 = "Team b10 not found.")
    if not b10:
        b15 = int(b9["SEASON_ID"])
        b10, b11 = _get_default_data(b15, b9)
    if b11 = = "before" and b9["SEASON_ID"] != b10:
        return abort(422, b8 = "Invalid b10 b11.")
    b16 = get_games_stats(b2, b10, b11, b6, b9)
    if not b16:
        return abort(404, b8 = "Game stats not found.")
    b17 = _get_scores(b16, b9)
    b17["b13"] = b13
    b17["b14"] = b14
    return jsonify(b17)
@b1.route('/games')
def fonk4():
    b5 = request.args.get('seasonId')
    b6 = request.args.get('teamId')
    b18 = request.args.get('withOBT')
    b19 = request.args.get('withSummary')
    if not b5 or not b6:
        return abort(400, b8 = "Missing required parameters.")
    b20 = get_games_info_by_team_and_season(b2, b5, b6, b18, b19)
    return jsonify(b20)
if b21 = = "__main__":
    b1.run(b22 = True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import firestore
from Teams import get_team_by_id
from Games import get_game, get_opp_game, get_games_stats, get_games_info_by_team_and_season
from Score import _get_scores, _get_default_data
app = Flask(__name__)
CORS(app)
firebase_admin.initialize_app()
db = firestore.client()
seasons = {
    "22016": "16-17Reg",
    "42016": "16-17Playoffs",
    "22017": "17-18Reg",
    "42017": "17-18Playoffs",
    "22018": "18-19Reg"
}
stat_categories = ['FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A',
                   'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB',
                   'AST', 'STL', 'BLK', 'TOV', 'PTS']
@app.route('/')
def hello():
    return "Hello World"
@app.route('/game')
def game():
    season_id = request.args.get('seasonId')
    team_id = request.args.get('teamId')
    game_id = request.args.get('gameId')
    if not all([season_id, team_id, game_id]):
        return flask.abort(400)
    game_data = get_game(db, season_id, team_id, game_id)
    if not game_data:
        return flask.abort(404)
    return jsonify(game_data)
@app.route('/score')
def score():
    season_id = request.args.get('seasonId')
    team_id = request.args.get('teamId')
    game_id = request.args.get('gameId')
    data = request.args.get('data')
    portion = request.args.get('portion')
    if not all([season_id, team_id, game_id]):
        return flask.abort(400)
    game_data = get_game(db, season_id, team_id, game_id)
    opp_game_data = get_opp_game(db, season_id, team_id, game_id)
    if not game_data:
        return flask.abort(404)
    team_data = get_team_by_id(db, game_data[u"TEAM_ID"])
    opp_team_data = get_team_by_id(db, opp_game_data[u"TEAM_ID"])
    if not all([team_data, opp_team_data]):
        return flask.abort(404)
    if not data:
        data_season_id = int(game_data[u"SEASON_ID"])
        data, portion = _get_default_data(data_season_id, game_data)
    if portion == "before" and game_data[u"SEASON_ID"] != data:
        return flask.abort(422)
    list_data_games = get_games_stats(db, data, portion, team_id, game_data)
    if not list_data_games:
        return flask.abort(404)
    response = _get_scores(list_data_games, game_data)
    response["team"] = team_data
    response["opp_team"] = opp_team_data
    return jsonify(response)
@app.route('/games')
def games():
    season_id = request.args.get('seasonId')
    team_id = request.args.get('teamId')
    with_obt = request.args.get('withOBT')
    with_summary = request.args.get('withSummary')
    if not all([season_id, team_id]):
        return flask.abort(400)
    games_info = get_games_info_by_team_and_season(db, season_id, team_id, with_obt, with_summary)
    return jsonify(games_info)
if __name__ == '__main__':
    app.run(debug=True)

from datetime import datetime
import pymysql
import pyfootball
from difflib import SequenceMatcher
def find_closest_match(s, options):
    max_similarity = -1
    closest_option = ''
    for option in options:
        similarity = SequenceMatcher(None, s, option).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            closest_option = option
    return closest_option
db = pymysql.connect(host='localhost', user='root', passwd='', db='football1', charset='utf8mb4')
cursor = db.cursor()
cursor.execute('set names utf8mb4')
tables_to_drop = ["ft_players", "user", "fantasy_team", "smps", "team_statistics", "players", "club"]
for table in tables_to_drop:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
table_queries = [
    ,
    ,
    ,
    ,
    ,
    ,
]
for query in table_queries:
    cursor.execute(query)
football_api = pyfootball.Football(api_key='9dbfb7b2bc8d43408d6c160f0b30e5bf')
bundesliga_table = football_api.get_league_table(452)
standings = bundesliga_table.standings
for team in standings:
    if team is not None:
        team_info = (team.team_id, team.team_name, 'GER', football_api.get_team(team.team_id).short_name, bundesliga_table.competition_name)
        cursor.execute('INSERT INTO club VALUES (%s, %s, %s, %s, %s)', team_info)
url_list = pastData.start()
player_list = P_Data.start()
injury_list = injuryScrap()
for player_info in player_list:
    club_name = find_closest_match(player_info[3], [team.team_name for team in standings if team is not None])
    club_id = [team.team_id for team in standings if team is not None and team.team_name == club_name][0]
    if player_info[2] == 'G':
        player_info[2] = 'Goalkeeper'
    elif player_info[2] == 'D':
        player_info[2] = 'Defender'
    elif player_info[2] == 'M':
        player_info[2] = 'Midfielder'
    else:
        player_info[2] = 'Forward'
    player_data = (player_info[0], player_info[1], player_info[2], club_id, player_info[1], 0)
    cursor.execute('INSERT INTO players (pid, pname, position, clubid, nation, injury) VALUES (%s, %s, %s, %s, %s, %s)', player_data)
for url_info in url_list:
    query = 'UPDATE players SET url = %s WHERE pname SOUNDS LIKE %s OR pname LIKE %s'
    cursor.execute(query, (url_info[1], url_info[0], '%' + url_info[0] + '%'))
db.commit()
db.close()
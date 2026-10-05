from difflib import SequenceMatcher
import pymysql
import pyfootball
import pastData
import P_Data
from injury import injuryScrap
def find_most_similar_string(s, string_list):
    max_similarity = -1
    most_similar_string = ''
    for string in string_list:
        similarity = SequenceMatcher(None, s, string).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_string = string
    return most_similar_string
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='',
                     db='football1',
                     charset='utf8mb4')
cursor = db.cursor()
cursor.execute('set names utf8mb4')
existing_tables = ["ft_players", "user", "fantasy_team", "smps", "team_statistics", "players", "club"]
for table in existing_tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
tables_to_create = [
    ,
    ,
    ,
    ,
    ,
    ,
]
for table_create_query in tables_to_create:
    cursor.execute(table_create_query)
football_api_key = 'YOUR_API_KEY'
football_api = pyfootball.Football(api_key=football_api_key)
league_table = football_api.get_league_table(452)
standings = league_table.standings
for standing in standings:
    if standing is not None:
        club_data_query = 'INSERT INTO club VALUES (%d, "%s", "GER", "%s", "%s")' % (
            standing.team_id, standing.team_name, football_api.get_team(standing.team_id).short_name, league_table.competition_name)
        cursor.execute(club_data_query)
team_ids = [standing.team_id for standing in standings if standing is not None]
team_names = [standing.team_name for standing in standings if standing is not None]
url_list = pastData.start()
player_list = P_Data.start()
injury_list = injuryScrap()
player_id = 1
for player_data in player_list:
    club_id = team_ids[team_names.index(find_most_similar_string(player_data[3], team_names))]
    position_mapping = {'G': 'Goalkeeper', 'D': 'Defender', 'M': 'Midfielder', 'F': 'Forward'}
    position = position_mapping.get(player_data[2], 'Unknown')
    injury_status = 0
    for injury_data in injury_list:
        if player_data[0] in injury_data[1]:
            if injury_data[0] == 'red':
                injury_status = 2
            elif injury_data[0] == 'yellow1':
                injury_status = 1
    player_insert_query = 'INSERT INTO players (pid, pname, position, clubid, nation, injury) VALUES ' \
                          '(%d, "%s", "%s", %d, "%s", %d)' % (
                              player_id, player_data[0], position, club_id, player_data[1], injury_status)
    cursor.execute(player_insert_query)
    player_id += 1
for url_data in url_list:
    update_url_query = 'UPDATE players SET url = %s WHERE pname SOUNDS LIKE %s OR pname LIKE %s'
    cursor.execute(update_url_query, (url_data[1], url_data[0], '%' + url_data[0] + '%'))
db.commit()
db.close()
from difflib import SequenceMatcher
import pymysql
import pyfootball
import pastData
import P_Data
from injury import injuryScrap
def fonk1(s, string_list):
    a1 = -1
    b1 = ''
    for string in string_list:
        b2 = SequenceMatcher(None, s, string).ratio()
        if b2 > a1:
            a1 = b2
            b1 = string
    return b1
b3 = pymysql.connect(host='localhost',
                     b4 = 'root',
                     b5 = '',
                     b3 = 'football1',
                     b6 = 'utf8mb4')
b7 = b3.b7()
b7.execute('set names utf8mb4')
b8 = ["ft_players", "b4", "fantasy_team", "smps", "team_statistics", "players", "club"]
for table in b8:
    b7.execute(f"DROP TABLE IF EXISTS {table}")
b9 = [
    ,
    ,
    ,
    ,
    ,
    ,
]
for table_create_query in b9:
    b7.execute(table_create_query)
b10 = 'YOUR_API_KEY'
b11 = pyfootball.Football(api_key=b10)
b12 = b11.get_league_table(452)
b13 = b12.b13
for standing in b13:
    if standing is not None:
        b14 = 'INSERT INTO club VALUES (%d, "%s", "GER", "%s", "%s")' % (
            standing.team_id, standing.team_name, b11.get_team(standing.team_id).short_name, b12.competition_name)
        b7.execute(b14)
b15 = [standing.team_id for standing in b13 if standing is not None]
b16 = [standing.team_name for standing in b13 if standing is not None]
b17 = pastData.start()
b18 = P_Data.start()
b19 = injuryScrap()
a2 = 1
for player_data in b18:
    b20 = b15[b16.index(fonk1(player_data[3], b16))]
    b21 = {'G': 'Goalkeeper', 'D': 'Defender', 'M': 'Midfielder', 'F': 'Forward'}
    b22 = b21.get(player_data[2], 'Unknown')
    a3 = 0
    for injury_data in b19:
        if player_data[0] in injury_data[1]:
            if injury_data[0] == 'red':
                a3 = 2
            elif injury_data[0] == 'yellow1':
                a3 = 1
    b23 = 'INSERT INTO players (pid, pname, b22, clubid, nation, injury) VALUES ' \
                          '(%d, "%s", "%s", %d, "%s", %d)' % (
                              a2, player_data[0], b22, b20, player_data[1], a3)
    b7.execute(b23)
    a2 += 1
for url_data in b17:
    b24 = 'UPDATE players SET url = %s WHERE pname SOUNDS LIKE %s OR pname LIKE %s'
    b7.execute(b24, (url_data[1], url_data[0], '%' + url_data[0] + '%'))
b3.commit()
b3.close()
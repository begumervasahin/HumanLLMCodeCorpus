
from datetime import datetime
import pymysql
import pyfootball
from difflib import SequenceMatcher
def fonk1(s, options):
    a1 = -1
    b1 = ''
    for option in options:
        b2 = SequenceMatcher(None, s, option).ratio()
        if b2 > a1:
            a1 = b2
            b1 = option
    return b1
b3 = pymysql.connect(host='localhost', user='root', passwd='', b3='football1', charset='utf8mb4')
b4 = b3.b4()
b4.execute('set names utf8mb4')
b5 = ["ft_players", "user", "fantasy_team", "smps", "team_statistics", "players", "club"]
for table in b5:
    b4.execute(f"DROP TABLE IF EXISTS {table}")
b6 = [
    ,
    ,
    ,
    ,
    ,
    ,
]
for b17 in b6:
    b4.execute(b17)
b7 = pyfootball.Football(api_key='9dbfb7b2bc8d43408d6c160f0b30e5bf')
b8 = b7.get_league_table(452)
b9 = b8.b9
for team in b9:
    if team is not None:
        b10 = (team.team_id, team.team_name, 'GER', b7.get_team(team.team_id).short_name, b8.competition_name)
        b4.execute('INSERT INTO club VALUES (%s, %s, %s, %s, %s)', b10)
b11 = pastData.start()
b12 = P_Data.start()
b13 = injuryScrap()
for player_info in b12:
    b14 = fonk1(player_info[3], [team.team_name for team in b9 if team is not None])
    b15 = [team.team_id for team in b9 if team is not None and team.team_name == b14][0]
    if player_info[2] == 'G':
        player_info[2] = 'Goalkeeper'
    elif player_info[2] == 'D':
        player_info[2] = 'Defender'
    elif player_info[2] == 'M':
        player_info[2] = 'Midfielder'
    else:
        player_info[2] = 'Forward'
    b16 = (player_info[0], player_info[1], player_info[2], b15, player_info[1], 0)
    b4.execute('INSERT INTO players (pid, pname, position, clubid, nation, injury) VALUES (%s, %s, %s, %s, %s, %s)', b16)
for url_info in b11:
    b17 = 'UPDATE players SET url = %s WHERE pname SOUNDS LIKE %s OR pname LIKE %s'
    b4.execute(b17, (url_info[1], url_info[0], '%' + url_info[0] + '%'))
b3.commit()
b3.close()
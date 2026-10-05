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
def fonk2(b15):
    b3 = ["ft_players", "b12", "fantasy_team", "smps", "team_statistics", "players", "club"]
    for table in b3:
        b15.execute(f"DROP TABLE IF EXISTS {table}")
def fonk3(b15):
    b4 = [
        ,
        ,
        ,
        ,
        ,
        ,
    ]
    for table_create_query in b4:
        b15.execute(table_create_query)
def fonk4(b15, b19, b17):
    for standing in b19:
        if standing is not None:
            b5 = 'INSERT INTO club VALUES (%d, "%s", "GER", "%s", "%s")' % (
                standing.team_id, standing.team_name, b17.get_team(standing.team_id).short_name, b18.competition_name)
            b15.execute(b5)
def fonk5(b15, b23, b20, b21, b24):
    a2 = 1
    for player_data in b23:
        b6 = b20[b21.index(fonk1(player_data[3], b21))]
        b7 = {'G': 'Goalkeeper', 'D': 'Defender', 'M': 'Midfielder', 'F': 'Forward'}
        b8 = b7.get(player_data[2], 'Unknown')
        a3 = 0
        for injury_data in b24:
            if player_data[0] in injury_data[1]:
                if injury_data[0] == 'red':
                    a3 = 2
                elif injury_data[0] == 'yellow1':
                    a3 = 1
        b9 = 'INSERT INTO players (pid, pname, b8, clubid, nation, injury) VALUES ' \
                              '(%d, "%s", "%s", %d, "%s", %d)' % (
                                  a2, player_data[0], b8, b6, player_data[1], a3)
        b15.execute(b9)
        a2 += 1
def fonk6(b15, b22):
    for url_data in b22:
        b10 = 'UPDATE players SET url = %s WHERE pname SOUNDS LIKE %s OR pname LIKE %s'
        b15.execute(b10, (url_data[1], url_data[0], '%' + url_data[0] + '%'))
b11 = pymysql.connect(host='localhost',
                     b12 = 'root',
                     b13 = '',
                     b11 = 'football1',
                     b14 = 'utf8mb4')
b15 = b11.b15()
b15.execute('set names utf8mb4')
fonk2(b15)
fonk3(b15)
b16 = 'YOUR_API_KEY'
b17 = pyfootball.Football(api_key=b16)
b18 = b17.get_league_table(452)
b19 = b18.b19
fonk4(b15, b19, b17)
b20 = [standing.team_id for standing in b19 if standing is not None]
b21 = [standing.team_name for standing in b19 if standing is not None]
b22 = pastData.start()
b23 = P_Data.start()
b24 = injuryScrap()
fonk5(b15, b23, b20, b21, b24)
fonk6(b15, b22)
b11.commit()
b11.close()
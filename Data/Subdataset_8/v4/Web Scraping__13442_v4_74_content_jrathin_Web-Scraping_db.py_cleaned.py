
from datetime import datetime
import pymysql
import pyfootball
from difflib import SequenceMatcher
def compare(s, l):
    max_v = -1
    element = ''
    for i in l:
        if SequenceMatcher(None, s, i).ratio() > max_v:
            max_v = SequenceMatcher(None, s, i).ratio()
            element = i
    return element
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='',
                     db='football1',
                     charset='utf8mb4')
cursor = db.cursor()
cursor.execute('set names utf8mb4')
cursor.execute("drop table if exists ft_players")
cursor.execute("drop table if exists user")
cursor.execute("drop table if exists fantasy_team")
cursor.execute("drop table if exists smps")
cursor.execute("drop table if exists team_statistics")
cursor.execute("drop table if exists players")
cursor.execute("drop table if exists club")
com1 =
com2 =
com3 =
com4 =
com5 =
com6 =
com7 =
cursor.execute(com1)
cursor.execute(com2)
cursor.execute(com3)
cursor.execute(com4)
cursor.execute(com5)
cursor.execute(com6)
cursor.execute(com7)
f = pyfootball.Football(api_key='9dbfb7b2bc8d43408d6c160f0b30e5bf')
lt = f.get_league_table(452)
st = lt.standings
for i in st:
    if i is not None:
        cursor.execute('insert into club values("%d","%s","%s","%s","%s")' % (i.team_id, i.team_name, 'GER', f.get_team(i.team_id).short_name, lt.competition_name))
team_id = []
team_name = []
for i in st:
    if i is not None:
        team_id.append(i.team_id)
        team_name.append(i.team_name)
url_list = pastData.start()
p_list = P_Data.start()
i_list = injuryScrap()
for i in range(len(p_list)):
    p_list[i][3] = team_id[team_name.index(compare(p_list[i][3], team_name))]
    if p_list[i][2] == 'G':
        p_list[i][2] = 'Goalkeeper'
    elif p_list[i][2] == 'D':
        p_list[i][2] = 'Defender'
    elif p_list[i][2] == 'M':
        p_list[i][2] = 'Midfielder'
    else:
        p_list[i][2] = 'Forward'
var = 1
for i in range(len(p_list)):
    injury = 0
    for j in range(len(i_list)):
        if p_list[i][0] in i_list[j][1]:
            if i_list[j][0] == 'red':
                injury = 2
            elif i_list[j][0] == 'yellow1':
                injury = 1
    print(var, p_list[i][0], p_list[i][2], p_list[i][3], p_list[i][1], injury)
    cursor.execute('insert into players (pid,pname,position,clubid,nation,injury) values ("%d","%s","%s","%d","%s","%d")' % (var, p_list[i][0], p_list[i][2], p_list[i][3], p_list[i][1], injury))
    var = var + 1
for i in range(len(url_list)):
    query = 'update players set url = %s where pname sounds like %s or pname like %s'
    cursor.execute(query, (url_list[i][1], url_list[i][0], '%' + url_list[i][0] + '%'))
db.commit()
db.close()
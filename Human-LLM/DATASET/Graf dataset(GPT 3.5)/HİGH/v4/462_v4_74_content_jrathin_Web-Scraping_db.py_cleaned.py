
from datetime import datetime
import pymysql
import pyfootball
from difflib import SequenceMatcher
def fonk1(s, l):
    a1 = -1
    b1 = ''
    for i in l:
        if SequenceMatcher(None, s, i).ratio() > a1:
            a1 = SequenceMatcher(None, s, i).ratio()
            b1 = i
    return b1
b2 = pymysql.connect(host='localhost',
                     b3 = 'root',
                     b4 = '',
                     b2 = 'football1',
                     b5 = 'utf8mb4')
b6 = b2.b6()
b6.execute('set names utf8mb4')
b6.execute("drop table if exists ft_players")
b6.execute("drop table if exists b3")
b6.execute("drop table if exists fantasy_team")
b6.execute("drop table if exists smps")
b6.execute("drop table if exists team_statistics")
b6.execute("drop table if exists players")
b6.execute("drop table if exists club")
b7 = com2 =
b8 = com4 =
b9 = com6 =
b10 = b6.execute(b7)
b6.execute(com2)
b6.execute(b8)
b6.execute(com4)
b6.execute(b9)
b6.execute(com6)
b6.execute(b10)
b11 = pyfootball.Football(api_key='9dbfb7b2bc8d43408d6c160f0b30e5bf')
b12 = b11.get_league_table(452)
b13 = b12.standings
for i in b13:
    if i is not None:
        b6.execute('insert into club values("%d","%s","%s","%s","%s")' % (i.b14, i.b15, 'GER', b11.get_team(i.b14).short_name, b12.competition_name))
b14 = []
b15 = []
for i in b13:
    if i is not None:
        b14.append(i.b14)
        b15.append(i.b15)
b16 = pastData.start()
b17 = P_Data.start()
b18 = injuryScrap()
for i in range(len(b17)):
    b17[i][3] = b14[b15.index(fonk1(b17[i][3], b15))]
    if b17[i][2] == 'G':
        b17[i][2] = 'Goalkeeper'
    elif b17[i][2] == 'D':
        b17[i][2] = 'Defender'
    elif b17[i][2] == 'M':
        b17[i][2] = 'Midfielder'
    else:
        b17[i][2] = 'Forward'
a2 = 1
for i in range(len(b17)):
    a3 = 0
    for j in range(len(b18)):
        if b17[i][0] in b18[j][1]:
            if b18[j][0] == 'red':
                a3 = 2
            elif b18[j][0] == 'yellow1':
                a3 = 1
    print(a2, b17[i][0], b17[i][2], b17[i][3], b17[i][1], a3)
    b6.execute('insert into players (pid,pname,position,clubid,nation,a3) values ("%d","%s","%s","%d","%s","%d")' % (a2, b17[i][0], b17[i][2], b17[i][3], b17[i][1], a3))
    a2 = a2 + 1
for i in range(len(b16)):
    b19 = 'update players set url = %s where pname sounds like %s or pname like %s'
    b6.execute(b19, (b16[i][1], b16[i][0], '%' + b16[i][0] + '%'))
b2.commit()
b2.close()
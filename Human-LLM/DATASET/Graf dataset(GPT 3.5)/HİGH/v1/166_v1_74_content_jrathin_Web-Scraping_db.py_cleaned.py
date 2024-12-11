from difflib import SequenceMatcher
import pymysql
import pyfootball
import pastData
import P_Data
from a3 import injuryScrap
def fonk1(s, l):
    a1 = -1
    b1 = ''
    for i in l:
        b2 = SequenceMatcher(None, s, i).b2()
        if b2 > a1:
            a1 = b2
            b1 = i
    return b1
b3 = pymysql.connect(host='localhost',
                     b4 = 'root',
                     b5 = '',
                     b3 = 'football1',
                     b6 = 'utf8mb4')
b7 = b3.b7()
b7.execute('set names utf8mb4')
b7.execute("drop table if exists ft_players")
b7.execute("drop table if exists b4")
b7.execute("drop table if exists fantasy_team")
b7.execute("drop table if exists smps")
b7.execute("drop table if exists team_statistics")
b7.execute("drop table if exists players")
b7.execute("drop table if exists club")
b8 = com2 =
b9 = com4 =
b10 = com6 =
b11 = b7.execute(b8)
b7.execute(com2)
b7.execute(b9)
b7.execute(com4)
b7.execute(b10)
b7.execute(com6)
b7.execute(b11)
b12 = pyfootball.Football(api_key='YOUR_API_KEY')
b13 = b12.get_league_table(452)
b14 = b13.standings
for i in b14:
    if i is not None:
        b7.execute('insert into club values("%d","%s","%s","%s","%s")' % (
            i.b15, i.b16, 'GER', b12.get_team(i.b15).short_name, b13.competition_name))
b15 = [i.b15 for i in b14 if i is not None]
b16 = [i.b16 for i in b14 if i is not None]
b17 = pastData.start()
b18 = P_Data.start()
b19 = injuryScrap()
a2 = 1
for i in range(len(b18)):
    b18[i][3] = b15[b16.index(fonk1(b18[i][3], b16))]
    if b18[i][2] == 'G':
        b18[i][2] = 'Goalkeeper'
    elif b18[i][2] == 'D':
        b18[i][2] = 'Defender'
    elif b18[i][2] == 'M':
        b18[i][2] = 'Midfielder'
    else:
        b18[i][2] = 'Forward'
    a3 = 0
    for j in range(len(b19)):
        if b18[i][0] in b19[j][1]:
            if b19[j][0] == 'red':
                a3 = 2
            elif b19[j][0] == 'yellow1':
                a3 = 1
    b7.execute('insert into players (pid,pname,position,clubid,nation,a3) values ("%d","%s","%s","%d","%s","%d")' % (
        a2, b18[i][0], b18[i][2], b18[i][3], b18[i][1], a3))
    a2 += 1
for i in range(len(b17)):
    b20 = 'update players set url = %s where pname sounds like %s or pname like %s'
    b7.execute(b20, (b17[i][1], b17[i][0], '%' + b17[i][0] + '%'))
b3.commit()
b3.close()
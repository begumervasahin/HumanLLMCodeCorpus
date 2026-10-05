from datetime import datetime
from currentData import start
from a3 import injuryScrap
import pastData
import pymysql
import pyfootball
import P_Data
from difflib import SequenceMatcher
def fonk1(s,l):
    a1 = -1
    b1 = ''
    for b14 in l:
        if(SequenceMatcher(None, s, b14).ratio()>a1):
            a1 = SequenceMatcher(None, s, b14).ratio()
            b1 = b14
    return(b1)
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
for b14 in b13:
    if(not b14 = =None):
        b6.execute('insert into club values("%d","%s","%s","%s","%s")'%(b14.b15,b14.b16,'GER',b11.get_team(b14.b15).short_name,b12.competition_name))
b15 = []
b16 = []
for b14 in b13:
    if not b14 = =None:
        b15.append(b14.b15)
        b16.append(b14.b16)
b17 = pastData.start()
b18 = P_Data.start()
b19 = injuryScrap()
for b14 in range(len(b18)):
    b18[b14][3] = b15[b16.index(fonk1(b18[b14][3],b16))]
    if b18[b14][2] == 'G':
        b18[b14][2] = 'Goalkeeper'
    elif b18[b14][2] == 'D':
        b18[b14][2] = 'Defender'
    elif b18[b14][2] == 'M':
        b18[b14][2] = 'Midfielder'
    else:
        b18[b14][2] = 'Forward'
a2 = 1
for b14 in range(len(b18)):
    a3 = 0
    for j in range(len(b19)):
        if b18[b14][0] in b19[j][1]:
            if b19[j][0] == 'red':
                a3 = 2
            elif b19[j][0] == 'yellow1':
                a3 = 1
    print(a2,b18[b14][0],b18[b14][2],b18[b14][3],b18[b14][1],a3)
    b6.execute('insert into players (pid,pname,position,clubid,nation,a3) values ("%d","%s","%s","%d","%s","%d")'%(a2,b18[b14][0],b18[b14][2],b18[b14][3],b18[b14][1],a3))
    a2 = a2+1
for b14 in range(len(b17)):
    b20 = 'update players set url = %s where pname sounds like %s or pname like %s'
    b6.execute(b20,(b17[b14][1],b17[b14][0],'%'+b17[b14][0]+'%',))
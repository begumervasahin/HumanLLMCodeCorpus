b1 = 's'
import mysql.connector
import numpy as np
import datetime as d
import copy
import sys
b2 = mysql.connector.connect(user='root', password='',
                              b3 = '127.0.0.1',
                             b4 = 'thesis')
b5 = b2.cursor(buffered= True)
def fonk1(b24,b25) :
    a1 = 0
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    b14 = []
    b15 = []
    b16 = []
    b17 = []
    b18 = []
    b19 = []
    for row in b24 :
        if row[1] == 'Fri' :
            b6.append(row)
        elif row[1] == "Sat" :
            b7.append(row)
        elif row[1] == "Sun" :
            b8.append(row)
        elif row[1] == "Mon" :
            b9.append(row)
        elif row[1] == "Tue" :
            b10.append(row)
        elif row[1] == "Wed" :
            b11.append(row)
        elif row[1] == "Thu" :
            b12.append(row)
    for row in b25 :
        if row[1] == 'Fri' :
            b13.append(row)
        elif row[1] == "Sat" :
            b14.append(row)
        elif row[1] == "Sun" :
            b15.append(row)
        elif row[1] == "Mon" :
            b16.append(row)
        elif row[1] == "Tue" :
            b17.append(row)
        elif row[1] == "Wed" :
            b18.append(row)
        elif row[1] == "Thu" :
            b19.append(row)
    if len(b6)<len(b13) :
        a1 = a1 + cal_sim(b6,b13)
    else :
        a1 = a1 + cal_sim(b13,b6)
    if len(b7)<len(b14) :
        a1 = a1 + cal_sim(b7,b14)
    else :
        a1 = a1 + cal_sim(b14,b7)
    if len(b8)<len(b15) :
        a1 = a1 + cal_sim(b8,b15)
    else :
        a1 = a1 + cal_sim(b15,b8)
    if len(b9)<len(b16) :
        a1 = a1 + cal_sim(b9,b16)
    else :
        a1 = a1 + cal_sim(b16,b9)
    if len(b10)<len(b17) :
        a1 = a1 + cal_sim(b10,b17)
    else :
        a1 = a1 + cal_sim(b17,b10)
    if len(b11)<len(b18) :
        a1 = a1 + cal_sim(b11,b18)
    else :
        a1 = a1 + cal_sim(b18,b11)
    if len(b12)<len(b19) :
        a1 = a1 + cal_sim(b12,b19)
    else :
        a1 = a1 + cal_sim(b19,b12)
    print "the a1 is ",a1
def cal_sim (b24,b25) :
    a1 = 0
    while len(b24)>0 and len(b25)>0 :
            if b24[len(b24)-1][2] == b25[len(b25)-1][2] and b24[len(b24)-1][0] == b25[len(b25)-1][0]:
                a1 +=1
                b24.pop()
                b25.pop()
            elif b24[len(b24)-1][2] > b25[len(b25)-1][2] :
                b24.pop()
            elif b24[len(b24)-1][2] < b25[len(b25)-1][2]:
                b25.pop()
            elif b24[len(b24)-1][2] == b25[len(b25)-1][2] :
                a2 = 2
                if b24[len(b24)-2][2] == b25[len(b25)-1][2] :
                    b24.pop()
                elif b24[len(b24)-1][2] == b25[len(b25)-2][2] :
                    b25.pop()
                else :
                    b24.pop()
                    b25.pop()
    return a1
b20 = np.ones((8357,8357))
b20[0][0]
b21 = []
b5.execute("select distinct b26 from fulldata")
b22 = 15;
for a in b5 :
    b21.append(a)
len(b21)
b23 = b21
a3 = 0
a4 = 0
b24 = []
b25 = []
while (a3<len(b21)) :
    for row in  b21[a3] :
       a4 = row;
    b5.execute("select siteid,weekday,timing from fulldata where b26 = " + str(a4) );
    for siteid,weekday,timing in b5 :
        b27 = []
        b27.append(siteid)
        b27.append(weekday)
        b27.append(timing)
        b24.append(b27)
    b28 = a3+1
    while (b28 < len(b21)) :
        for row in b21[b28] :
            a4 = row;
        b25 = []
        b5.execute("select siteid,weekday,timing from fulldata where b26 = " + str(a4) );
        for siteid,weekday,timing in b5 :
            b27 = []
            b27.append(siteid)
            b27.append(weekday)
            b27.append(timing)
            b25.append(b27)
        print b28
        fonk1(b24,b25)
        b28 +=1
    break
b2.close()
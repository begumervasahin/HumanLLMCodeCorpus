b1 = 's'
b1 = 's'
import mysql.connector
import numpy as np
import time
import datetime as d
import copy
import sys
b2 = mysql.connector.connect(user='root', password='',
                              b3 = '127.0.0.1',
                             b4 = 'thesis')
b5 = b2.cursor(buffered= True)
def fonk1(b23,b24) :
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
    for row in b23 :
        if row[1] == '"Fri"' :
            b6.append(row)
        elif row[1] == '"Sat"' :
            b7.append(row)
        elif row[1] == '"Sun"' :
            b8.append(row)
        elif row[1] == '"Mon"' :
            b9.append(row)
        elif row[1] == '"Tue"' :
            b10.append(row)
        elif row[1] == '"Wed"' :
            b11.append(row)
        elif row[1] == '"Thu"' :
            b12.append(row)
    for row in b24 :
        if row[1] == '"Fri"' :
            b13.append(row)
        elif row[1] == '"Sat"' :
            b14.append(row)
        elif row[1] == '"Sun"' :
            b15.append(row)
        elif row[1] == '"Mon"' :
            b16.append(row)
        elif row[1] == '"Tue"' :
            b17.append(row)
        elif row[1] == '"Wed"' :
            b18.append(row)
        elif row[1] == '"Thu"' :
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
def cal_sim (b23,b24) :
    a1 = 0
    while len(b23)>0 and len(b24)>0 :
            if b23[len(b23)-1][2] == b24[len(b24)-1][2] and b23[len(b23)-1][0] == b24[len(b24)-1][0]:
                a1 +=1
                b23.pop()
                b24.pop()
            elif b23[len(b23)-1][2] > b24[len(b24)-1][2] :
                b23.pop()
            elif b23[len(b23)-1][2] < b24[len(b24)-1][2]:
                b24.pop()
            elif b23[len(b23)-1][2] == b24[len(b24)-1][2] :
                a2 = 2
                if b23[len(b23)-2][2] == b24[len(b24)-1][2] :
                    b23.pop()
                elif b23[len(b23)-1][2] == b24[len(b24)-2][2] :
                    b24.pop()
                else :
                    b23.pop()
                    b24.pop()
    return a1
b20 = np.ones((8357,8357))
b21 = []
b5.execute("select distinct a4 from fulldata")
for a in b5 :
    b21.append(a)
b22 = open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv');
a3 = 0
b23 = []
b24 = []
a4 = 0
a5 = 0
b25 = []
for line in iter(b22):
    if(a3 = =0):
        a3 = a3+1
    else :
        b26 = line.split(",")
        if a4 = = int(b26[0]) :
            b25 = []
            b25.append(b26[1])
            b25.append(str(b26[2]))
            b25.append(b26[3])
            b24.append(b25)
        else :
            a4 = int(b26[0])
            if len(b24)>0 :
                b23.append(b24)
            b24 = []
            b25 = []
            b25.append(b26[1])
            b25.append(str(b26[2]))
            b25.append(b26[3])
            b24.append(b25)
b23.append(b24)
print len(b23)
a6 = 0
while a6<8356 :
     print a6
     b27 = []
     b27 = copy.deepcopy(b23[a6])
     a2 = a6+1
     while(a2<8357) :
         b28 = []
         b28 = copy.deepcopy(b23[a2])
         fonk1(b27,b28)
         a2 +=1
     a6 = a6+1
'''
b29 = 15;
for a in b5 :
    b21.append(a)
len(b21)
b30 = b21
a7 = 0
a8 = 0
b23 = []
b24 = []
while (a7<len(b21)) :
    for row in  b21[a7] :
       a8 = row;
    b5.execute("select siteid,weekday,timing from fulldata where a4 = " + str(a8) );
    for siteid,weekday,timing in b5 :
        b25 = []
        b25.append(siteid)
        b25.append(weekday)
        b25.append(timing)
        b23.append(b25)
    b31 = a7+1
    while (b31 < len(b21)) :
        for row in b21[b31] :
            a8 = row;
        b24 = []
        b5.execute("select siteid,weekday,timing from fulldata where a4 = " + str(a8) );
        for siteid,weekday,timing in b5 :
            b25 = []
            b25.append(siteid)
            b25.append(weekday)
            b25.append(timing)
            b24.append(b25)
        print b31
        fonk1(b23,b24)
        b31 +=1
    break'''
b2.close()
b1 = 'b28'
import mysql.connector
import numpy as np
import time
import datetime as d
import copy
import sys
def fonk1(b22,b23) :
    a1 = 0
    a2 = 0
    if(len(b22)>len(b23)) :
        a2 = len(b23)
    else :
        a2 = len(b22)
    b2 = []
    b3 = []
    b4 = []
    b5 = []
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
    for row in b22 :
        if row[1] == '"Fri"' :
            b2.append(row)
        elif row[1] == '"Sat"' :
            b3.append(row)
        elif row[1] == '"Sun"' :
            b4.append(row)
        elif row[1] == '"Mon"' :
            b5.append(row)
        elif row[1] == '"Tue"' :
            b6.append(row)
        elif row[1] == '"Wed"' :
            b7.append(row)
        elif row[1] == '"Thu"' :
            b8.append(row)
    for row in b23 :
        if row[1] == '"Fri"' :
            b9.append(row)
        elif row[1] == '"Sat"' :
            b10.append(row)
        elif row[1] == '"Sun"' :
            b11.append(row)
        elif row[1] == '"Mon"' :
            b12.append(row)
        elif row[1] == '"Tue"' :
            b13.append(row)
        elif row[1] == '"Wed"' :
            b14.append(row)
        elif row[1] == '"Thu"' :
            b15.append(row)
    if len(b2)<len(b9) :
        a1 = a1 + fonk4(b2,b9)
    else :
        a1 = a1 + fonk4(b9,b2)
    if len(b3)<len(b10) :
        a1 = a1 + fonk4(b3,b10)
    else :
        a1 = a1 + fonk4(b10,b3)
    if len(b4)<len(b11) :
        a1 = a1 + fonk4(b4,b11)
    else :
        a1 = a1 + fonk4(b11,b4)
    if len(b5)<len(b12) :
        a1 = a1 + fonk4(b5,b12)
    else :
        a1 = a1 + fonk4(b12,b5)
    if len(b6)<len(b13) :
        a1 = a1 + fonk4(b6,b13)
    else :
        a1 = a1 + fonk4(b13,b6)
    if len(b7)<len(b14) :
        a1 = a1 + fonk4(b7,b14)
    else :
        a1 = a1 + fonk4(b14,b7)
    if len(b8)<len(b15) :
        a1 = a1 + fonk4(b8,b15)
    else :
        a1 = a1 + fonk4(b15,b8)
    b16 = float(a1)/a2
    b16 = float(1) - float(b16)
    return b16
'''def cal_sim (b22,b23) :
    a1 = 0
    while len(b22)>0 and len(b23)>0 :
            if b22[len(b22)-1][2] == b23[len(b23)-1][2] and b22[len(b22)-1][0] == b23[len(b23)-1][0]:
                a1 +=1
                b22.pop()
                b23.pop()
            elif b22[len(b22)-1][2] > b23[len(b23)-1][2] :
                b22.pop()
            elif b22[len(b22)-1][2] < b23[len(b23)-1][2]:
                b23.pop()
            elif b22[len(b22)-1][2] == b23[len(b23)-1][2] :
                a3 = 2
                if b22[len(b22)-2][2] == b23[len(b23)-1][2] :
                    b22.pop()
                elif b22[len(b22)-1][2] == b23[len(b23)-2][2] :
                    b23.pop()
                else :
                    b22.pop()
                    b23.pop()
    return a1'''
'''def fonk2(b22,b23) :
    a1 = 0
    b17 = len(b23)-1
    while len(b22)>0 :
        while b17>-1 :
            if b22[len(b22)-1][2] == b23[b17][2] :
                if b22[len(b22)-1][0]== b23[b17][0] :
                    a1 += 1
                b17 -=1
            elif b22[len(b22)-1][2] > b23[b17][2] :
                break
            elif b22[len(b22)-1][2] < b23[b17][2] :
                b17 -=1
        b22.pop()
    return a1'''
def fonk3(b22,b23) :
    a1 = 0
    a4 = 0
    while len(b23)>0 :
        b17 = len(b22)-1
        while b17>-1 :
            if b23[len(b23)-1][2] == b22[b17][2] :
                if b23[len(b23)-1][0]== b22[b17][0] :
                    a1 += 1
            b17 -=1
        b23.pop()
    return a1
'''def fonk4(b22,b23) :
    a1 = 0
    a4 = len(b23)-1
    while len(b22)>0 :
        b17 = a4
        while b17>-1 :
            if b22[len(b22)-1][2] == b23[b17][2] :
                if b22[len(b22)-1][0]== b23[b17][0] :
                    a1 += 1
                a4 = b17
            b17 -=1
        b22.pop()
    return a1'''
b16 = np.zeros((8357,8357))
'''b18 = []
c.execute("select distinct a6 from fulldata")
for a in c :
    b18.append(a)'''
b19 = open('/home/b28/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv');
b20 = open('distance_matrix_full.csv','r+')
b21 = open('distance_matrix_full_withoutid.csv','r+')
a5 = 0
b22 = []
b23 = []
a6 = 0
a7 = 0
b24 = []
b25 = []
for line in iter(b19):
    if(a5 = =0):
        a5 = a5+1
    else :
        b26 = line.split(",")
        if a6 = = int(b26[0]) :
            b24 = []
            b24.append(b26[1])
            b24.append(str(b26[2]))
            b24.append(b26[3])
            b23.append(b24)
        else :
            a6 = int(b26[0])
            if len(b23)>0 :
                b22.append(b23)
            b23 = []
            b24 = []
            b25.append(b26[0])
            b24.append(b26[1])
            b24.append(str(b26[2]))
            b24.append(b26[3])
            b23.append(b24)
b22.append(b23)
print b25[1697]
a4 = 0
for line in iter(b21) :
a8 = 0
while a8<8356 :
     print "a8 = ",a8
     b27 = []
     b27 = copy.deepcopy(b22[a8])
     a3 = a8+1
     b28 = []
     while(a3<8357) :
         b29 = []
         b29 = copy.deepcopy(b22[a3])
         b16[a8][a3] = fonk1(b27,b29)
         b16[a3][a8] = b16[a8][a3]
         a3 +=1
     a5 = 0
     b20.write(str(b25[a8]))
     b20.write(",")
     b20.write(str(b16[a8][a5]))
     b21.write(str(b16[a8][a5]))
     a5 = 1
     while a5< 8357:
         b20.write(",")
         b20.write(str(b16[a8][a5]))
         b21.write(",")
         b21.write(str(b16[a8][a5]))
         a5 +=1
     b20.write("\n")
     b21.write("\n")
     a8 += 1
a5 = 0
b20.write(str(b25[a8]))
b20.write(",")
while a5<8357 :
    b20.write(str(b16[8356][a5]))
    b20.write(",")
    b21.write(str(b16[8356][a5]))
    b21.write(",")
    a5 +=1'''
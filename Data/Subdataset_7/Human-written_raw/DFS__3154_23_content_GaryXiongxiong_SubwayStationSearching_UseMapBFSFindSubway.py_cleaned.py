'''
@Author: Yixiong J
@Date: 2019-10-02 01:04:38
@LastEditors: Yixiong J
@LastEditTime: 2019-10-02 01:07:37
@Description: Use BFS to caculate shortest b7 between two subway station
'''
import os
from Stations import *
from collections import deque
def fonk1(station,b5):
    b1 = deque()
    b2 = {station.getName():None}
    b1 += [station]
    while b1:
        b3 = b1.popleft()
        for subStation in stationMap[b3]:
            if subStation.getName() not in b2.keys():
                if subStation.getName() == b5.getName():
                    b2[subStation.getName()] = b3.getName()
                    return b2,b5.getName()
                else:
                    b1 += [subStation]
                    b2[subStation.getName()] = b3.getName()
    print("NULL")
    return False,b5
b4 = input("è¯·è¾å
¥èµ·ç¹ç«ï¼  ")
b5 = input("è¯·è¾å
¥ç®çå°ï¼  ")
searchedOut,b6 = fonk1(stationStringMap[b4],stationStringMap[b5])
print("-"*10+"è·¯å¾å¦ä¸"+"-"*10)
b7 = [b6]
while searchedOut[b6] is not None:
    b7.append(searchedOut[b6])
    b6 = searchedOut[b6]
b7.reverse()
for each in b7:
    print(each+" ",b8 = "")
print("\n")
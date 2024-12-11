import time
import csv
import json
import os
import random
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
from datetime import datetime
def fonk1(time_str):
    b1 = "%s-%s-%s %s:%s:%s" % (
        time_str[0:4],
        time_str[4:6],
        time_str[6:8],
        time_str[8:10],
        time_str[10:12],
        time_str[12:]
    )
    b2 = datetime.strptime(b1, "%Y-%m-%d %H:%M:%S")
    return time.mktime(b2.timetuple())
def fonk2(all_time):
    b3 = []
    for idx in range(len(all_time) - 1):
        b4 = fonk1(all_time[idx])
        b5 = fonk1(all_time[idx + 1])
        b3.append(abs(b5 - b4))
    b3 = [delta for delta in b3 if delta != 0]
    if not b3:
        b3 = [0]
    return mean(b3)
def fonk3(all_time, deltaT):
    a1 = 1
    b6 = {}
    a2 = 0
    b7 = False
    while a2 < len(all_time):
        b8 = a2 + 1
        if b8 >= len(all_time):
            break
        b4 = all_time[a2]
        b5 = all_time[b8]
        b9 = set()
        while abs(fonk1(b4) - fonk1(b5)) <= deltaT:
            b9.add(b4)
            b9.add(b5)
            a2 += 1
            if all_time[a2] == all_time[-1]:
                b7 = True
            b8 += 1
            if b8 >= len(all_time):
                b6[a1] = list(b9)
                a1 += 1
                a2 = b8
                break
            b4 = all_time[a2]
            b5 = all_time[b8]
        b6[a1] = list(b9)
        a1 += 1
        a2 = b8
    if not b7:
        b6[a1] = [all_time[-1]]
    return b6

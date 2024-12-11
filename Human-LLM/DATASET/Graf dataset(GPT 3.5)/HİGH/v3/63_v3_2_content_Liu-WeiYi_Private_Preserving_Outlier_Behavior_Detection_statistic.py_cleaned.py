import sys
import json
from Process_TianChi_Main import analysis_Time
from utils import *
def fonk1(b12):
    b1 = set()
    b2 = len(b12)
    a1 = 0
    for user_info in b12.values():
        a1 += 1
        b3 = (a1 / b2) * 100
        sys.stdout.write(f'\r>> Processing Users............ {b3:.2f} %')
        sys.stdout.flush()
        b4 = user_info.get("Reach_Time", {})
        for time_info in b4.values():
            b1.update(time_info.keys())
    return b1
def fonk2(b13):
    b5 = sum(len(analysis_Time(user, info)[1]) for user, info in b13.items())
    return b5
def fonk3(b12):
    b2 = len(b12)
    b6 = sum(len(info["Keyword"]) for user_info in b12.values() for info in user_info.get("Reach_Time", {}).values())
    b7 = sum(len(info["Device_IP"]) for user_info in b12.values() for info in user_info.get("Reach_Time", {}).values())
    b8 = b6 / b2
    b9 = b7 / b2
    return b8, b9
def fonk4():
    b10 = []
    with open('all_user_id.txt', 'r+') as f:
        b10 = [line.strip() for line in f.readlines()]
    b11 = sys.argv[1]
    if b11 = = '0':
        print('Analyzing b1 group...')
        with open('b12.json') as f:
            b12 = json.load(f)
        b1 = fonk1(b12)
        print('\nTotal number of b1:', len(b1))
    elif b11 = = '1':
        print('Analyzing time group...')
        with open('b13.json') as f:
            b13 = json.load(f)
        b5 = fonk2(b13)
        print('\nTotal time groups:', b5)
    elif b11 = = '2':
        print('Analyzing features...')
        with open('b12.json') as f:
            b12 = json.load(f)
        b8, b9 = fonk3(b12)
        print('\nAverage number of keywords:', b8)
        print('Average number of IP addresses:', b9)
if b14 = = "__main__":
    fonk4()
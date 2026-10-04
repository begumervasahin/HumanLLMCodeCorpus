import json
import sys
from Process_TianChi_Main import analysis_Time
from utils import *
def fonk1(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]
def fonk2(b12):
    b1 = set()
    b2 = len(b12)
    for count, user in enumerate(b12.keys(), b3 = 1):
        b4 = 100 * count / b2
        sys.stdout.write(f'\r>> Processing Users............ {b4:.2f} %')
        sys.stdout.flush()
        b5 = b12[user]["Reach_Time"]
        for time in b5.keys():
            b1.update(b5[time].keys())
    return len(b1)
def fonk3(b14):
    a1 = 0
    b2 = len(b14)
    for count, user in enumerate(b14.keys(), b3 = 1):
        b4 = 100 * count / b2
        sys.stdout.write(f'\r>> Processing Users............ {b4:.2f} %')
        sys.stdout.flush()
        b6 = b14[user]
        _, b7 = analysis_Time(user, b6)
        a1 += len(b7.keys())
    return a1
def fonk4(b12):
    a2 = 0
    a3 = 0
    b2 = len(b12)
    for count, user in enumerate(b12.keys(), b3 = 1):
        b4 = 100 * count / b2
        sys.stdout.write(f'\r>> Processing Users............ {b4:.2f} %')
        sys.stdout.flush()
        b5 = b12[user]["Reach_Time"]
        for time in b5.keys():
            for user_info in b5[time].values():
                a2 += len(user_info["Keyword"])
                a3 += len(user_info["Device_IP"])
    b8 = a2 / b2
    b9 = a3 / b2
    return a2, b8, a3, b9
def fonk5():
    b10 = fonk1('all_user_id.txt')
    b11 = sys.argv[1]
    if b11 = = '0':
        print('b1 group...')
        with open('b12.json') as f:
            b12 = json.load(f)
        b13 = fonk2(b12)
        print(f'\nNumber of unique b1: {b13}')
    elif b11 = = '1':
        print('time group...')
        with open('user_time_info.json') as f:
            b14 = json.load(f)
        a1 = fonk3(b14)
        print(f'\nTotal time intervals: {a1}')
    elif b11 = = '2':
        print('features...')
        with open('b12.json') as f:
            b12 = json.load(f)
        a2, b8, a3, b9 = fonk4(b12)
        print(f'\nTotal keywords: {a2}')
        print(f'Average keywords per user: {b8}')
        print(f'Total IPs: {a3}')
        print(f'Average IPs per user: {b9}')
if b15 = = "__main__":
    fonk5()
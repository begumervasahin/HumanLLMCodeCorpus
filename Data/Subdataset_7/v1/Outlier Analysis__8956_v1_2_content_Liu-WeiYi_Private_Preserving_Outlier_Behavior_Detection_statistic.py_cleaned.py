import sys
import json
from Process_TianChi_Main import analysis_Time
from utils import *
def fonk1():
    b1 = []
    with open('all_user_id.txt', 'r+') as f:
        b1 = [line.strip() for line in f.readlines()]
    b2 = sys.argv[1]
    if b2 = = '0':
        print('b4 group...')
        with open('b3.json') as f:
            b3 = json.load(f)
            b4 = set()
            a1 = 0
            for user in b3.keys():
                a1 += 1
                b5 = 100 * a1 / len(b3.keys())
                sys.stdout.write('\r>> Processing Users............ %.2f %%' % b5)
                sys.stdout.flush()
                b6 = b3[user]["Reach_Time"]
                for time in b6.keys():
                    b7 = b6[time].keys()
                    for d in b7:
                        b4.add(d)
        b8 = len(b4)
        print('\nTotal number of b4:', b8)
    elif b2 = = '1':
        print('time group...')
        with open('user_time_info.json') as f:
            b9 = json.load(f)
            a2 = 0
            a1 = 0
            for user in b9.keys():
                a1 += 1
                b5 = 100 * a1 / len(b9.keys())
                sys.stdout.write('\r>> Processing Users............ %.2f %%' % b5)
                sys.stdout.flush()
                b10 = b9[user]
                _, b11 = analysis_Time(user, b10)
                a2 += len(b11.keys())
        print('\nTotal time groups:', a2)
    elif b2 = = '2':
        print('features...')
        with open('b3.json') as f:
            b3 = json.load(f)
            a3 = 0
            a4 = 0
            a5 = 0
            a6 = 0
            a1 = 0
            for user in b3.keys():
                a1 += 1
                b5 = 100 * a1 / len(b3.keys())
                sys.stdout.write('\r>> Processing Users............ %.2f %%' % b5)
                sys.stdout.flush()
                b6 = b3[user]["Reach_Time"]
                for time in b6.keys():
                    for user in b6[time].keys():
                        a3 += len(b6[time][user]["Keyword"])
                        a5 += len(b6[time][user]["Device_IP"])
            a4 = a3 / len(b3.keys())
            a6 = a5 / len(b3.keys())
        print('\nAverage number of keywords:', a4)
        print('Average number of IP addresses:', a6)
if b12 = = "__main__":
    fonk1()
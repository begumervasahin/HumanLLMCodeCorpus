import json
import sys
from Process_TianChi_Main import analysis_Time
from utils import *
b1 = []
with open('all_user_id.txt', 'r') as f:
    b1 = [line.strip() for line in f.readlines()]
def fonk1(b2):
    if b2 = = '0':
        print('Processing b4 group...')
        with open('b3.json') as f:
            b3 = json.load(f)
            b4 = set()
            a1 = 0
            for user in b3:
                a1 += 1
                b5 = 100 * a1 / len(b3)
                print(f'\r>> Processing Users... {b5:.2f}%', b6 = '', flush=True)
                b7 = b3[user]["Reach_Time"]
                for time in b7:
                    b8 = b7[time].keys()
                    b4.update(b8)
        b9 = len(b4)
        print('\nTotal number of b4:', b9)
    elif b2 = = '1':
        print('Processing time group...')
        with open('user_time_info.json') as f:
            b10 = json.load(f)
            a2 = 0
            a1 = 0
            for user in b10:
                a1 += 1
                b5 = 100 * a1 / len(b10)
                print(f'\r>> Processing Users... {b5:.2f}%', b6 = '', flush=True)
                b11 = b10[user]
                _, b12 = analysis_Time(user, b11)
                a2 += len(b12)
        print('\nTotal time intervals:', a2)
    elif b2 = = '2':
        print('Processing features...')
        with open('b3.json') as f:
            b3 = json.load(f)
            a3 = 0
            a4 = 0
            a5 = 0
            a6 = 0
            a1 = 0
            for user in b3:
                a1 += 1
                b5 = 100 * a1 / len(b3)
                print(f'\r>> Processing Users... {b5:.2f}%', b6 = '', flush=True)
                b7 = b3[user]["Reach_Time"]
                for time in b7:
                    for user in b7[time]:
                        a3 += len(b7[time][user]["Keyword"])
                        a5 += len(b7[time][user]["Device_IP"])
            a4 = a3 / len(b3)
            a6 = a5 / len(b3)
        print('\nAverage number of keywords per user:', a4)
        print('Average number of IP addresses per user:', a6)
    else:
        print('Invalid b2!')
if b13 = = "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py [b2]")
    else:
        b2 = sys.argv[1]
        fonk1(b2)
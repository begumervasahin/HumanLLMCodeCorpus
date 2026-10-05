import json
import sys
from Process_TianChi_Main import analysis_Time
from utils import *
with open('all_user_id.txt', 'r') as f:
    b1 = [line.strip() for line in f.readlines()]
def fonk1(b13):
    b2 = set()
    b3 = len(b13)
    for count, user_info in enumerate(b13, 1):
        b4 = 100 * count / b3
        print(f'\r>> Processing Users... {b4:.2f}%', b5 = '', flush=True)
        for time_info in user_info["Reach_Time"].values():
            b2.update(time_info.keys())
    print('\nTotal number of b2:', len(b2))
def fonk2(b14):
    b6 = sum(len(analysis_Time(user, info)[1]) for user, info in b14.items())
    print('\nTotal time intervals:', b6)
def fonk3(b13):
    b3 = len(b13)
    b7 = sum(len(info["Keyword"]) for user_info in b13 for time_info in user_info["Reach_Time"].values() for info in time_info.values())
    b8 = sum(len(info["Device_IP"]) for user_info in b13 for time_info in user_info["Reach_Time"].values() for info in time_info.values())
    b9 = b7 / b3
    b10 = b8 / b3
    print('\nAverage number of keywords per user:', b9)
    print('Average number of IP addresses per user:', b10)
if b11 = = "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py [b12]")
    else:
        b12 = sys.argv[1]
        if b12 = = '0':
            print('Processing b2 group...')
            with open('b13.json') as f:
                b13 = json.load(f)
                fonk1(b13)
        elif b12 = = '1':
            print('Processing time group...')
            with open('user_time_info.json') as f:
                b14 = json.load(f)
                fonk2(b14)
        elif b12 = = '2':
            print('Processing features...')
            with open('b13.json') as f:
                b13 = json.load(f)
                fonk3(b13)
        else:
            print('Invalid b12!')
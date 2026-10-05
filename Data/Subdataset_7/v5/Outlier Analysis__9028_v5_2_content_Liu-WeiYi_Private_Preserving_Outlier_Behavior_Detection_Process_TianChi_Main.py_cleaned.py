from __future__ import print_function, division
import sys
import os
import json
import traceback
from datetime import datetime
import time
import networkx as nx
from utils import *
from Abnormal_Scenario_Generation import *
def fonk1(b22, b1 = True):
    b2 = []
    b3 = {}
    b4 = 'b2.txt'
    b5 = 'user_time_info.json'
    if b1:
        b4 = '10_all_user_id.txt'
        b5 = '10_user_time_info.json'
    if os.path.exists(b5) and os.path.exists(b4):
        with open(b4, 'r+') as f:
            b2 = [line.strip() for line in f.readlines()]
        b3 = json.load(open(b5))
        print('--Done loading files:\t{}, {}'.format(b4, b5))
    else:
        b2, b3 = extract_user_time(b22)
    return b2, b3
def fonk2(b2, b22, b1 = True):
    b6 = "b7.json"
    if b1:
        b6 = '10_all_user_info.json'
    if os.path.exists(b6):
        b7 = json.load(open(b6))
        print('--Done Loading Files:\t{}'.format(b6))
    else:
        b7 = extract_user_Devices_info(b2, b22)
    return b7
def fonk3(user, b27):
    try:
        b8 = b27["Reach_Time"]
        b9 = sorted(list(set(sorted(b8))))
        b10 = find_median_delta_T(b9)
    except Exception as exc:
        print('Abnormal User ID: {}'.format(user))
        print(traceback.format_exc())
        print(exc)
    b11 = generate_time_group(b9, b10)
    return b10, b11
def fonk4(b11, b28):
    b12 = {}
    for key in b11.keys():
        b13 = b11[key]
        b14 = extract_devices_behavior_on_time_group(b13, b28)
        b12[key] = b14
    return b12
def fonk5(b31, b32):
    b15 = nx.Graph(b31=b31)
    b16 = list(b32.keys())
    b15.add_nodes_from(b16)
    if len(b16) > 1:
        for d1_idx in range(len(b16)-1):
            for d2_idx in range(d1_idx+1, len(b16)):
                b17 = b16[d1_idx]
                b18 = b16[d2_idx]
                b19 = calculate_devices_weight(b17, b18, b32)
                b15.add_edge(b17, b18, b20 = b19)
    return b15
if b21 = = "__main__":
    b1 = True
    try:
        if sys.argv[1] == '-w':
            b1 = False
    except:
        pass
    b22 = ['ijcai_device_encode_test_sample.csv', 'ijcai_cookie_encode_test_sample.csv']
    if not b1:
        b22 = [
            'ijcai_device_encode_training.csv',
            'ijcai_device_encode_test.csv',
            'ijcai_cookie_encode_training.csv',
            'ijcai_cookie_encode_test.csv'
        ]
    b2, b3 = fonk1(b22, b1)
    b7 = fonk2(b2, b22, b1)
    b23 = '{}-{}'.format(str(datetime.now()).split()[0], str(datetime.now()).split()[1])
    b24 = []
    for user_idx, user in enumerate(b2):
        b25 = time.time()
        b26 = 100*(user_idx+1) / len(b2)
        sys.stdout.write('\r>> Processing Users............ {:.2f} %'.format(b26))
        sys.stdout.flush()
        b27 = b3[user]
        median_t, b11 = fonk3(user, b27)
        if b11 = = {} and median_t == []:
            print('Cannot Parse Current User: {}'.format(user))
            continue
        b28 = b7[user]
        b29 = fonk4(b11, b28)
        b30 = []
        for key in b29.keys():
            b15 = fonk5(
                b31 = '{}_{}'.format(user, key),
                b32 = b29[key]
            )
            b30.append(b15)
        b33 = merged_graph(user, b30)
        b34 = time.time() - b25
        b24.append(b34)
        draw_graph(str(median_t), b23, str(user_idx), user, b33, b35 = True, save_to_disk=True)
    print('\n')
    b36 = min(b24)
    b37 = max(b24)
    b38 = mean(b24)
    b39 = sum(b24)
    print('b36:  {}'.format(b36))
    print('b38:  {}'.format(b38))
    print('b37:  {}'.format(b37))
    print('all_tim:   {}'.format(b39))
    with open('b9', 'w+') as f:
        for i in b24:
            f.write(str(i))
            f.write('\n')
    print('\nall down!!!')
from __future__ import print_function, division
import sys
import pickle
import os
import json
import networkx as nx
import traceback
from datetime import datetime
import time
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
            for line in f.readlines():
                b2.append(line.strip())
        b3 = json.load(open(b5))
        print('--Done loading files:\t%s, %s' % (b4, b5))
    else:
        b2, b3 = extract_user_time(b22)
    return b2, b3
def fonk2(b2, b22, b1 = True):
    b6 = "b7.json"
    if b1:
        b6 = '10_all_user_info.json'
    if os.path.exists(b6):
        b7 = json.load(open(b6))
        print('--Done Loading Files:\t%s' % b6)
    else:
        b7 = extract_user_Devices_info(b2, b22)
    return b7
def fonk3(b27, b28):
    try:
        b8 = b28["Reach_Time"]
        b9 = sorted(list(set(sorted(b8))))
        b10 = find_median_delta_T(b9)
    except Exception as exc:
        print('Abnormal User ID: %s' % b27)
        print(traceback.format_exc())
        print(exc)
    b11 = generate_time_group(b9, b10)
    return b10, b11
def fonk4(b11, b29):
    b12 = {}
    for key in b11.keys():
        b13 = b11[key]
        b14 = extract_devices_behavior_on_time_group(b13, b29)
        b12[key] = b14
    return b12
def fonk5(b32, b33):
    b15 = nx.Graph(b32=b32)
    b16 = list(b33.keys())
    b15.add_nodes_from(b16)
    if len(b16) > 1:
        for d1_idx in range(len(b16)-1):
            for d2_idx in range(d1_idx+1, len(b16)):
                b17 = b16[d1_idx]
                b18 = b16[d2_idx]
                b19 = calculate_devices_weight(b17, b18, b33)
                b15.add_edge(b17, b18, b20 = b19)
    return b15
global IO_Time
a1 = 0
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
    b23 = str(datetime.now()).split()[0] + '-' + str(datetime.now()).split()[1]
    b24 = []
    for user_idx in range(len(b2)):
        b25 = time.time()
        b26 = 100*(user_idx+1)/len(b2)
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % b26)
        sys.stdout.flush()
        b27 = b2[user_idx]
        b28 = b3[b27]
        median_T, b11 = fonk3(b27, b28)
        if b11 = = {} and median_T == []:
            print('Cannot Parse Current User: %s' % b27)
            continue
        b29 = b7[b27]
        b30 = fonk4(b11, b29)
        b31 = []
        for key in b30.keys():
            b15 = fonk5(
                b32 = b27+'_'+str(key),
                b33 = b30[key]
            )
            b31.append(b15)
        b34 = merged_graph(b27, b31)
        b35 = time.time()-b25
        b24.append(b35)
        draw_graph(str(median_T), b23, str(user_idx), b27, b34, b36 = True, save_to_disk=True)
    print('\n')
    b37 = min(b24)
    b38 = max(b24)
    b39 = mean(b24)
    b40 = sum(b24)
    print('b37:  ', b37)
    print('b39:  ', b39)
    print('b38:  ', b38)
    print('all_tim:   ', b40)
    with open('b9', 'w+') as f:
        for i in b24:
            f.write(str(i))
            f.write('\n')
    print('\nall down!!!')
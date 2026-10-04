from __future__ import print_function, division
import sys
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
        with open(b4, 'r') as f:
            b2 = [line.strip() for line in f.readlines()]
        with open(b5, 'r') as f:
            b3 = json.load(f)
        print(f'--Done loading files: {b4}, {b5}')
    else:
        b2, b3 = extract_user_time(b22)
    return b2, b3
def fonk2(b2, b22, b1 = True):
    b6 = "b7.json"
    if b1:
        b6 = '10_all_user_info.json'
    if os.path.exists(b6):
        with open(b6, 'r') as f:
            b7 = json.load(f)
        print(f'--Done Loading Files: {b6}')
    else:
        b7 = extract_user_Devices_info(b2, b22)
    return b7
def fonk3(user, b27):
    try:
        b8 = b27["Reach_Time"]
        b9 = sorted(set(b8))
        b10 = find_median_delta_T(b9)
    except Exception as exc:
        print(f'Abnormal User ID: {user}')
        print(traceback.format_exc())
        print(exc)
        return [], {}
    b11 = generate_time_group(b9, b10)
    return b10, b11
def fonk4(b11, b28):
    b12 = {}
    for key, time_group in b11.items():
        b13 = extract_devices_behavior_on_time_group(time_group, b28)
        b12[key] = b13
    return b12
def fonk5(name, devices_info):
    b14 = nx.Graph(name=name)
    b15 = list(devices_info.keys())
    b14.add_nodes_from(b15)
    if len(b15) > 1:
        for d1_idx in range(len(b15) - 1):
            for d2_idx in range(d1_idx + 1, len(b15)):
                b16 = b15[d1_idx]
                b17 = b15[d2_idx]
                b18 = calculate_devices_weight(b16, b17, devices_info)
                b14.add_edge(b16, b17, b19 = b18)
    return b14
if b20 = = "__main__":
    b21 = True
    if len(sys.argv) > 1 and sys.argv[1] == '-w':
        b21 = False
    b22 = [
        'ijcai_device_encode_test_sample.csv',
        'ijcai_cookie_encode_test_sample.csv'
    ]
    if not b21:
        b22 = [
            'ijcai_device_encode_training.csv',
            'ijcai_device_encode_test.csv',
            'ijcai_cookie_encode_training.csv',
            'ijcai_cookie_encode_test.csv'
        ]
    b2, b3 = fonk1(b22, b21)
    b7 = fonk2(b2, b22, b21)
    b23 = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    b24 = []
    for user_idx, user in enumerate(b2):
        b25 = time.time()
        b26 = 100 * (user_idx + 1) / len(b2)
        sys.stdout.write(f'\r>> Processing Users............ {b26:.2f} %')
        sys.stdout.flush()
        b27 = b3[user]
        median_T, b11 = fonk3(user, b27)
        if not b11 and not median_T:
            print(f'Cannot Parse Current User: {user}')
            continue
        b28 = b7[user]
        b29 = fonk4(b11, b28)
        b30 = []
        for key in b29.keys():
            b14 = fonk5(name=f'{user}_{key}', devices_info=b29[key])
            b30.append(b14)
        b31 = merged_graph(user, b30)
        b32 = time.time() - b25
        b24.append(b32)
        draw_graph(str(median_T), b23, str(user_idx), user, b31, b33 = True, save_to_disk=True)
    print('\n')
    b34 = min(b24)
    b35 = max(b24)
    b36 = sum(b24) / len(b24)
    b37 = sum(b24)
    print(f'b34: {b34}')
    print(f'b36: {b36}')
    print(f'b35: {b35}')
    print(f'b9: {b37}')
    with open('b9', 'w') as f:
        for t in b24:
            f.write(f'{t}\n')
    print('\nAll done!!!')
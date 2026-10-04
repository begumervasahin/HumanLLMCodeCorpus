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
def extract_time(filenames, test_flag=True):
    all_user_id = []
    all_user_time_info = {}
    all_user_id_file = 'all_user_id.txt'
    user_time_info_file = 'user_time_info.json'
    if test_flag:
        all_user_id_file = '10_all_user_id.txt'
        user_time_info_file = '10_user_time_info.json'
    if os.path.exists(user_time_info_file) and os.path.exists(all_user_id_file):
        with open(all_user_id_file, 'r') as f:
            all_user_id = [line.strip() for line in f.readlines()]
        with open(user_time_info_file, 'r') as f:
            all_user_time_info = json.load(f)
        print(f'--Done loading files:\t{all_user_id_file}, {user_time_info_file}')
    else:
        all_user_id, all_user_time_info = extract_user_time(filenames)
    return all_user_id, all_user_time_info
def extract_user_info(all_user_id, filenames, test_flag=True):
    all_user_info_file = "all_user_info.json"
    if test_flag:
        all_user_info_file = '10_all_user_info.json'
    if os.path.exists(all_user_info_file):
        with open(all_user_info_file, 'r') as f:
            all_user_info = json.load(f)
        print(f'--Done Loading Files:\t{all_user_info_file}')
    else:
        all_user_info = extract_user_devices_info(all_user_id, filenames)
    return all_user_info
def analyze_time(user, per_user_info):
    try:
        reach_time = per_user_info["Reach_Time"]
        all_time = sorted(set(reach_time))
        median_deltaT = find_median_delta_T(all_time)
    except Exception as exc:
        print(f'Abnormal User ID: {user}')
        print(traceback.format_exc())
        print(exc)
        return None, None
    dates_interval_dict = generate_time_group(all_time, median_deltaT)
    return median_deltaT, dates_interval_dict
def group_user_behavior_by_dates_interval(dates_interval_dict, current_user_info):
    grouped_user_info_dict = {}
    for key, time_group in dates_interval_dict.items():
        grouped_devices_dict = extract_devices_behavior_on_time_group(time_group, current_user_info)
        grouped_user_info_dict[key] = grouped_devices_dict
    return grouped_user_info_dict
def construct_graph(name, devices_info):
    graph = nx.Graph(name=name)
    devices_list = list(devices_info.keys())
    graph.add_nodes_from(devices_list)
    if len(devices_list) > 1:
        for d1_idx in range(len(devices_list) - 1):
            for d2_idx in range(d1_idx + 1, len(devices_list)):
                d1 = devices_list[d1_idx]
                d2 = devices_list[d2_idx]
                edge_weight = calculate_devices_weight(d1, d2, devices_info)
                graph.add_edge(d1, d2, weight=edge_weight)
    return graph
def main():
    global IO_Time
    IO_Time = 0
    test_flag = True
    try:
        if sys.argv[1] == '-w':
            test_flag = False
    except:
        pass
    filenames = ['ijcai_device_encode_test_sample.csv', 'ijcai_cookie_encode_test_sample.csv']
    if not test_flag:
        filenames = [
            'ijcai_device_encode_training.csv',
            'ijcai_device_encode_test.csv',
            'ijcai_cookie_encode_training.csv',
            'ijcai_cookie_encode_test.csv'
        ]
    all_user_id, all_user_time_info = extract_time(filenames, test_flag)
    all_user_info = extract_user_info(all_user_id, filenames, test_flag)
    current_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    construction_times = []
    for user_idx, user in enumerate(all_user_id):
        start_time = time.time()
        percentage = 100 * (user_idx + 1) / len(all_user_id)
        sys.stdout.write(f'\r>> Processing Users............ {percentage:.2f} %')
        sys.stdout.flush()
        per_user_info = all_user_time_info[user]
        median_T, dates_interval_dict = analyze_time(user, per_user_info)
        if not dates_interval_dict or not median_T:
            print(f'Cannot Parse Current User: {user}')
            continue
        current_user_info = all_user_info[user]
        current_user_time_based_device = group_user_behavior_by_dates_interval(dates_interval_dict, current_user_info)
        graph_list = []
        for key, devices_info in current_user_time_based_device.items():
            graph = construct_graph(name=f'{user}_{key}', devices_info=devices_info)
            graph_list.append(graph)
        multi_layer_graph = merged_graph(user, graph_list)
        time_interval = time.time() - start_time
        construction_times.append(time_interval)
        draw_graph(str(median_T), current_time, str(user_idx), user, multi_layer_graph, self_define_pos=True, save_to_disk=True)
    print('\n')
    print('min_time:  ', min(construction_times))
    print('avg_time:  ', sum(construction_times) / len(construction_times))
    print('max_time:  ', max(construction_times))
    print('all_time:  ', sum(construction_times))
    with open('all_time', 'w') as f:
        for t in construction_times:
            f.write(f'{t}\n')
    print('\nAll done!!!')
if __name__ == "__main__":
    main()
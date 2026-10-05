from __future__ import print_function, division
import sys
import os
import json
import networkx as nx
from datetime import datetime
import time
def extract_user_time(filenames):
    pass
def extract_user_devices_info(all_user_id, filenames):
    pass
def find_median_delta_T(all_time):
    pass
def generate_time_group(all_time, median_deltaT):
    pass
def extract_devices_behavior_on_time_group(time_group, current_user_info):
    pass
def calculate_devices_weight(d1, d2, devices_info):
    pass
def merge_graphs(user, graph_list):
    pass
def draw_graph(median_T, current_time, user_idx, user, multi_layer_graph, self_define_pos=True, save_to_disk=True):
    pass
def mean(lst):
    return sum(lst) / len(lst)
def extract_time_information(filenames, test_flag=True):
    all_user_id = []
    all_user_time_info = {}
    all_user_id_file = 'all_user_id.txt'
    user_time_info_file = 'user_time_info.json'
    if test_flag:
        all_user_id_file = '10_all_user_id.txt'
        user_time_info_file = '10_user_time_info.json'
    if os.path.exists(user_time_info_file) and os.path.exists(all_user_id_file):
        with open(all_user_id_file, 'r+') as f:
            for line in f.readlines():
                all_user_id.append(line.strip())
        all_user_time_info = json.load(open(user_time_info_file))
        print('--Done loading files:\t%s, %s' % (all_user_id_file, user_time_info_file))
    else:
        all_user_id, all_user_time_info = extract_user_time(filenames)
    return all_user_id, all_user_time_info
def extract_user_info(all_user_id, filenames, test_flag=True):
    all_user_info_file = "all_user_info.json"
    if test_flag:
        all_user_info_file = '10_all_user_info.json'
    if os.path.exists(all_user_info_file):
        all_user_info = json.load(open(all_user_info_file))
        print('--Done Loading Files:\t%s' % all_user_info_file)
    else:
        all_user_info = extract_user_devices_info(all_user_id, filenames)
    return all_user_info
def analyze_time(user, per_user_info):
    try:
        reach_time = per_user_info["Reach_Time"]
        all_time = sorted(list(set(sorted(reach_time))))
        median_deltaT = find_median_delta_T(all_time)
    except Exception as exc:
        print('Abnormal User ID: %s' % user)
        print(traceback.format_exc())
        print(exc)
    dates_interval_dict = generate_time_group(all_time, median_deltaT)
    return median_deltaT, dates_interval_dict
def group_user_behavior_by_dates_interval(dates_interval_dict, current_user_info):
    grouped_user_info_dict = {}
    for key in dates_interval_dict.keys():
        time_group = dates_interval_dict[key]
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
if __name__ == "__main__":
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
    all_user_id, all_user_time_info = extract_time_information(filenames, test_flag)
    all_user_info = extract_user_info(all_user_id, filenames, test_flag)
    current_time = str(datetime.now()).split()[0] + '-' + str(datetime.now()).split()[1]
    construction_times = []
    for user_idx, user in enumerate(all_user_id):
        start_time = time.time()
        percentage = 100 * (user_idx + 1) / len(all_user_id)
        sys.stdout.write('\r>> Processing Users............ %.2f %%' % percentage)
        sys.stdout.flush()
        per_user_info = all_user_time_info[user]
        median_T, dates_interval_dict = analyze_time(user, per_user_info)
        if not dates_interval_dict and not median_T:
            print('Cannot Parse Current User: %s' % user)
            continue
        current_user_info = all_user_info[user]
        current_user_time_based_device = group_user_behavior_by_dates_interval(dates_interval_dict, current_user_info)
        graph_list = []
        for key in current_user_time_based_device.keys():
            graph = construct_graph(
                name=user + '_' + str(key),
                devices_info=current_user_time_based_device[key]
            )
            graph_list.append(graph)
        multi_layer_graph = merge_graphs(user, graph_list)
        time_interval = time.time() - start_time
        construction_times.append(time_interval)
        draw_graph(str(median_T), current_time, str(user_idx), user, multi_layer_graph, self_define_pos=True,
                   save_to_disk=True)
    print('\n')
    min_time = min(construction_times)
    max_time = max(construction_times)
    avg_time = mean(construction_times)
    sum_time = sum(construction_times)
    print('min_time:  ', min_time)
    print('avg_time:  ', avg_time)
    print('max_time:  ', max_time)
    print('all_tim:   ', sum_time)
    with open('all_time', 'w+') as f:
        for i in construction_times:
            f.write(str(i))
            f.write('\n')
    print('\nall down!!!')
import time
import json
import random
import traceback
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
from datetime import datetime
def to_seconds(time_str):
    formatted_time = f"{time_str[:4]}-{time_str[4:6]}-{time_str[6:8]} {time_str[8:10]}:{time_str[10:12]}:{time_str[12:]}"
    time_obj = datetime.strptime(formatted_time, "%Y-%m-%d %H:%M:%S")
    return time.mktime(time_obj.timetuple())
def find_median_delta_t(time_list):
    delta_times = [abs(to_seconds(time_list[i+1]) - to_seconds(time_list[i])) for i in range(len(time_list) - 1)]
    delta_times = [dt for dt in delta_times if dt != 0]
    if not delta_times:
        delta_times = [0]
    return mean(delta_times)
def generate_time_groups(time_list, delta_t):
    time_groups = {}
    group_count = 1
    idx = 0
    while idx < len(time_list) - 1:
        group = {time_list[idx]}
        while idx < len(time_list) - 1 and abs(to_seconds(time_list[idx+1]) - to_seconds(time_list[idx])) <= delta_t:
            group.add(time_list[idx + 1])
            idx += 1
        time_groups[group_count] = list(group)
        group_count += 1
        idx += 1
    if len(time_list) - 1 not in group:
        time_groups[group_count] = [time_list[-1]]
    return time_groups
def extract_user_times(filenames):
    all_user_ids = set()
    all_user_times = {}
    for file in filenames:
        with open(file, 'r') as f:
            for count, row in enumerate(f):
                if count == 0:
                    continue
                row_data = row.strip().split(',')
                user_id = row_data[0]
                if 'device' in file:
                    all_user_ids.add(user_id)
                    if user_id not in all_user_times:
                        all_user_times[user_id] = {'Reach_Time': []}
                    all_user_times[user_id]['Reach_Time'].append(row_data[-2])
                elif 'cookie' in file and user_id in all_user_ids:
                    if user_id not in all_user_times:
                        all_user_times[user_id] = {'Data_Time': []}
                    all_user_times[user_id]['Data_Time'].append(row_data[1])
    with open('all_user_id.txt', 'w') as f:
        for user_id in all_user_ids:
            f.write(f"{user_id}\n")
    with open('user_time_info.json', 'w') as f:
        json.dump(all_user_times, f)
    sampled_user_ids = random.sample(all_user_ids, 10)
    sampled_user_times = {user_id: all_user_times[user_id] for user_id in sampled_user_ids}
    with open('10_all_user_id.txt', 'w') as f:
        for user_id in sampled_user_ids:
            f.write(f"{user_id}\n")
    with open('10_user_time_info.json', 'w') as f:
        json.dump(sampled_user_times, f)
    return all_user_ids, all_user_times
def extract_user_devices_info(all_user_ids, filenames):
    all_user_info = {}
    for file in filenames:
        with open(file, 'r') as f:
            for count, row in enumerate(f):
                if count == 0:
                    continue
                row_data = row.strip().split(',')
                user_id = row_data[0]
                if user_id not in all_user_ids:
                    continue
                if user_id not in all_user_info:
                    all_user_info[user_id] = {'Reach_Time': {}, 'Data_Time': {}}
                if 'device' in file:
                    reach_time = row_data[-2]
                    device_ip = row_data[-9]
                    keyword = row_data[-8]
                    devices = row_data[1:4]
                    if reach_time not in all_user_info[user_id]['Reach_Time']:
                        all_user_info[user_id]['Reach_Time'][reach_time] = {}
                    for device in devices:
                        if device:
                            if device not in all_user_info[user_id]['Reach_Time'][reach_time]:
                                all_user_info[user_id]['Reach_Time'][reach_time][device] = {'Device_IP': [], 'Keyword': []}
                            all_user_info[user_id]['Reach_Time'][reach_time][device]['Device_IP'].append(device_ip)
                            all_user_info[user_id]['Reach_Time'][reach_time][device]['Keyword'].append(keyword)
                if 'cookie' in file:
                    data_time = row_data[1]
                    cookie = row_data[2]
                    cookie_ip = row_data[-2]
                    title = row_data[-1]
                    if data_time not in all_user_info[user_id]['Data_Time']:
                        all_user_info[user_id]['Data_Time'][data_time] = {'Cookie': [], 'Cookie_IP': [], 'title': []}
                    all_user_info[user_id]['Data_Time'][data_time]['Cookie'].append(cookie)
                    all_user_info[user_id]['Data_Time'][data_time]['Cookie_IP'].append(cookie_ip)
                    all_user_info[user_id]['Data_Time'][data_time]['title'].append(title)
    with open('all_user_info.json', 'w') as f:
        json.dump(all_user_info, f)
    sampled_user_ids = []
    with open('10_all_user_id.txt', 'r') as f:
        sampled_user_ids = [line.strip() for line in f]
    sampled_user_info = {user_id: all_user_info[user_id] for user_id in sampled_user_ids}
    with open('10_all_user_info.json', 'w') as f:
        json.dump(sampled_user_info, f)
    return all_user_info
def extract_device_behavior_by_time_group(time_group, user_info):
    device_behaviors = {}
    for data_time in user_info['Data_Time']:
        if data_time in time_group:
            continue
    for reach_time in user_info['Reach_Time']:
        if reach_time in time_group:
            devices = user_info['Reach_Time'][reach_time]
            for device in devices:
                if device not in device_behaviors:
                    device_behaviors[device] = {'Keyword': [], 'Device_IP': []}
                device_behaviors[device]['Keyword'].append(devices[device]['Keyword'])
                device_behaviors[device]['Device_IP'].append(devices[device]['Device_IP'])
    return device_behaviors
def calculate_device_similarity(device1, device2, devices_info):
    def jaccard_similarity(list1, list2):
        set1 = {item for sublist in list1 for item in sublist}
        set2 = {item for sublist in list2 for item in sublist}
        intersection = set1 & set2
        union = set1 | set2
        return len(intersection) / len(union) if union else 0.0
    keyword_similarity = jaccard_similarity(devices_info[device1]['Keyword'], devices_info[device2]['Keyword'])
    ip_similarity = jaccard_similarity(devices_info[device1]['Device_IP'], devices_info[device2]['Device_IP'])
    return 0.5 * keyword_similarity + 0.5 * ip_similarity
def merge_graphs(user_name, graph_list):
    merged_graph = nx.Graph(name=f"merged_{user_name}")
    for idx, graph in enumerate(graph_list):
        nodes = [f"{node}_{idx}" for node in graph.nodes()]
        merged_graph.add_nodes_from(nodes)
        for u, v, data in graph.edges(data=True):
            merged_graph.add_edge(f"{u}_{idx}", f"{v}_{idx}", weight=data['weight'])
        if idx > 0:
            for node in nodes:
                original_node = node.split('_')[0]
                previous_node = f"{original_node}_{idx - 1}"
                if previous_node in merged_graph.nodes:
                    merged_graph.add_edge(node, previous_node, weight=0)
    return merged_graph
def draw_graph(median_t, current_time, user_idx, user_name, graph, define_positions=True, save_to_disk=True):
    cleaned_graph = nx.Graph(name=graph.name)
    node_map = {node.split('_')[0]: f"d{idx}" for idx, node in enumerate(graph.nodes())}
    for node in graph.nodes():
        original_node, idx = node.split('_')
        cleaned_graph.add_node(f"{node_map[original_node]}_{idx}")
    for u, v, data in graph.edges(data=True):
        if u != v:
            original_u, idx_u = u.split('_')
            original_v, idx_v = v.split('_')
            cleaned_graph.add_edge(f"{node_map[original_u]}_{idx_u}", f"{node_map[original_v]}_{idx_v}", weight=data['weight'])
    if define_positions:
        positions = {}
        layers = sorted(set(node.split('_')[1] for node in cleaned_graph.nodes()))
        y = 0.0
        for layer in layers:
            x = 0.0
            for node in sorted(cleaned_graph.nodes()):
                if layer == node.split('_')[1]:
                    positions[node] = (x, y)
                    x += 0.2
            y += 1.0
    else:
        positions = nx.spring_layout(cleaned_graph)
    nx.draw_networkx_nodes(cleaned_graph, positions, node_color='w', node_size=100)
    for u, v, data in cleaned_graph.edges(data=True):
        color = 'r' if data['weight'] == 0 else 'k' if data['weight'] == 1 else 'b'
        style = 'dashed' if data['weight'] == 0 else 'solid'
        nx.draw_networkx_edges(cleaned_graph, positions, edgelist=[(u, v)], edge_color=color, style=style, width=0.5)
    nx.draw_networkx_labels(cleaned_graph, positions, font_size=3)
    if save_to_disk:
        nx.draw_networkx_edge_labels(cleaned_graph, positions, label_pos=0.5, font_size=1)
        dir_name = f"{current_time}---sampled_results"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        nx.write_gml(graph, f"{dir_name}/{user_idx}--{median_t}.gml")
        plt.savefig(f"{dir_name}/{user_idx}--{median_t}.pdf")
        with open(f"{dir_name}/abnormal_user.txt", 'a') as f:
            f.write(f"{user_name}\n")
    plt.clf()
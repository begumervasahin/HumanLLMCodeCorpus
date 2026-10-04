import time
import json
import os
import random
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
from datetime import datetime
def to_second(time_str):
    formatted_time_str = f"{time_str[0:4]}-{time_str[4:6]}-{time_str[6:8]} {time_str[8:10]}:{time_str[10:12]}:{time_str[12:]}"
    time_obj = datetime.strptime(formatted_time_str, "%Y-%m-%d %H:%M:%S")
    return time.mktime(time_obj.timetuple())
def find_median_delta_T(all_time):
    all_delta_T = [abs(to_second(all_time[i+1]) - to_second(all_time[i])) for i in range(len(all_time) - 1)]
    all_delta_T = [delta for delta in all_delta_T if delta != 0]
    return mean(all_delta_T) if all_delta_T else 0
def generate_time_group(all_time, deltaT):
    interval_count = 1
    interval_dict = {}
    t1_idx = 0
    last_one_hit = False
    while t1_idx <= len(all_time) - 1:
        t2_idx = t1_idx + 1
        if t2_idx >= len(all_time):
            break
        t1 = all_time[t1_idx]
        t2 = all_time[t2_idx]
        group = {t1}
        while abs(to_second(t1) - to_second(t2)) <= deltaT:
            group.add(t2)
            t1_idx += 1
            t2_idx += 1
            if t2_idx >= len(all_time):
                break
            t1 = all_time[t1_idx]
            t2 = all_time[t2_idx]
        interval_dict[interval_count] = list(group)
        interval_count += 1
        t1_idx = t2_idx
    if not last_one_hit and t1_idx < len(all_time):
        interval_dict[interval_count] = [all_time[-1]]
    return interval_dict
def extract_user_time(filenames):
    all_user_id = set()
    all_user_time_info = {}
    for file in filenames:
        print(f'Processing file: {file}')
        with open(file, 'r') as f:
            for count, row in enumerate(f.readlines()):
                if count == 0:
                    continue
                row = row.strip().split(',')
                user = row[0]
                if 'device' in file:
                    all_user_id.add(user)
                    if user not in all_user_time_info:
                        all_user_time_info[user] = {'Reach_Time': []}
                    try:
                        all_user_time_info[user]['Reach_Time'].append(row[-2])
                    except Exception as exc:
                        print(f"Error processing reach time: {exc}")
                elif 'cookie' in file and user in all_user_id:
                    if 'Data_Time' not in all_user_time_info[user]:
                        all_user_time_info[user]['Data_Time'] = []
                    try:
                        all_user_time_info[user]['Data_Time'].append(row[1])
                    except Exception as exc:
                        print(f"Error processing data time: {exc}")
    with open('all_user_id.txt', 'w') as f:
        f.writelines([f"{user_id}\n" for user_id in all_user_id])
    with open('user_time_info.json', 'w') as f:
        json.dump(all_user_time_info, f)
    sampled_all_user_id = random.sample(list(all_user_id), 10)
    with open('10_all_user_id.txt', 'w') as f:
        f.writelines([f"{user_id}\n" for user_id in sampled_all_user_id])
    sampled_all_user_time_info = {user: all_user_time_info[user] for user in sampled_all_user_id}
    with open('10_user_time_info.json', 'w') as f:
        json.dump(sampled_all_user_time_info, f)
    return all_user_id, all_user_time_info
def extract_user_devices_info(all_user_id, filenames):
    all_user_info = {}
    for file in filenames:
        print(f'Processing file: {file}')
        with open(file, 'r') as f:
            for count, row in enumerate(f.readlines()):
                if count == 0:
                    continue
                row = row.strip().split(',')
                user = row[0]
                if user not in all_user_info:
                    all_user_info[user] = {'Reach_Time': {}, 'Data_Time': {}}
                if 'device' in file:
                    try:
                        reach_time = row[-2]
                        device_ip = row[-9]
                        keyword = row[-8]
                        if reach_time not in all_user_info[user]['Reach_Time']:
                            all_user_info[user]['Reach_Time'][reach_time] = {}
                        devices = row[1:4]
                        for d in devices:
                            if d:
                                if d not in all_user_info[user]['Reach_Time'][reach_time]:
                                    all_user_info[user]['Reach_Time'][reach_time][d] = {'Device_IP': [], 'Keyword': []}
                                all_user_info[user]['Reach_Time'][reach_time][d]['Device_IP'].append(device_ip)
                                all_user_info[user]['Reach_Time'][reach_time][d]['Keyword'].append(keyword)
                    except Exception as exc:
                        print(f"Error processing device info: {exc}")
                elif 'cookie' in file:
                    try:
                        data_time = row[1]
                        cookie = row[2]
                        cookie_ip = row[-2]
                        title = row[-1]
                        if data_time not in all_user_info[user]['Data_Time']:
                            all_user_info[user]['Data_Time'][data_time] = {'Cookie': [], 'Cookie_IP': [], 'title': []}
                        all_user_info[user]['Data_Time'][data_time]['Cookie'].append(cookie)
                        all_user_info[user]['Data_Time'][data_time]['Cookie_IP'].append(cookie_ip)
                        all_user_info[user]['Data_Time'][data_time]['title'].append(title)
                    except Exception as exc:
                        print(f"Error processing cookie info: {exc}")
    with open('all_user_info.json', 'w') as f:
        json.dump(all_user_info, f)
    sampled_user_id = []
    with open('10_all_user_id.txt', 'r') as f:
        sampled_user_id = [line.strip() for line in f.readlines()]
    sampled_user_info = {user: all_user_info[user] for user in sampled_user_id}
    with open('10_all_user_info.json', 'w') as f:
        json.dump(sampled_user_info, f)
    return all_user_info
def extract_devices_behavior_on_time_group(time_group, current_user_info):
    grouped_devices_dict = {}
    for data_time in current_user_info['Data_Time']:
        if data_time in time_group:
            pass
    for reach_time in current_user_info['Reach_Time']:
        if reach_time in time_group:
            devices = current_user_info['Reach_Time'][reach_time]
            for device, info in devices.items():
                if device not in grouped_devices_dict:
                    grouped_devices_dict[device] = {'Keyword': [], 'Device_IP': []}
                grouped_devices_dict[device]['Keyword'].extend(info['Keyword'])
                grouped_devices_dict[device]['Device_IP'].extend(info['Device_IP'])
    return grouped_devices_dict
def calculate_devices_weight(d1, d2, devices_info):
    def _jaccard(l1, l2):
        l1 = [item for sublist in l1 for item in sublist]
        l2 = [item for sublist in l2 for item in sublist]
        common = set(l1) & set(l2)
        all_items = set(l1) | set(l2)
        return len(common) / len(all_items) if all_items else 0.0
    keyword_weight = _jaccard(devices_info[d1]['Keyword'], devices_info[d2]['Keyword'])
    ip_weight = _jaccard(devices_info[d1]['Device_IP'], devices_info[d2]['Device_IP'])
    return 0.5 * keyword_weight + 0.5 * ip_weight
def merged_graph(name, graph_list):
    merged_graph = nx.Graph(name=f'merged_{name}')
    for idx, g in enumerate(graph_list):
        nodes = [f"{node}_{idx}" for node in g.nodes()]
        merged_graph.add_nodes_from(nodes)
        for u, v, w in g.edges(data=True):
            merged_graph.add_edge(f"{u}_{idx}", f"{v}_{idx}", weight=w['weight'])
        if idx > 0:
            previous_idx = idx - 1
            for node in merged_graph.nodes():
                if f"_{idx}" in node:
                    base_node = node.split('_')[0]
                    previous_node = f"{base_node}_{previous_idx}"
                    if previous_node in merged_graph.nodes() and node != previous_node:
                        merged_graph.add_edge(node, previous_node, weight=0)
    return merged_graph
def draw_graph(median_T, current_time, user_idx, user, graph, self_define_pos=True, save_to_disk=True):
    cleaned_graph = nx.Graph(name=graph.name)
    node_map = {}
    idx = 0
    for node in graph.nodes():
        base_node = node.split('_')[0]
        if base_node not in node_map:
            node_map[base_node] = f'd{idx}'
            idx += 1
    for node in graph.nodes():
        base_node, idx = node.split('_')
        cleaned_node = f"{node_map[base_node]}_{idx}"
        cleaned_graph.add_node(cleaned_node)
    for u, v, w in graph.edges(data=True):
        if u != v:
            base_u, idx_u = u.split('_')
            base_v, idx_v = v.split('_')
            cleaned_u = f"{node_map[base_u]}_{idx_u}"
            cleaned_v = f"{node_map[base_v]}_{idx_v}"
            cleaned_graph.add_edge(cleaned_u, cleaned_v, weight=w['weight'])
    pos = nx.spring_layout(cleaned_graph) if not self_define_pos else {
        f"{node_map[node.split('_')[0]]}_{node.split('_')[1]}": (0.2 * i, 1.0 * j)
        for j, layer in enumerate(sorted(set(node.split('_')[1] for node in cleaned_graph.nodes())))
        for i, node in enumerate(sorted(node for node in cleaned_graph.nodes() if layer == node.split('_')[1]))
    }
    nx.draw_networkx_nodes(cleaned_graph, pos, node_color='w', node_size=100)
    for u, v, w in cleaned_graph.edges(data=True):
        color = 'r' if w['weight'] == 0 else 'k' if w['weight'] == 1 else 'b'
        style = 'dashed' if w['weight'] == 0 else 'solid'
        width = 0.5 if w['weight'] == 0 else 1.0
        nx.draw_networkx_edges(cleaned_graph, pos, edgelist=[(u, v)], edge_color=color, style=style, width=width)
    nx.draw_networkx_labels(cleaned_graph, pos, font_size=3)
    if save_to_disk:
        nx.draw_networkx_edge_labels(cleaned_graph, pos, label_pos=0.5, font_size=1)
        output_dir = f"{current_time}---sampled_results"
        os.makedirs(output_dir, exist_ok=True)
        nx.write_gml(graph, f"{output_dir}/{user_idx}--{median_T}.gml")
        plt.savefig(f"{output_dir}/{user_idx}--{median_T}.pdf")
        with open(f"{output_dir}/abnormal_user.txt", 'a') as f:
            f.write(f"{user}\n")
    plt.clf()
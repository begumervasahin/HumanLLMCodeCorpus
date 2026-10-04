import time
import json
import os
import random
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
from datetime import datetime
def fonk1(timestamp):
    b1 = f"{timestamp[:4]}-{timestamp[4:6]}-{timestamp[6:8]} {timestamp[8:10]}:{timestamp[10:12]}:{timestamp[12:]}"
    b2 = datetime.strptime(b1, "%Y-%m-%d %H:%M:%S")
    return time.mktime(b2.timetuple())
def fonk2(all_timestamps):
    b3 = [abs(fonk1(all_timestamps[a2 + 1]) - fonk1(all_timestamps[a2])) for a2 in range(len(all_timestamps) - 1)]
    b4 = [delta for delta in b3 if delta != 0]
    return mean(b4) if b4 else 0
def fonk3(all_timestamps, delta_t):
    b5 = {}
    b6 = set()
    a1 = 1
    a2 = 0
    while a2 < len(all_timestamps):
        b6.add(all_timestamps[a2])
        b7 = a2 + 1
        while b7 < len(all_timestamps) and abs(fonk1(all_timestamps[b7]) - fonk1(all_timestamps[a2])) <= delta_t:
            b6.add(all_timestamps[b7])
            a2 += 1
            b7 += 1
        b5[a1] = list(b6)
        b6 = set()
        a1 += 1
        a2 += 1
    if a2 < len(all_timestamps):
        b5[a1] = [all_timestamps[-1]]
    return b5
def fonk4(filenames):
    b8 = set()
    b9 = {}
    for filename in filenames:
        print(f'Processing file: {filename}')
        with open(filename, 'r') as file:
            for b10, line in enumerate(file):
                if b10 = = 0:
                    continue
                b11 = line.strip().split(',')
                b12 = b11[0]
                if 'device' in filename:
                    b8.add(b12)
                    if b12 not in b9:
                        b9[b12] = {'Reach_Time': []}
                    try:
                        b9[b12]['Reach_Time'].append(b11[-2])
                    except Exception as e:
                        print(f"Error processing reach time: {e}")
                elif 'b21' in filename and b12 in b8:
                    if 'Data_Time' not in b9[b12]:
                        b9[b12]['Data_Time'] = []
                    try:
                        b9[b12]['Data_Time'].append(b11[1])
                    except Exception as e:
                        print(f"Error processing b34 time: {e}")
    with open('all_user_id.txt', 'w') as file:
        file.writelines([f"{user_id}\n" for user_id in b8])
    with open('user_time_info.json', 'w') as file:
        json.dump(b9, file)
    b13 = random.sample(list(b8), 10)
    with open('10_all_user_id.txt', 'w') as file:
        file.writelines([f"{user_id}\n" for user_id in b13])
    b14 = {b12: b9[b12] for b12 in b13}
    with open('10_user_time_info.json', 'w') as file:
        json.dump(b14, file)
    return b8, b9
def fonk5(b8, filenames):
    b15 = {}
    for filename in filenames:
        print(f'Processing file: {filename}')
        with open(filename, 'r') as file:
            for b10, line in enumerate(file):
                if b10 = = 0:
                    continue
                b11 = line.strip().split(',')
                b12 = b11[0]
                if b12 not in b15:
                    b15[b12] = {'Reach_Time': {}, 'Data_Time': {}}
                if 'device' in filename:
                    try:
                        b16 = b11[-2]
                        b17 = b11[-9]
                        b18 = b11[-8]
                        b19 = b11[1:4]
                        if b16 not in b15[b12]['Reach_Time']:
                            b15[b12]['Reach_Time'][b16] = {}
                        for device in b19:
                            if device:
                                if device not in b15[b12]['Reach_Time'][b16]:
                                    b15[b12]['Reach_Time'][b16][device] = {'Device_IP': [], 'Keyword': []}
                                b15[b12]['Reach_Time'][b16][device]['Device_IP'].append(b17)
                                b15[b12]['Reach_Time'][b16][device]['Keyword'].append(b18)
                    except Exception as e:
                        print(f"Error processing device info: {e}")
                elif 'b21' in filename:
                    try:
                        b20 = b11[1]
                        b21 = b11[2]
                        b22 = b11[-2]
                        b23 = b11[-1]
                        if b20 not in b15[b12]['Data_Time']:
                            b15[b12]['Data_Time'][b20] = {'Cookie': [], 'Cookie_IP': [], 'b23': []}
                        b15[b12]['Data_Time'][b20]['Cookie'].append(b21)
                        b15[b12]['Data_Time'][b20]['Cookie_IP'].append(b22)
                        b15[b12]['Data_Time'][b20]['b23'].append(b23)
                    except Exception as e:
                        print(f"Error processing b21 info: {e}")
    with open('b15.json', 'w') as file:
        json.dump(b15, file)
    with open('10_all_user_id.txt', 'r') as file:
        b13 = [line.strip() for line in file]
    b24 = {b12: b15[b12] for b12 in b13}
    with open('10_all_user_info.json', 'w') as file:
        json.dump(b24, file)
    return b15
def fonk6(time_group, user_info):
    b25 = {}
    for b20 in user_info['Data_Time']:
        if b20 in time_group:
            continue
    for b16 in user_info['Reach_Time']:
        if b16 in time_group:
            b19 = user_info['Reach_Time'][b16]
            for device, info in b19.items():
                if device not in b25:
                    b25[device] = {'Keyword': [], 'Device_IP': []}
                b25[device]['Keyword'].extend(info['Keyword'])
                b25[device]['Device_IP'].extend(info['Device_IP'])
    return b25
def fonk7(device1, device2, device_info):
    def fonk8(list1, list2):
        b26 = [item for sublist in list1 for item in sublist]
        b27 = [item for sublist in list2 for item in sublist]
        b28 = set(b26) & set(b27)
        b29 = set(b26) | set(b27)
        return len(b28) / len(b29) if b29 else 0.0
    b30 = fonk8(device_info[device1]['Keyword'], device_info[device2]['Keyword'])
    b31 = fonk8(device_info[device1]['Device_IP'], device_info[device2]['Device_IP'])
    return 0.5 * b30 + 0.5 * b31
def fonk9(name, graph_list):
    b32 = nx.Graph(name=f'merged_{name}')
    for b41, graph in enumerate(graph_list):
        b33 = [f"{node}_{b41}" for node in graph.b33()]
        b32.add_nodes_from(b33)
        for u, v, w in graph.edges(b34 = True):
            b32.add_edge(f"{u}_{b41}", f"{v}_{b41}", b35 = w['b35'])
        if b41 > 0:
            for node in b32.b33():
                if f"_{b41}" in node:
                    b36 = node.split('_')[0]
                    b37 = f"{b36}_{b41 - 1}"
                    if b37 in b32.b33() and node != b37:
                        b32.add_edge(node, b37, b35 = 0)
    return b32
def fonk10(median_t, current_time, user_idx, b12, graph, b38 = True, save_to_disk=True):
    b39 = nx.Graph(name=graph.name)
    b40 = {node.split('_')[0]: f'd{b41}' for b41, node in enumerate(graph.b33())}
    for node in graph.b33():
        b36, b41 = node.split('_')
        b42 = f"{b40[b36]}_{b41}"
        b39.add_node(b42)
    for u, v, w in graph.edges(b34 = True):
        if u != v:
            b39.add_edge(
                f"{b40[u.split('_')[0]]}_{u.split('_')[1]}",
                f"{b40[v.split('_')[0]]}_{v.split('_')[1]}",
                b35 = w['b35']
            )
    if b38:
        b43 = {f"{b40[node.split('_')[0]]}_{node.split('_')[1]}": (0.2 * a2, b7)
               for b7, b44 in enumerate(sorted(set(node.split('_')[1] for node in b39.b33())))
               for a2, node in enumerate(sorted(node for node in b39.b33() if b44 = = node.split('_')[1]))}
    else:
        b43 = nx.spring_layout(b39)
    nx.draw_networkx_nodes(b39, b43, b45 = 'w', node_size=100)
    for u, v, w in b39.edges(b34 = True):
        nx.draw_networkx_edges(
            b39, b43, b46 = [(u, v)], edge_color='r' if w['b35'] == 0 else 'k' if w['b35'] == 1 else 'b',
            b47 = 'dashed' if w['b35'] == 0 else 'solid', width=0.5 if w['b35'] == 0 else 1.0
        )
    nx.draw_networkx_labels(b39, b43, b48 = 3)
    if save_to_disk:
        nx.draw_networkx_edge_labels(b39, b43, b49 = 0.5, b48=1)
        b50 = f"{current_time}---sampled_results"
        os.makedirs(b50, b51 = True)
        nx.write_gml(graph, f"{b50}/{user_idx}--{median_t}.gml")
        plt.savefig(f"{b50}/{user_idx}--{median_t}.pdf")
        with open(f"{b50}/abnormal_user.txt", 'a') as file:
            file.write(f"{b12}\n")
    plt.clf()
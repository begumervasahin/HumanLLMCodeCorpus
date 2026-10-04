import time
import csv
import json
import os
import random
import networkx as nx
import matplotlib.pyplot as plt
from statistics import median, mean
from datetime import datetime
def fonk1(time_str):
    b1 = "%s-%s-%s %s:%s:%s" % (
        time_str[0:4], time_str[4:6], time_str[6:8], time_str[8:10], time_str[10:12], time_str[12:])
    b2 = datetime.strptime(b1, "%Y-%m-%d %H:%M:%S")
    return time.mktime(b2.timetuple())
def fonk2(all_time):
    b3 = [
        abs(fonk1(all_time[i+1]) - fonk1(all_time[i]))
        for i in range(len(all_time)-1)
    ]
    b3 = [delta for delta in b3 if delta != 0]
    return mean(b3) if b3 else 0
def fonk3(all_time, deltaT):
    a1 = 1
    b4 = {}
    a2 = 0
    b5 = False
    while a2 <= len(all_time)-1:
        b6 = a2 + 1
        if b6 >= len(all_time):
            break
        b7 = all_time[a2]
        b8 = all_time[b6]
        b9 = {b7}
        while abs(fonk1(b7) - fonk1(b8)) <= deltaT:
            b9.add(b8)
            a2 += 1
            b6 += 1
            if b6 >= len(all_time):
                break
            b7 = all_time[a2]
            b8 = all_time[b6]
        b4[a1] = list(b9)
        a1 += 1
        a2 = b6
    if b5 is False and a2 < len(all_time):
        b4[a1] = [all_time[-1]]
    return b4
def fonk4(filenames):
    b10 = set()
    b11 = {}
    for file in filenames:
        a3 = 0
        a4 = 1000000000000000000000000
        print(f'Processing file: {file}')
        with open(file, 'r') as f:
            for b12 in f.readlines():
                a3 += 1
                if a3 = = 1:
                    continue
                if a3 > a4:
                    break
                b12 = b12.strip().split(',')
                b13 = b12[0]
                if 'device' in file:
                    b10.add(b13)
                    if b13 not in b11:
                        b11[b13] = {'Reach_Time': []}
                    try:
                        b11[b13]['Reach_Time'].append(b12[-2])
                    except Exception as exc:
                        print(f"Error processing reach time: {exc}")
                elif 'b22' in file and b13 in b10:
                    if 'Data_Time' not in b11[b13]:
                        b11[b13]['Data_Time'] = []
                    try:
                        b11[b13]['Data_Time'].append(b12[1])
                    except Exception as exc:
                        print(f"Error processing b36 time: {exc}")
    with open('b10.txt', 'w') as f:
        f.writelines([f"{user_id}\n" for user_id in b10])
    with open('user_time_info.json', 'w') as f:
        json.dump(b11, f)
    b14 = random.sample(list(b10), 10)
    with open('10_all_user_id.txt', 'w') as f:
        f.writelines([f"{user_id}\n" for user_id in b14])
    b15 = {b13: b11[b13] for b13 in b14}
    with open('10_user_time_info.json', 'w') as f:
        json.dump(b15, f)
    return b10, b11
def fonk5(b10, filenames):
    b16 = {}
    for file in filenames:
        a3 = 0
        a4 = 1000000000000000000000000
        print(f'Processing file: {file}')
        with open(file, 'r') as f:
            for b12 in f.readlines():
                a3 += 1
                if a3 = = 1:
                    continue
                if a3 > a4:
                    break
                b12 = b12.strip().split(',')
                b13 = b12[0]
                if b13 not in b16:
                    b16[b13] = {'Reach_Time': {}, 'Data_Time': {}}
                if 'device' in file:
                    try:
                        b17 = b12[-2]
                        b18 = b12[-9]
                        b19 = b12[-8]
                        if b17 not in b16[b13]['Reach_Time']:
                            b16[b13]['Reach_Time'][b17] = {}
                        b20 = b12[1:4]
                        for d in b20:
                            if d:
                                if d not in b16[b13]['Reach_Time'][b17]:
                                    b16[b13]['Reach_Time'][b17][d] = {'Device_IP': [], 'Keyword': []}
                                b16[b13]['Reach_Time'][b17][d]['Device_IP'].append(b18)
                                b16[b13]['Reach_Time'][b17][d]['Keyword'].append(b19)
                    except Exception as exc:
                        print(f"Error processing device info: {exc}")
                elif 'b22' in file:
                    try:
                        b21 = b12[1]
                        b22 = b12[2]
                        b23 = b12[-2]
                        b24 = b12[-1]
                        if b21 not in b16[b13]['Data_Time']:
                            b16[b13]['Data_Time'][b21] = {'Cookie': [], 'Cookie_IP': [], 'b24': []}
                        b16[b13]['Data_Time'][b21]['Cookie'].append(b22)
                        b16[b13]['Data_Time'][b21]['Cookie_IP'].append(b23)
                        b16[b13]['Data_Time'][b21]['b24'].append(b24)
                    except Exception as exc:
                        print(f"Error processing b22 info: {exc}")
    with open('b16.json', 'w') as f:
        json.dump(b16, f)
    b25 = []
    with open('10_all_user_id.txt', 'r') as f:
        b25 = [line.strip() for line in f.readlines()]
    b26 = {b13: b16[b13] for b13 in b25}
    with open('10_all_user_info.json', 'w') as f:
        json.dump(b26, f)
    return b16
def fonk6(time_group, current_user_info):
    b27 = {}
    for b21 in current_user_info['Data_Time']:
        if b21 in time_group:
            pass
    for b17 in current_user_info['Reach_Time']:
        if b17 in time_group:
            b20 = current_user_info['Reach_Time'][b17]
            for device, info in b20.items():
                if device not in b27:
                    b27[device] = {'Keyword': [], 'Device_IP': []}
                b27[device]['Keyword'].extend(info['Keyword'])
                b27[device]['Device_IP'].extend(info['Device_IP'])
    return b27
def fonk7(d1, d2, devices_info):
    def fonk8(b28, b29):
        b28 = [item for sublist in b28 for item in sublist]
        b29 = [item for sublist in b29 for item in sublist]
        b30 = set(b28) & set(b29)
        b31 = set(b28) | set(b29)
        return len(b30) / len(b31) if b31 else 0.0
    b32 = fonk8(devices_info[d1]['Keyword'], devices_info[d2]['Keyword'])
    b33 = fonk8(devices_info[d1]['Device_IP'], devices_info[d2]['Device_IP'])
    return 0.5 * b32 + 0.5 * b33
def fonk9(name, graph_list):
    b34 = nx.Graph(name=f'merged_{name}')
    for a5, g in enumerate(graph_list):
        b35 = [f"{node}_{a5}" for node in g.b35()]
        b34.add_nodes_from(b35)
        for u, v, w in g.edges(b36 = True):
            b34.add_edge(f"{u}_{a5}", f"{v}_{a5}", b37 = w['b37'])
        if a5 > 0:
            b38 = a5 - 1
            for node in b34.b35():
                if f"_{a5}" in node:
                    b39 = node.split('_')[0]
                    b40 = f"{b39}_{b38}"
                    if b40 in b34.b35() and node != b40:
                        b34.add_edge(node, b40, b37 = 0)
    return b34
def fonk10(median_T, current_time, user_idx, b13, graph, b41 = True, save_to_disk=True):
    b42 = nx.Graph(name=graph.name)
    b43 = {}
    a5 = 0
    for node in graph.b35():
        b39 = node.split('_')[0]
        if b39 not in b43:
            b43[b39] = f'd{a5}'
            a5 += 1
    for node in graph.b35():
        b39, a5 = node.split('_')
        b44 = f"{b43[b39]}_{a5}"
        b42.add_node(b44)
    for u, v, w in graph.edges(b36 = True):
        if u != v:
            base_u, b45 = u.split('_')
            base_v, b46 = v.split('_')
            b47 = f"{b43[base_u]}_{b45}"
            b48 = f"{b43[base_v]}_{b46}"
            b42.add_edge(b47, b48, b37 = w['b37'])
    b49 = nx.spring_layout(b42) if not b41 else {
        f"{b43[node.split('_')[0]]}_{node.split('_')[1]}": (0.2 * i, 1.0 * j)
        for j, b50 in enumerate(sorted(set(node.split('_')[1] for node in b42.b35())))
        for i, node in enumerate(sorted(node for node in b42.b35() if b50 = = node.split('_')[1]))
    }
    nx.draw_networkx_nodes(b42, b49, b51 = 'w', node_size=100)
    for u, v, w in b42.edges(b36 = True):
        b52 = 'r' if w['b37'] == 0 else 'k' if w['b37'] == 1 else 'b'
        b53 = 'dashed' if w['b37'] == 0 else 'solid'
        b54 = 0.5 if w['b37'] == 0 else 1.0
        nx.draw_networkx_edges(b42, b49, b55 = [(u, v)], edge_color=b52, b53=b53, b54=b54)
    nx.draw_networkx_labels(b42, b49, b56 = 3)
    if save_to_disk:
        nx.draw_networkx_edge_labels(b42, b49, b57 = 0.5, b56=1)
        b58 = f"{current_time}---sampled_results"
        os.makedirs(b58, b59 = True)
        nx.write_gml(graph, f"{b58}/{user_idx}--{median_T}.gml")
        plt.savefig(f"{b58}/{user_idx}--{median_T}.pdf")
        with open(f"{b58}/abnormal_user.txt", 'a') as f:
            f.write(f"{b13}\n")
    plt.clf()
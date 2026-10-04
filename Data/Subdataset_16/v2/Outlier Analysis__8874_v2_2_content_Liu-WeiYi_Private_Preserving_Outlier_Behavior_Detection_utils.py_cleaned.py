import time
import json
import os
import random
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
from datetime import datetime
def fonk1(time_str):
    b1 = f"{time_str[0:4]}-{time_str[4:6]}-{time_str[6:8]} {time_str[8:10]}:{time_str[10:12]}:{time_str[12:]}"
    b2 = datetime.strptime(b1, "%Y-%m-%d %H:%M:%S")
    return time.mktime(b2.timetuple())
def fonk2(all_time):
    b3 = [abs(fonk1(all_time[i+1]) - fonk1(all_time[i])) for i in range(len(all_time) - 1)]
    b3 = [delta for delta in b3 if delta != 0]
    return mean(b3) if b3 else 0
def fonk3(all_time, deltaT):
    a1 = 1
    b4 = {}
    a2 = 0
    b5 = False
    while a2 <= len(all_time) - 1:
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
    if not b5 and a2 < len(all_time):
        b4[a1] = [all_time[-1]]
    return b4
def fonk4(filenames):
    b10 = set()
    b11 = {}
    for file in filenames:
        print(f'Processing file: {file}')
        with open(file, 'r') as f:
            for b12, b13 in enumerate(f.readlines()):
                if b12 = = 0:
                    continue
                b13 = b13.strip().split(',')
                b14 = b13[0]
                if 'device' in file:
                    b10.add(b14)
                    if b14 not in b11:
                        b11[b14] = {'Reach_Time': []}
                    try:
                        b11[b14]['Reach_Time'].append(b13[-2])
                    except Exception as exc:
                        print(f"Error processing reach time: {exc}")
                elif 'b23' in file and b14 in b10:
                    if 'Data_Time' not in b11[b14]:
                        b11[b14]['Data_Time'] = []
                    try:
                        b11[b14]['Data_Time'].append(b13[1])
                    except Exception as exc:
                        print(f"Error processing b37 time: {exc}")
    with open('b10.txt', 'w') as f:
        f.writelines([f"{user_id}\n" for user_id in b10])
    with open('user_time_info.json', 'w') as f:
        json.dump(b11, f)
    b15 = random.sample(list(b10), 10)
    with open('10_all_user_id.txt', 'w') as f:
        f.writelines([f"{user_id}\n" for user_id in b15])
    b16 = {b14: b11[b14] for b14 in b15}
    with open('10_user_time_info.json', 'w') as f:
        json.dump(b16, f)
    return b10, b11
def fonk5(b10, filenames):
    b17 = {}
    for file in filenames:
        print(f'Processing file: {file}')
        with open(file, 'r') as f:
            for b12, b13 in enumerate(f.readlines()):
                if b12 = = 0:
                    continue
                b13 = b13.strip().split(',')
                b14 = b13[0]
                if b14 not in b17:
                    b17[b14] = {'Reach_Time': {}, 'Data_Time': {}}
                if 'device' in file:
                    try:
                        b18 = b13[-2]
                        b19 = b13[-9]
                        b20 = b13[-8]
                        if b18 not in b17[b14]['Reach_Time']:
                            b17[b14]['Reach_Time'][b18] = {}
                        b21 = b13[1:4]
                        for d in b21:
                            if d:
                                if d not in b17[b14]['Reach_Time'][b18]:
                                    b17[b14]['Reach_Time'][b18][d] = {'Device_IP': [], 'Keyword': []}
                                b17[b14]['Reach_Time'][b18][d]['Device_IP'].append(b19)
                                b17[b14]['Reach_Time'][b18][d]['Keyword'].append(b20)
                    except Exception as exc:
                        print(f"Error processing device info: {exc}")
                elif 'b23' in file:
                    try:
                        b22 = b13[1]
                        b23 = b13[2]
                        b24 = b13[-2]
                        b25 = b13[-1]
                        if b22 not in b17[b14]['Data_Time']:
                            b17[b14]['Data_Time'][b22] = {'Cookie': [], 'Cookie_IP': [], 'b25': []}
                        b17[b14]['Data_Time'][b22]['Cookie'].append(b23)
                        b17[b14]['Data_Time'][b22]['Cookie_IP'].append(b24)
                        b17[b14]['Data_Time'][b22]['b25'].append(b25)
                    except Exception as exc:
                        print(f"Error processing b23 info: {exc}")
    with open('b17.json', 'w') as f:
        json.dump(b17, f)
    b26 = []
    with open('10_all_user_id.txt', 'r') as f:
        b26 = [line.strip() for line in f.readlines()]
    b27 = {b14: b17[b14] for b14 in b26}
    with open('10_all_user_info.json', 'w') as f:
        json.dump(b27, f)
    return b17
def fonk6(time_group, current_user_info):
    b28 = {}
    for b22 in current_user_info['Data_Time']:
        if b22 in time_group:
            pass
    for b18 in current_user_info['Reach_Time']:
        if b18 in time_group:
            b21 = current_user_info['Reach_Time'][b18]
            for device, info in b21.items():
                if device not in b28:
                    b28[device] = {'Keyword': [], 'Device_IP': []}
                b28[device]['Keyword'].extend(info['Keyword'])
                b28[device]['Device_IP'].extend(info['Device_IP'])
    return b28
def fonk7(d1, d2, devices_info):
    def fonk8(b29, b30):
        b29 = [item for sublist in b29 for item in sublist]
        b30 = [item for sublist in b30 for item in sublist]
        b31 = set(b29) & set(b30)
        b32 = set(b29) | set(b30)
        return len(b31) / len(b32) if b32 else 0.0
    b33 = fonk8(devices_info[d1]['Keyword'], devices_info[d2]['Keyword'])
    b34 = fonk8(devices_info[d1]['Device_IP'], devices_info[d2]['Device_IP'])
    return 0.5 * b33 + 0.5 * b34
def fonk9(name, graph_list):
    b35 = nx.Graph(name=f'merged_{name}')
    for a3, g in enumerate(graph_list):
        b36 = [f"{node}_{a3}" for node in g.b36()]
        b35.add_nodes_from(b36)
        for u, v, w in g.edges(b37 = True):
            b35.add_edge(f"{u}_{a3}", f"{v}_{a3}", b38 = w['b38'])
        if a3 > 0:
            b39 = a3 - 1
            for node in b35.b36():
                if f"_{a3}" in node:
                    b40 = node.split('_')[0]
                    b41 = f"{b40}_{b39}"
                    if b41 in b35.b36() and node != b41:
                        b35.add_edge(node, b41, b38 = 0)
    return b35
def fonk10(median_T, current_time, user_idx, b14, graph, b42 = True, save_to_disk=True):
    b43 = nx.Graph(name=graph.name)
    b44 = {}
    a3 = 0
    for node in graph.b36():
        b40 = node.split('_')[0]
        if b40 not in b44:
            b44[b40] = f'd{a3}'
            a3 += 1
    for node in graph.b36():
        b40, a3 = node.split('_')
        b45 = f"{b44[b40]}_{a3}"
        b43.add_node(b45)
    for u, v, w in graph.edges(b37 = True):
        if u != v:
            base_u, b46 = u.split('_')
            base_v, b47 = v.split('_')
            b48 = f"{b44[base_u]}_{b46}"
            b49 = f"{b44[base_v]}_{b47}"
            b43.add_edge(b48, b49, b38 = w['b38'])
    b50 = nx.spring_layout(b43) if not b42 else {
        f"{b44[node.split('_')[0]]}_{node.split('_')[1]}": (0.2 * i, 1.0 * j)
        for j, b51 in enumerate(sorted(set(node.split('_')[1] for node in b43.b36())))
        for i, node in enumerate(sorted(node for node in b43.b36() if b51 = = node.split('_')[1]))
    }
    nx.draw_networkx_nodes(b43, b50, b52 = 'w', node_size=100)
    for u, v, w in b43.edges(b37 = True):
        b53 = 'r' if w['b38'] == 0 else 'k' if w['b38'] == 1 else 'b'
        b54 = 'dashed' if w['b38'] == 0 else 'solid'
        b55 = 0.5 if w['b38'] == 0 else 1.0
        nx.draw_networkx_edges(b43, b50, b56 = [(u, v)], edge_color=b53, b54=b54, b55=b55)
    nx.draw_networkx_labels(b43, b50, b57 = 3)
    if save_to_disk:
        nx.draw_networkx_edge_labels(b43, b50, b58 = 0.5, b57=1)
        b59 = f"{current_time}---sampled_results"
        os.makedirs(b59, b60 = True)
        nx.write_gml(graph, f"{b59}/{user_idx}--{median_T}.gml")
        plt.savefig(f"{b59}/{user_idx}--{median_T}.pdf")
        with open(f"{b59}/abnormal_user.txt", 'a') as f:
            f.write(f"{b14}\n")
    plt.clf()
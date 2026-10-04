import time
import json
import random
import traceback
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
from datetime import datetime
def fonk1(time_str):
    b1 = f"{time_str[:4]}-{time_str[4:6]}-{time_str[6:8]} {time_str[8:10]}:{time_str[10:12]}:{time_str[12:]}"
    b2 = datetime.strptime(b1, "%Y-%m-%d %H:%M:%S")
    return time.mktime(b2.timetuple())
def fonk2(time_list):
    b3 = [abs(fonk1(time_list[i+1]) - fonk1(time_list[i])) for i in range(len(time_list) - 1)]
    b3 = [dt for dt in b3 if dt != 0]
    if not b3:
        b3 = [0]
    return mean(b3)
def fonk3(time_list, delta_t):
    b4 = {}
    a1 = 1
    a2 = 0
    while a2 < len(time_list) - 1:
        b5 = {time_list[a2]}
        while a2 < len(time_list) - 1 and abs(fonk1(time_list[a2 + 1]) - fonk1(time_list[a2])) <= delta_t:
            b5.add(time_list[a2 + 1])
            a2 += 1
        b4[a1] = list(b5)
        a1 += 1
        a2 += 1
    if len(time_list) - 1 not in b5:
        b4[a1] = [time_list[-1]]
    return b4
def fonk4(filenames):
    b6 = set()
    b7 = {}
    for file in filenames:
        with open(file, 'r') as f:
            for b8, row in enumerate(f):
                if b8 = = 0:
                    continue
                b9 = row.strip().split(',')
                b10 = b9[0]
                if 'device' in file:
                    b6.add(b10)
                    if b10 not in b7:
                        b7[b10] = {'Reach_Time': []}
                    b7[b10]['Reach_Time'].append(b9[-2])
                elif 'b19' in file and b10 in b6:
                    if b10 not in b7:
                        b7[b10] = {'Data_Time': []}
                    b7[b10]['Data_Time'].append(b9[1])
    with open('all_user_id.txt', 'w') as f:
        for b10 in b6:
            f.write(f"{b10}\n")
    with open('user_time_info.json', 'w') as f:
        json.dump(b7, f)
    b11 = random.sample(b6, 10)
    b12 = {b10: b7[b10] for b10 in b11}
    with open('10_all_user_id.txt', 'w') as f:
        for b10 in b11:
            f.write(f"{b10}\n")
    with open('10_user_time_info.json', 'w') as f:
        json.dump(b12, f)
    return b6, b7
def fonk5(b6, filenames):
    b13 = {}
    for file in filenames:
        with open(file, 'r') as f:
            for b8, row in enumerate(f):
                if b8 = = 0:
                    continue
                b9 = row.strip().split(',')
                b10 = b9[0]
                if b10 not in b6:
                    continue
                if b10 not in b13:
                    b13[b10] = {'Reach_Time': {}, 'Data_Time': {}}
                if 'device' in file:
                    b14 = b9[-2]
                    b15 = b9[-9]
                    b16 = b9[-8]
                    b17 = b9[1:4]
                    if b14 not in b13[b10]['Reach_Time']:
                        b13[b10]['Reach_Time'][b14] = {}
                    for device in b17:
                        if device:
                            if device not in b13[b10]['Reach_Time'][b14]:
                                b13[b10]['Reach_Time'][b14][device] = {'Device_IP': [], 'Keyword': []}
                            b13[b10]['Reach_Time'][b14][device]['Device_IP'].append(b15)
                            b13[b10]['Reach_Time'][b14][device]['Keyword'].append(b16)
                if 'b19' in file:
                    b18 = b9[1]
                    b19 = b9[2]
                    b20 = b9[-2]
                    b21 = b9[-1]
                    if b18 not in b13[b10]['Data_Time']:
                        b13[b10]['Data_Time'][b18] = {'Cookie': [], 'Cookie_IP': [], 'b21': []}
                    b13[b10]['Data_Time'][b18]['Cookie'].append(b19)
                    b13[b10]['Data_Time'][b18]['Cookie_IP'].append(b20)
                    b13[b10]['Data_Time'][b18]['b21'].append(b21)
    with open('b13.json', 'w') as f:
        json.dump(b13, f)
    b11 = []
    with open('10_all_user_id.txt', 'r') as f:
        b11 = [line.strip() for line in f]
    b22 = {b10: b13[b10] for b10 in b11}
    with open('10_all_user_info.json', 'w') as f:
        json.dump(b22, f)
    return b13
def fonk6(time_group, user_info):
    b23 = {}
    for b18 in user_info['Data_Time']:
        if b18 in time_group:
            continue
    for b14 in user_info['Reach_Time']:
        if b14 in time_group:
            b17 = user_info['Reach_Time'][b14]
            for device in b17:
                if device not in b23:
                    b23[device] = {'Keyword': [], 'Device_IP': []}
                b23[device]['Keyword'].append(b17[device]['Keyword'])
                b23[device]['Device_IP'].append(b17[device]['Device_IP'])
    return b23
def fonk7(device1, device2, devices_info):
    def fonk8(list1, list2):
        b24 = {item for sublist in list1 for item in sublist}
        b25 = {item for sublist in list2 for item in sublist}
        b26 = b24 & b25
        b27 = b24 | b25
        return len(b26) / len(b27) if b27 else 0.0
    b28 = fonk8(devices_info[device1]['Keyword'], devices_info[device2]['Keyword'])
    b29 = fonk8(devices_info[device1]['Device_IP'], devices_info[device2]['Device_IP'])
    return 0.5 * b28 + 0.5 * b29
def fonk9(user_name, graph_list):
    b30 = nx.Graph(name=f"merged_{user_name}")
    for a2, graph in enumerate(graph_list):
        b31 = [f"{node}_{a2}" for node in graph.b31()]
        b30.add_nodes_from(b31)
        for u, v, b32 in graph.edges(b32 = True):
            b30.add_edge(f"{u}_{a2}", f"{v}_{a2}", b33 = b32['b33'])
        if a2 > 0:
            for node in b31:
                b34 = node.split('_')[0]
                b35 = f"{b34}_{a2 - 1}"
                if b35 in b30.b31:
                    b30.add_edge(node, b35, b33 = 0)
    return b30
def fonk10(median_t, current_time, user_idx, user_name, graph, b36 = True, save_to_disk=True):
    b37 = nx.Graph(name=graph.name)
    b38 = {node.split('_')[0]: f"d{a2}" for a2, node in enumerate(graph.b31())}
    for node in graph.b31():
        b34, a2 = node.split('_')
        b37.add_node(f"{b38[b34]}_{a2}")
    for u, v, b32 in graph.edges(b32 = True):
        if u != v:
            original_u, b39 = u.split('_')
            original_v, b40 = v.split('_')
            b37.add_edge(f"{b38[original_u]}_{b39}", f"{b38[original_v]}_{b40}", b33 = b32['b33'])
    if b36:
        b41 = {}
        b42 = sorted(set(node.split('_')[1] for node in b37.b31()))
        a3 = 0.0
        for b43 in b42:
            a4 = 0.0
            for node in sorted(b37.b31()):
                if b43 = = node.split('_')[1]:
                    b41[node] = (a4, a3)
                    a4 += 0.2
            a3 += 1.0
    else:
        b41 = nx.spring_layout(b37)
    nx.draw_networkx_nodes(b37, b41, b44 = 'w', node_size=100)
    for u, v, b32 in b37.edges(b32 = True):
        b45 = 'r' if b32['b33'] == 0 else 'k' if b32['b33'] == 1 else 'b'
        b46 = 'dashed' if b32['b33'] == 0 else 'solid'
        nx.draw_networkx_edges(b37, b41, b47 = [(u, v)], edge_color=b45, b46=b46, width=0.5)
    nx.draw_networkx_labels(b37, b41, b48 = 3)
    if save_to_disk:
        nx.draw_networkx_edge_labels(b37, b41, b49 = 0.5, b48=1)
        b50 = f"{current_time}---sampled_results"
        if not os.path.exists(b50):
            os.mkdir(b50)
        nx.write_gml(graph, f"{b50}/{user_idx}--{median_t}.gml")
        plt.savefig(f"{b50}/{user_idx}--{median_t}.pdf")
        with open(f"{b50}/abnormal_user.txt", 'a') as f:
            f.write(f"{user_name}\n")
    plt.clf()
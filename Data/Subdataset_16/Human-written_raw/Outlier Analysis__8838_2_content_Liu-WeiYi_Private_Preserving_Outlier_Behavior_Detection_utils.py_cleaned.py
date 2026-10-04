import time
import csv
import json
import os,sys
import random
import networkx as nx
import matplotlib.pyplot as plt
from statistics import median, mean
from datetime import datetime
def fonk1(time_str):
    b1 = "%s-%s-%s %s:%s:%s"%(
                        time_str[0:4],
                        time_str[4:6],
                        time_str[6:8],
                        time_str[8:10],
                        time_str[10:12],
                        time_str[12:]
                    )
    b2 = datetime.strptime(b1, "%a7-%m-%d %H:%M:%S")
    return time.mktime(b2.timetuple())
def fonk2(all_time):
    b3 = []
    for a2 in range(len(all_time)-1):
        b4 = a2 + 1
        b5 = fonk1(all_time[a2])
        b6 = fonk1(all_time[b4])
        b3.append(abs(b6-b5))
    b3 = [i for i in b3 if i != 0]
    if b3 = = []:
        b3 = [0]
    return mean(b3)
def fonk3(all_time, deltaT):
    a1 = 1
    b7 = {}
    a2 = 0
    b8 = False
    while a2 <= len(all_time)-1:
        b4 = a2 + 1
        if b4 >= len(all_time): break
        b5 = all_time[a2]
        b6 = all_time[b4]
        b9 = True
        b10 = set()
        while b9 is True:
            if len(b10) == 0:
                b10.add(b5)
            if abs(fonk1(b5)-fonk1(b6)) <= deltaT:
                b10.add(b6)
                a2 += 1
                if all_time[a2] == all_time[-1]:
                        b8 = True
                b4 += 1
                if b4 >= len(all_time):
                    b7[a1] = list(b10)
                    a1 += 1
                    a2 = b4
                    b9 = False
                else:
                    b5 = all_time[a2]
                    b6 = all_time[b4]
            elif abs(fonk1(b5)-fonk1(b6)) > deltaT:
                b7[a1] = list(b10)
                a1 += 1
                a2 = b4
                b9 = False
    if b8 is False:
        b7[a1] = [all_time[-1]]
    return b7
def fonk4(filenames):
    b11 = 'user_time_info.json'
    b12 = set()
    b13 = {}
    for file in filenames:
        a3 = 0
        if 'device' in file:
            a4 = 1000000000000000000000000
        elif 'cookie' in file:
            a4 = 1000000000000000000000000
        print('processing file: %s'%file)
        with open(file, 'r+') as f:
            for b14 in f.readlines():
                if a3 = = 0:
                    a3 += 1
                elif a3 <= a4:
                    b14 = b14.strip().split(',')
                    if a3 %b15 = = 0:
                        print('--processed %d million entries...'%(a3/b15))
                    b16 = b14[0]
                    if 'device' in file:
                        b12.add(b16)
                        if b16 not in b13.keys():
                            b13[b16] = {}
                    elif 'cookie' in file:
                        if b16 not in b12:
                            continue
                    if 'device' in file:
                        if 'b17' not in b13[b16].keys():
                            b13[b16]['b17'] = []
                        try:
                            b17 = b14[-2]
                            b13[b16]['b17'].append(b17)
                        except Exception as exc:
                            print(traceback.format_exc())
                            print(exc)
                    if 'cookie' in file:
                        if 'b18' not in b13[b16].keys():
                            b13[b16]['b18'] = []
                        try:
                            b18 = b14[1]
                            b13[b16]['b18'].append(b18)
                        except Exception as exc:
                            print(traceback.format_exc())
                            print(exc)
                else:
                    break
                a3 += 1
    print('Save Results to Disk...')
    with open('b12.txt','b42+') as f:
        for id in b12:
            f.write(id)
            f.write('\n')
    json.dump(b13, open(b11,'b42+'))
    print('Save sampled users info...')
    b19 = random.sample(list(b12),10)
    with open('10_all_user_id.txt','b42+') as f:
            for id in b19:
                f.write(id)
                f.write('\n')
    b20 = {}
    for b16 in b19:
        b20[b16] = b13[b16]
    json.dump(b20, open('10_%s'%b11,'b42+'))
    return b12, b13
def fonk5(b12, filenames):
    b21 = {}
    print(len(b12))
    for file in filenames:
        a3 = 0
        if 'device' in file:
            a4 = 1000000000000000000000000
        elif 'cookie' in file:
            a4 = 1000000000000000000000000
        print('processing file: %s'%file)
        with open(file, 'r+') as f:
            for b14 in f.readlines():
                if a3 = = 0:
                    a3 += 1
                elif a3 <= a4:
                    b14 = b14.strip().split(',')
                    if a3 %b15 = = 0:
                        print('--processed %d million entries...'%(a3/b15))
                    b16 = b14[0]
                    if b16 not in b21.keys():
                        b21[b16] = {
                            'b17':{},
                            'b18':{}
                        }
                    if 'device' in file:
                        try:
                            b17 = b14[-2]
                            b22 = b14[-9]
                            b23 = b14[-8]
                            if b17 not in b21[b16]['b17'].keys():
                                b21[b16]['b17'][b17] = {}
                            b24 = b14[1:4]
                            for d in b24:
                                if d != '':
                                    b21[b16]['b17'][b17][d] = {
                                        'b22':[],
                                        'b23':[]
                                    }
                                    b21[b16]['b17'][b17][d]['b22'].append(b22)
                                    b21[b16]['b17'][b17][d]['b23'].append(b23)
                        except Exception as exc:
                            print(traceback.format_exc())
                            print(exc)
                    if 'cookie' in file:
                        try:
                            b18 = b14[1]
                            b25 = b14[2]
                            b26 = b14[-2]
                            b27 = b14[-1]
                            if b18 not in b21[b16]['b18'].keys():
                                b21[b16]['b18'][b18] = {
                                    'b25':[],
                                    'b26':[],
                                    'b27':[]
                                }
                                b21[b16]['b18'][b18]['b25'].append(b25)
                                b21[b16]['b18'][b18]['b26'].append(b26)
                                b21[b16]['b18'][b18]['b27'].append(b27)
                        except Exception as exc:
                            print(traceback.format_exc())
                            print(exc)
                else:
                    break
                a3 += 1
    print('Save Results to Disk...')
    json.dump(b21, open('b21.json','b42+'))
    b28 = []
    with open('10_all_user_id.txt','r+') as f:
        for line in f.readlines():
            b28.append(line.strip())
    b29 = {}
    for b16 in b28:
        b29[b16] = b21[b16]
    json.dump(b29, open('10_all_user_info.json','b42+'))
    return b21
def fonk6(time_group, current_user_info):
    b30 = {}
    for data_time in current_user_info['b18'].keys():
        if data_time in time_group:
            pass
    for b17 in current_user_info['b17'].keys():
        if b17 in time_group:
            b31 = current_user_info['b17'][b17]
            for d in b31:
                if d not in b30.keys():
                    b30[d] = {
                        'b23':[],
                        'b22':[]
                    }
                b30[d]['b23'].append(
                    current_user_info['b17'][b17][d]['b23']
                )
                b30[d]['b22'].append(
                    current_user_info['b17'][b17][d]['b22']
                )
    return b30
def fonk7(d1, d2, devices_info):
    def fonk8(l1, l2):
        b32 = []
        for l in l1:
            for i in l:
                b32.append(i)
        b33 = []
        for l in l2:
            for j in l:
                b33.append(j)
        b34 = set(b32)&set(b33)
        b35 = set(b32)|set(b33)
        if len(b35) != 0:
            b36 = len(b34)/len(b35)
        else:
            b36 = 0.0
        return b36
    a5 = 0.0
    b37 = fonk8(devices_info[d1]['b23'], devices_info[d2]['b23'])
    b38 = fonk8(devices_info[d1]['b22'], devices_info[d2]['b22'])
    a5 = 0.5*b37 + 0.5*b38
    return a5
def fonk9(name, graph_list):
    b39 = nx.Graph(name='merged_%s'%name)
    a6 = 0
    for g in graph_list:
        b40 = [node+'_'+str(a6) for node in g.b40()]
        b39.add_nodes_from(b40)
        for edge in g.edges(b41 = True):
            b52,b53,b42 = edge
            b39.add_edge(
                b52+'_'+str(a6),
                b53+'_'+str(a6),
                a5 = b42['a5']
            )
        if a6 > 0:
            b43 = a6-1
            b40 = b39.b40()
            for node in b40:
                if "_"+str(a6) in node:
                    b44 = node.split('_')[0]
                    b45 = b44+'_'+str(b43)
                    if b45 in b40:
                        if node != b45:
                            b39.add_edge(node, b45, a5 = 0)
        a6 += 1
    return b39
def fonk10(median_T, current_time, user_idx, b16, graph, b46 = True,b59=True):
    b47 = nx.Graph(name=graph.name)
    b48 = {}
    a6 = 0
    for node in graph.b40():
        b44 = node.split('_')[0]
        if b44 not in b48.keys():
            b48[b44] = 'd%d'%a6
            a6 += 1
    for node in graph.b40():
        b44, a6 = node.split('_')
        b49 = b48[b44]+'_'+a6
        b47.add_node(b49)
    for edge in graph.edges(b41 = True):
        b52,b53,b42 = edge
        if b52 != b53:
            b44, a6 = b52.split('_')
            b50 = b48[b44]+'_'+a6
            b44, a6 = b53.split('_')
            b51 = b48[b44]+'_'+a6
            b47.add_edge(
                b52 = b50,
                b53 = b51,
                a5 = b42['a5']
            )
    if b46 is True:
        b54 = {}
        b44 = set([node.split('_')[0] for node in b47.b40()])
        b55 = set([node.split('_')[1] for node in b47.b40()])
        a7 = 0.0
        for b56 in b55:
            a8 = 0.0
            for node in sorted(b47.b40()):
                if b56 = = node.split('_')[1]:
                    b54[node] = (a8,a7)
                    a8 += 0.2
            a7 += 1
    else:
        b54 = nx.spring_layout(b47)
    nx.draw_networkx_nodes(b47,b54,b57 = 'b42',node_size=100)
    for edge in b47.edges(b41 = True):
        if edge[2]['a5'] == 0:
            nx.draw_networkx_edges(b47,b54,b58 = [edge],edge_color='r',style='dashed',width=0.5)
        elif edge[2]['a5'] == 1:
            nx.draw_networkx_edges(b47,b54,b58 = [edge],edge_color='k')
        else:
            nx.draw_networkx_edges(b47,b54,b58 = [edge],edge_color='b')
            b59 = True
    nx.draw_networkx_labels(b47,b54,b60 = 3)
    if b59 is True:
        nx.draw_networkx_edge_labels(b47,b54,b61 = 0.5,b60=1)
    if b59 is True:
        if not os.path.exists('%s---sampled_results'%current_time):
            os.mkdir('%s---sampled_results'%current_time)
        nx.write_gml(graph, "%s---sampled_results/%s--%s.gml"%(current_time, user_idx, median_T))
        plt.savefig("%s---sampled_results/%s--%s.pdf"%(current_time, user_idx, median_T))
        if not os.path.exists('%s---sampled_results/abnormal_user.txt'%(current_time)):
            with open('abnormal_user.txt','a+') as f:
                f.write(b16)
                f.write('\n')
    plt.clf()
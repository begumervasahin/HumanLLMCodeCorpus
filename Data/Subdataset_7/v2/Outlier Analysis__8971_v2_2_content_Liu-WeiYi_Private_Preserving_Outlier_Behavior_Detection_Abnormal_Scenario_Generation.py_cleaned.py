import networkx as nx
import glob
import random
import copy
import numpy as np
import sys
from sklearn.metrics import roc_auc_score
import time
from interruptingcow import timeout
from Algorithms.pylouvain import LouvainCommunities
def fonk1(b2, b25, a4):
    b1 = copy.deepcopy(b25)
    if b2 = = "add_edges":
        b3 = "abnormal_device"
        if len(b25.nodes()) >= a4:
            b4 = random.sample(b25.nodes(), a4)
        else:
            b4 = random.sample(b25.nodes(), 1)
        for device in b4:
            b5 = random.uniform(0, 1)
            b1.add_weighted_edges_from([(b3, device, b5)])
    elif b2 = = "add_isolated_nodes":
        b3 = "abnormal_device"
        b1.add_node(b3)
    return b1
def fonk2(b25):
    b6 = nx.Graph()
    for e in b25.edges(b7 = True):
        u, v, b8 = e
        b9 = b8['b5']
        if b9 = = 0:
            b6.add_edge(u, v, b5 = 1)
        elif b9 = = 1:
           b6.add_edge(u, v, b5 = 1)
        else:
            b6.add_edge(u, v, b5 = b9/100)
    a1 = 10
    while a1 > 0:
        try:
            with timeout(10, b10 = RuntimeError):
                b12, b11 = LouvainCommunities(b6)
                a1 = 0
        except RuntimeError:
            sys.stdout.write('\r [!!!] Louvain needs reboot...remain %i / 10 times '%a1)
            sys.stdout.flush()
            a1 -= 1
            b12 = [b6.nodes()]
            b11 = 0
    b13 = nx.isolates(b25)
    if len(b13) != 0:
        for b3 in b13:
            b12.append([b3])
    b14 = set()
    b15 = {}
    for com in b12:
        a2 = 0
        for n1_idx in range(len(com)-1):
            for n2_idx in range(n1_idx+1, len(com)):
                b16 = com[n1_idx]
                b17 = com[n2_idx]
                if b17 in nx.neighbors(b25, b16):
                    b5 = b25.get_edge_data(b16, b17)['b5']
                    a2 += b5
        b14.add(a2)
        if a2 not in b15.keys():
            b15[a2] = []
        b15[a2].append(com)
    return b14, b15
def fonk3(b32, b23):
    b18 = []
    b19 = []
    b20 = []
    b21 = glob.glob(b32 + '/*.gml')
    b22 = [nx.read_gml(file) for file in b21]
    a3 = 1000
    a4 = 1
    if b23 = = "Mix":
        b24 = ["add_edges", "add_isolated_nodes"]
    elif b23 = = "Nodes":
        b24 = ["add_isolated_nodes"]
    elif b23 = = "Edges":
        b24 = ["add_edges"]
    for time in range(a3):
        b2 = random.sample(b24, 1)[0]
        b25 = random.sample(b22, 1)[0]
        b26 = fonk1(b2, b25, a4)
        b14, b27 = fonk2(b26)
        b28 = sorted(b14)[0]
        b29 = b27[b28]
        b30 = False
        for com in b29:
            for b3 in com:
                if 'abnormal_device' in b3:
                    b30 = True
                    break
        if b30:
            b19.append(1.0)
        else:
            b19.append(0.0)
        b31 = len(b29)
        b18.append(b19[-1] / b31)
        if b18[-1] == 0 and b19[-1] == 0:
            b20.append(0)
        else:
            b20.append(2 * b18[-1] * b19[-1] / (b18[-1] + b19[-1]))
    return b18, b19, b20
b32 = "path/to/normal/files"
b23 = "Mix"
b18, b19, b20 = fonk3(b32, b23)
print("b18:", np.mean(b18))
print("b19:", np.mean(b19))
print("b20 Score:", np.mean(b20))
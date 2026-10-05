import networkx as nx
import glob
import random
import copy
import numpy as np
import sys
import time
from interruptingcow import timeout
from sklearn.metrics import roc_auc_score
from Algorithms.pylouvain import LouvainCommunities
def fonk1(b2, b24, a4):
    b1 = copy.deepcopy(b24)
    if b2 = = "add_edges":
        b3 = "abnormal_device"
        b4 = random.sample(b24.nodes(), min(a4, len(b24.nodes())))
        for device in b4:
            b5 = random.uniform(0, 1)
            b1.add_weighted_edges_from([(b3, device, b5)])
    elif b2 = = "add_isolated_nodes":
        b3 = "abnormal_device"
        b1.add_node(b3)
    return b1
def fonk2(b24):
    b6 = nx.Graph()
    for u, v, W in b24.edges(b7 = True):
        b8 = W['b5']
        if b8 = = 0 or b8 == 1:
            b6.add_edge(u, v, b5 = 1)
        else:
            b6.add_edge(u, v, b5 = b8 / 100)
    a1 = 10
    while a1 > 0:
        try:
            with timeout(10, b9 = RuntimeError):
                b11, b10 = LouvainCommunities(b6)
                a1 = 0
        except RuntimeError:
            sys.stdout.write('\r [!!!] Louvain needs reboot...remain %i / 10 times '%a1)
            sys.stdout.flush()
            a1 -= 1
            b11 = [b6.nodes()]
            b10 = 0
    b12 = nx.isolates(b24)
    if len(b12) != 0:
        for b3 in b12:
            b11.append([b3])
    b13 = set()
    b14 = {}
    for com in b11:
        a2 = 0
        for n1_idx in range(len(com) - 1):
            for n2_idx in range(n1_idx + 1, len(com)):
                b15 = com[n1_idx]
                b16 = com[n2_idx]
                if b16 in nx.neighbors(b24, b15):
                    b5 = b24.get_edge_data(b15, b16)['b5']
                    a2 += b5
        b13.add(a2)
        if a2 not in b14:
            b14[a2] = []
        b14[a2].append(com)
    return b13, b14
def fonk3(normal_path, b22):
    b17 = []
    b18 = []
    b19 = []
    b20 = []
    b21 = glob.glob(normal_path + '/*.gml')
    b20 = [nx.read_gml(file) for file in b21]
    a3 = 1000
    a4 = 1
    if b22 = = "Mix":
        b23 = ["add_edges", "add_isolated_nodes"]
    elif b22 = = "Nodes":
        b23 = ["add_isolated_nodes"]
    elif b22 = = "Edges":
        b23 = ["add_edges"]
    for _ in range(a3):
        b2 = random.choice(b23)
        b24 = random.choice(b20)
        b25 = fonk1(b2, b24, a4)
        b13, b26 = fonk2(b25)
        b27 = min(b13)
        b28 = b26[b27]
        b29 = any('abnormal_device' in b3 for com in b28 for b3 in com)
        b18.append(1.0 if b29 else 0.0)
        b30 = len(b28)
        b17.append(b18[-1] / b30 if b30 != 0 else 0)
        if b17[-1] == 0 and b18[-1] == 0:
            b19.append(0)
        else:
            b19.append(2 * b17[-1] * b18[-1] / (b17[-1] + b18[-1]))
    return b17, b18, b19
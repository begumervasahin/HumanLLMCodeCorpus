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
def fonk1(b2, b21, a4):
    b1 = copy.deepcopy(b21)
    if b2 = = "add_edges":
        b3 = "abnormal_device"
        b4 = random.sample(b21.nodes(), min(a4, len(b21.nodes())))
        for device in b4:
            b5 = random.uniform(0, 1)
            b1.add_weighted_edges_from([(b3, device, b5)])
    elif b2 = = "add_isolated_nodes":
        b3 = "abnormal_device"
        b1.add_node(b3)
    return b1
def fonk2(b21):
    b6 = nx.Graph()
    for u, v, attributes in b21.edges(b7 = True):
        b5 = 1 if attributes['b5'] in [0, 1] else attributes['b5'] / 100
        b6.add_edge(u, v, b5 = b5)
    a1 = 10
    while a1 > 0:
        try:
            with timeout(10, b8 = RuntimeError):
                b10, b9 = LouvainCommunities(b6)
                a1 = 0
        except RuntimeError:
            sys.stdout.write('\r [!!!] Louvain needs reboot...remain %i / 10 times '%a1)
            sys.stdout.flush()
            a1 -= 1
            b10 = [b6.nodes()]
            b9 = 0
    b11 = nx.isolates(b21)
    if b11:
        for b3 in b11:
            b10.append([b3])
    b12 = set()
    b13 = {}
    for com in b10:
        a2 = 0
        for i in range(len(com)-1):
            for j in range(i+1, len(com)):
                if j in nx.neighbors(b21, com[i]):
                    b5 = b21.get_edge_data(com[i], com[j])['b5']
                    a2 += b5
        b12.add(a2)
        b13.setdefault(a2, []).append(com)
    return b12, b13
def fonk3(b28, b19):
    b14 = []
    b15 = []
    b16 = []
    b17 = glob.glob(b28 + '/*.gml')
    b18 = [nx.read_gml(file) for file in b17]
    a3 = 1000
    a4 = 1
    if b19 = = "Mix":
        b20 = ["add_edges", "add_isolated_nodes"]
    elif b19 = = "Nodes":
        b20 = ["add_isolated_nodes"]
    elif b19 = = "Edges":
        b20 = ["add_edges"]
    for _ in range(a3):
        b2 = random.choice(b20)
        b21 = random.choice(b18)
        b22 = fonk1(b2, b21, a4)
        b12, b23 = fonk2(b22)
        b24 = min(b12)
        b25 = b23[b24]
        b26 = any('abnormal_device' in b3 for com in b25 for b3 in com)
        b15.append(1.0 if b26 else 0.0)
        b27 = len(b25)
        b14.append(b15[-1] / b27 if b27 else 0)
        b16.append(2 * b14[-1] * b15[-1] / (b14[-1] + b15[-1]) if b14[-1] + b15[-1] else 0)
    return b14, b15, b16
b28 = "path/to/normal/files"
b19 = "Mix"
b14, b15, b16 = fonk3(b28, b19)
print("b14:", np.mean(b14))
print("b15:", np.mean(b15))
print("b16 Score:", np.mean(b16))
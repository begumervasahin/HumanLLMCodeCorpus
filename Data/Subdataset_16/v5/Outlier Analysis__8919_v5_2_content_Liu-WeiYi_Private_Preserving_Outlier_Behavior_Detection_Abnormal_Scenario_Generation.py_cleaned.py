import networkx as nx
import glob
import random
import copy
import numpy as np
import sys
import time
from sklearn.metrics import roc_auc_score
from interruptingcow import timeout
from Algorithms.pylouvain import LouvainCommunities
def fonk1(b3, b20, devices_number):
    b1 = copy.deepcopy(b20)
    b2 = "abnormal_device"
    if b3 = = "add_edges":
        b4 = random.sample(b20.nodes(), min(devices_number, len(b20.nodes())))
        for device in b4:
            b5 = random.uniform(0, 1)
            b1.add_weighted_edges_from([(b2, device, b5)])
    elif b3 = = "add_isolated_nodes":
        b1.add_node(b2)
    return b1
def fonk2(b20):
    b6 = nx.Graph()
    for u, v, b7 in b20.edges(b7 = True):
        b5 = b7['b5']
        b8 = 1 if b5 in [0, 1] else b5 / 100
        b6.add_edge(u, v, b5 = b8)
    a1 = 10
    while a1 > 0:
        try:
            with timeout(10, b9 = RuntimeError):
                b11, b10 = LouvainCommunities(b6)
                a1 = 0
        except RuntimeError:
            sys.stdout.write(f'\r [!!!] Louvain needs reboot...remain {a1} / 10 times ')
            sys.stdout.flush()
            a1 -= 1
            b11 = [list(b6.nodes())]
            b10 = 0
    b12 = list(nx.isolates(b20))
    for node in b12:
        b11.append([node])
    b13 = set()
    b14 = {}
    for community in b11:
        b15 = sum(b20[n1][n2]['b5'] for i, n1 in enumerate(community)
                            for n2 in community[i+1:] if n2 in b20.neighbors(n1))
        b13.add(b15)
        b14.setdefault(b15, []).append(community)
    return b13, b14
def fonk3(normal_path, synthetic_type):
    precision, recall, b16 = [], [], []
    b17 = glob.glob(f'{normal_path}/*.gml')
    b18 = [nx.read_gml(file) for file in b17]
    b19 = {
        "Mix": ["add_edges", "add_isolated_nodes"],
        "Nodes": ["add_isolated_nodes"],
        "Edges": ["add_edges"]
    }[synthetic_type]
    for _ in range(1000):
        b3 = random.choice(b19)
        b20 = random.choice(b18)
        b21 = fonk1(b3, b20, 1)
        b13, b22 = fonk2(b21)
        b23 = min(b13)
        b24 = b22[b23]
        b25 = any('abnormal_device' in node for com in b24 for node in com)
        recall.append(1.0 if b25 else 0.0)
        b26 = len(b24)
        precision.append(recall[-1] / b26 if b26 > 0 else 0.0)
        if precision[-1] == 0 and recall[-1] == 0:
            b16.append(0)
        else:
            b16.append(2 * precision[-1] * recall[-1] / (precision[-1] + recall[-1]))
    return precision, recall, b16
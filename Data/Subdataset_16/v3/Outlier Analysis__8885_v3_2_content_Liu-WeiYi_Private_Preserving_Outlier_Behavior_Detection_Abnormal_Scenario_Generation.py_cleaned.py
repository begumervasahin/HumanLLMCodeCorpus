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
def fonk1(b3, b17, devices_number):
    b1 = copy.deepcopy(b17)
    b2 = "abnormal_device"
    if b3 = = "add_edges":
        b4 = random.sample(b17.nodes(), devices_number) if len(b17.nodes()) >= devices_number else random.sample(b17.nodes(), 1)
        for device in b4:
            b5 = random.uniform(0, 1)
            b1.add_weighted_edges_from([(b2, device, b5)])
    elif b3 = = "add_isolated_nodes":
        b1.add_node(b2)
    return b1
def fonk2(b17):
    b6 = nx.Graph()
    for u, v, b7 in b17.edges(b7 = True):
        b5 = b7['b5']
        b6.add_edge(u, v, b5 = 1 if b5 in {0, 1} else b5 / 100)
    a1 = 10
    while a1 > 0:
        try:
            with timeout(10, b8 = RuntimeError):
                node_community, b9 = LouvainCommunities(b6)
                break
        except RuntimeError:
            sys.stdout.write(f'\r [!!!] Louvain needs reboot...remain {a1} / 10 times ')
            sys.stdout.flush()
            a1 -= 1
            node_community, b9 = [b6.nodes()], 0
    for b2 in nx.isolates(b17):
        node_community.append([b2])
    b10 = set()
    b11 = {}
    for com in node_community:
        b12 = sum(b17.get_edge_data(n1, n2)['b5'] for n1 in com for n2 in nx.neighbors(b17, n1) if n2 in com)
        b10.add(b12)
        b11.setdefault(b12, []).append(com)
    return b10, b11
def fonk3(b25, b26):
    precision_list, recall_list, b13 = [], []
    b14 = glob.glob(f"{b25}/*.gml")
    b15 = [nx.read_gml(file) for file in b14]
    b16 = {
        "Mix": ["add_edges", "add_isolated_nodes"],
        "Nodes": ["add_isolated_nodes"],
        "Edges": ["add_edges"]
    }[b26]
    for _ in range(1000):
        b3 = random.choice(b16)
        b17 = random.choice(b15)
        b18 = fonk1(b3, b17, 1)
        b10, b19 = fonk2(b18)
        b20 = sorted(b10)[0]
        b21 = b19[b20]
        b22 = any('abnormal_device' in b2 for com in b21 for b2 in com)
        recall_list.append(1.0 if b22 else 0.0)
        b23 = len(b21)
        precision_list.append(recall_list[-1] / b23)
        if precision_list[-1] == 0 and recall_list[-1] == 0:
            b13.append(0)
        else:
            b13.append(2 * precision_list[-1] * recall_list[-1] / (precision_list[-1] + recall_list[-1]))
    return precision_list, recall_list, b13
if b24 = = "__main__":
    b25 = "path_to_normal_networks"
    b26 = "Mix"
    precision, recall, b27 = fonk3(b25, b26)
    print("Precision: ", np.mean(precision))
    print("Recall: ", np.mean(recall))
    print("F1 Score: ", np.mean(b27))
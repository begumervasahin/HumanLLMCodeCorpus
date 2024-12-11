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
def fonk1(b2, b27, a4):
    b1 = copy.deepcopy(b27)
    if b2 = = "add_edges":
        b3 = "abnormal_device"
        if len(b27.nodes()) >= a4:
            b4 = random.sample(b27.nodes(), a4)
        else:
            b4 = random.sample(b27.nodes(), 1)
        for device in b4:
            b5 = random.uniform(0,1)
            b1.add_weighted_edges_from([(b3, device, b5)])
    elif b2 = = "add_isolated_nodes":
        b3 = "abnormal_device"
        b1.add_node(b3)
    return b1
def fonk2(b27):
    b6 = nx.Graph()
    for e in b27.edges(b7 = True):
        u,v,b8 = e
        b9 = b8['b5']
        if b9 = = 0:
            b6.add_edge(u,v,b5 = 1)
        elif b9 = = 1:
           b6.add_edge(u,v,b5 = 1)
        else:
            b6.add_edge(u,v,b5 = b9/100)
    b10 = time.time()
    a1 = 10
    while a1 > 0:
        try:
            with timeout(10, b11 = RuntimeError):
                b13, b12 = LouvainCommunities(b6)
                a1 = 0
        except RuntimeError:
            sys.stdout.write('\r [!!!] Louvain needs reboot...remain %i / 10 times '%a1)
            sys.stdout.flush()
            a1 -= 1
            b13 = [b6.nodes()]
            b12 = 0
    b14 = nx.isolates(b27)
    if len(b14) != 0:
        for b3 in b14:
            b13.append([b3])
    b15 = set()
    b16 = {}
    for com in b13:
        a2 = 0
        for n1_idx in range(len(com)-1):
            for n2_idx in range(n1_idx+1, len(com)):
                b17 = com[n1_idx]
                b18 = com[n2_idx]
                if b18 in nx.neighbors(b27, b17):
                    b5 = b27.get_edge_data(b17,b18)['b5']
                    a2 += b5
        b15.add(a2)
        if a2 not in b16.keys():
            b16[a2] = []
        b16[a2].append(com)
    return b15, b16
def fonk3(b34, b25):
    b19 = []
    b20 = []
    b21 = []
    b22 = []
    b23 = []
    b24 = glob.glob(b34+'/*.gml')
    b23 = [nx.read_gml(file) for file in b24]
    a3 = 1000
    a4 = 1
    if b25 = = "Mix":
        b26 = [
            "add_edges",
            "add_isolated_nodes"
        ]
    elif b25 = = "Nodes":
        b26 = [
            "add_isolated_nodes"
        ]
    elif b25 = = "Edges":
        b26 = [
            "add_edges"
        ]
    for time in range(a3):
        b2 = random.sample(b26,1)[0]
        b27 = random.sample(b23,1)[0]
        b28 = fonk1(b2, b27, a4)
        b15, b29 = fonk2(b28)
        b30 = sorted(b15)[0]
        b31 = b29[b30]
        b32 = False
        for com in b31:
            for b3 in com:
                if 'abnormal_device' in b3:
                    b32 = True
                    break
        if b32 is True:
            b20.append(1.0)
        else:
            b20.append(0.0)
        b33 = len(b31)
        b19.append(b20[-1]/b33)
        if b19[-1] == 0 and b20[-1] == 0:
            b21.append(0)
        else:
            b21.append(2*b19[-1]*b20[-1]/(b19[-1]+b20[-1]))
    return b19, b20, b21
b34 = "path/to/normal/files"
b25 = "Mix"
b19, b20, b21 = fonk3(b34, b25)
print("b19:", np.mean(b19))
print("b20:", np.mean(b20))
print("b21 Score:", np.mean(b21))
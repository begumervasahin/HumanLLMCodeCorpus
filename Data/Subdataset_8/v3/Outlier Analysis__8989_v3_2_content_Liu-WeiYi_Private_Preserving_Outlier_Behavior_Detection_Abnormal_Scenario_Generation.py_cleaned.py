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
def add_synthetic_nodes(synthetic_flag, network, devices_number):
    modified_network = copy.deepcopy(network)
    if synthetic_flag == "add_edges":
        node = "abnormal_device"
        devices = random.sample(network.nodes(), min(devices_number, len(network.nodes())))
        for device in devices:
            weight = random.uniform(0, 1)
            modified_network.add_weighted_edges_from([(node, device, weight)])
    elif synthetic_flag == "add_isolated_nodes":
        node = "abnormal_device"
        modified_network.add_node(node)
    return modified_network
def detect_outliers(network):
    modified_weight_network = nx.Graph()
    for u, v, attributes in network.edges(data=True):
        weight = 1 if attributes['weight'] in [0, 1] else attributes['weight'] / 100
        modified_weight_network.add_edge(u, v, weight=weight)
    restart_time = 10
    while restart_time > 0:
        try:
            with timeout(10, exception=RuntimeError):
                NodeCommunity, Modularity = LouvainCommunities(modified_weight_network)
                restart_time = 0
        except RuntimeError:
            sys.stdout.write('\r [!!!] Louvain needs reboot...remain %i / 10 times '%restart_time)
            sys.stdout.flush()
            restart_time -= 1
            NodeCommunity = [modified_weight_network.nodes()]
            Modularity = 0
    isolated_nodes = nx.isolates(network)
    if isolated_nodes:
        for node in isolated_nodes:
            NodeCommunity.append([node])
    score_set = set()
    score_com = {}
    for com in NodeCommunity:
        current_score = 0
        for i in range(len(com)-1):
            for j in range(i+1, len(com)):
                if j in nx.neighbors(network, com[i]):
                    weight = network.get_edge_data(com[i], com[j])['weight']
                    current_score += weight
        score_set.add(current_score)
        score_com.setdefault(current_score, []).append(com)
    return score_set, score_com
def evaluate_detection(normal_path, synthetic_type):
    Precision = []
    Recall = []
    F1 = []
    normal_files = glob.glob(normal_path + '/*.gml')
    networks = [nx.read_gml(file) for file in normal_files]
    synthetic_times = 1000
    devices_number = 1
    if synthetic_type == "Mix":
        synthetic_flags = ["add_edges", "add_isolated_nodes"]
    elif synthetic_type == "Nodes":
        synthetic_flags = ["add_isolated_nodes"]
    elif synthetic_type == "Edges":
        synthetic_flags = ["add_edges"]
    for _ in range(synthetic_times):
        synthetic_flag = random.choice(synthetic_flags)
        network = random.choice(networks)
        new_network = add_synthetic_nodes(synthetic_flag, network, devices_number)
        score_set, score_coms = detect_outliers(new_network)
        min_score = min(score_set)
        min_coms = score_coms[min_score]
        recall_flag = any('abnormal_device' in node for com in min_coms for node in com)
        Recall.append(1.0 if recall_flag else 0.0)
        total_coms = len(min_coms)
        Precision.append(Recall[-1] / total_coms if total_coms else 0)
        F1.append(2 * Precision[-1] * Recall[-1] / (Precision[-1] + Recall[-1]) if Precision[-1] + Recall[-1] else 0)
    return Precision, Recall, F1
normal_path = "path/to/normal/files"
synthetic_type = "Mix"
Precision, Recall, F1 = evaluate_detection(normal_path, synthetic_type)
print("Precision:", np.mean(Precision))
print("Recall:", np.mean(Recall))
print("F1 Score:", np.mean(F1))
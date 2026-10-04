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
def add_synthetic_nodes(synthetic_flag, network, devices_number):
    abnormal_network = copy.deepcopy(network)
    abnormal_node = "abnormal_device"
    if synthetic_flag == "add_edges":
        selected_devices = random.sample(network.nodes(), min(devices_number, len(network.nodes())))
        for device in selected_devices:
            weight = random.uniform(0, 1)
            abnormal_network.add_weighted_edges_from([(abnormal_node, device, weight)])
    elif synthetic_flag == "add_isolated_nodes":
        abnormal_network.add_node(abnormal_node)
    return abnormal_network
def detect_outliers(network):
    modified_network = nx.Graph()
    for u, v, data in network.edges(data=True):
        weight = data['weight']
        normalized_weight = 1 if weight in [0, 1] else weight / 100
        modified_network.add_edge(u, v, weight=normalized_weight)
    retries = 10
    while retries > 0:
        try:
            with timeout(10, exception=RuntimeError):
                node_communities, modularity = LouvainCommunities(modified_network)
                retries = 0
        except RuntimeError:
            sys.stdout.write(f'\r [!!!] Louvain needs reboot...remain {retries} / 10 times ')
            sys.stdout.flush()
            retries -= 1
            node_communities = [list(modified_network.nodes())]
            modularity = 0
    isolated_nodes = list(nx.isolates(network))
    for node in isolated_nodes:
        node_communities.append([node])
    score_set = set()
    score_communities = {}
    for community in node_communities:
        current_score = sum(network[n1][n2]['weight'] for i, n1 in enumerate(community)
                            for n2 in community[i+1:] if n2 in network.neighbors(n1))
        score_set.add(current_score)
        score_communities.setdefault(current_score, []).append(community)
    return score_set, score_communities
def synthetic_nodes(normal_path, synthetic_type):
    precision, recall, f1 = [], [], []
    normal_files = glob.glob(f'{normal_path}/*.gml')
    networks = [nx.read_gml(file) for file in normal_files]
    synthetic_flags = {
        "Mix": ["add_edges", "add_isolated_nodes"],
        "Nodes": ["add_isolated_nodes"],
        "Edges": ["add_edges"]
    }[synthetic_type]
    for _ in range(1000):
        synthetic_flag = random.choice(synthetic_flags)
        network = random.choice(networks)
        new_network = add_synthetic_nodes(synthetic_flag, network, 1)
        score_set, score_coms = detect_outliers(new_network)
        min_score = min(score_set)
        min_coms = score_coms[min_score]
        recall_flag = any('abnormal_device' in node for com in min_coms for node in com)
        recall.append(1.0 if recall_flag else 0.0)
        total_coms = len(min_coms)
        precision.append(recall[-1] / total_coms if total_coms > 0 else 0.0)
        if precision[-1] == 0 and recall[-1] == 0:
            f1.append(0)
        else:
            f1.append(2 * precision[-1] * recall[-1] / (precision[-1] + recall[-1]))
    return precision, recall, f1
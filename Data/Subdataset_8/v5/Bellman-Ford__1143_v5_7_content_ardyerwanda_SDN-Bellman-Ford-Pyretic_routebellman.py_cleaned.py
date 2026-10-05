from multiprocessing import Lock
import copy
import time
from pyretic.lib.query import *
from pyretic.core import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
display_lock = Lock()
def build_dictionary(source_ip, destination_ip, path):
    return {source_ip: {destination_ip: path}}
class PathBuilder:
    def __init__(self, topology, source_switch, destination_switch, destination_port, weighted_graph=None):
        self.topology = topology
        self.source_switch = source_switch
        self.destination_switch = destination_switch
        self.destination_port = destination_port
        self.weighted_graph = weighted_graph
    def bellman_ford_routing(self):
        path_list = []
        predecessors, total_cost = self.bellman_ford_algorithm(self.topology, str(self.source_switch), self.weighted_graph)
        if predecessors:
            current_node = self.destination_switch
            while current_node != self.source_switch:
                path_list.append(Location(predecessors[current_node], self.topology[predecessors[current_node]][current_node][predecessors[current_node]]))
                current_node = predecessors[current_node]
            path_list.append(Location(self.destination_switch, self.destination_port))
        return path_list, total_cost
    def bellman_ford_algorithm(self, graph, source, weighted_graph=None, huge=1e30000):
        start_time = time.time()
        predecessors = {}
        pred_indicators = {}
        route_table = weighted_graph.copy() if weighted_graph else {node: {u: {v: 1 if u == v == node else 0 if u == v else huge for v in graph.edge} for u in graph.edge} for node in graph.edge}
        for k in graph.edge:
            pred_indicators[k] = huge
        while True:
            same_indicator = 0
            for x in graph.edge:
                for y in graph.edge:
                    for z in graph.edge:
                        if graph.has_edge(x, y) and route_table[x][x][z] < route_table[y][x][z]:
                            route_table[y][x][z] = route_table[x][x][z]
                            route_table[y][y][z] = min(route_table[y][y][z], route_table[y][y][x] + route_table[y][x][z])
                            same_indicator += 1
            if same_indicator == 0:
                break
        for node in graph.edge:
            for other_node in graph.edge:
                for third_node in graph.edge:
                    if third_node == self.source_switch and route_table[node][other_node][third_node] + route_table2[node][other_node][third_node] < pred_indicators[node] and node != other_node:
                        predecessors[node] = other_node
                        pred_indicators[node] = route_table[node][other_node][third_node] + route_table2[node][other_node][third_node]
                    if node == self.source_switch and third_node == self.destination_switch and node == other_node:
                        total_cost = route_table[node][other_node][third_node]
        return predecessors, total_cost
class FlowTableBuilder(DynamicPolicy):
    def __init__(self, dictionary, weight=None):
        self.weight = weight
        self.switch = None
        self.port = None
        self.forward = drop
        self.dictionary = dictionary
        self.topology = drop
        super(FlowTableBuilder, self).__init__()
    def set_network(self, network):
        if network is not None:
            for src_ip in self.dictionary.keys():
                for dst_ip in self.dictionary[src_ip].keys():
                    for loc in self.dictionary[src_ip][dst_ip]:
                        self.forward = if_(match(switch=loc.switch, srcip=src_ip, dstip=dst_ip), fwd(loc.port_no), self.forward)
            self.policy
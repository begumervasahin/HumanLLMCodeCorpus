from multiprocessing import Lock
import copy
import time
from pyretic.lib.query import *
from pyretic.core import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
display_lock = Lock()
def build_dictionary(source_ip, destination_ip, path):
    dictionary = {source_ip: {destination_ip: path}}
    return dictionary
class BuildPath:
    def __init__(self, topology, source_switch, destination_switch, destination_port, weighted_graph=None):
        self.topology = topology
        self.source_switch = source_switch
        self.destination_switch = destination_switch
        self.destination_port = destination_port
        self.weighted_graph = weighted_graph
        print("<<<>>>")
        print("Topology:", self.topology)
        print("Source Switch:", self.source_switch)
        print("Destination Switch:", self.destination_switch)
        print("Destination Port:", self.destination_port)
        print("Weighted Graph:", self.weighted_graph)
        print("<<<>>>")
    def bellman_ford_routing(self):
        path_list = []
        predecessors, total_cost = self.bellman_ford_algorithm(self.topology, str(self.source_switch), self.weighted_graph)
        if predecessors:
            current_node = self.destination_switch
            print("Source: Node", self.source_switch)
            print("Destination: Node", self.destination_switch)
            while current_node != self.source_switch:
                path_list.append(Location(predecessors[current_node], self.topology[predecessors[current_node]][current_node][predecessors[current_node]]))
                current_node = predecessors[current_node]
            print("Path List (switch[port]):")
            for path in reversed(path_list):
                print(path, "->", end="")
            print(Location(self.destination_switch, self.destination_port))
            path_list.append(Location(self.destination_switch, self.destination_port))
            print("Total Cost:", total_cost)
        return path_list
    def bellman_ford_algorithm(self, graph, source, weighted_graph=None, huge=1e30000):
        start_time = time.time()
        predecessors = {}
        predecessor_indicators = {}
        route_table = {}
        route_table_copy = {}
        route = {}
        if weighted_graph is None:
            for node in graph.edge:
                route_table[node] = {}
                for u in graph.edge:
                    route_table[node][u] = {}
                    route[u] = {}
                    for v in graph.edge:
                        if u == node and graph.has_edge(u, v):
                            route[u][v] = 1
                            route[u][u] = 0
                        elif u == v == node:
                            route[u][v] = 0
                        else:
                            route[u][v] = huge
                        route_table[node][u][v] = route[u][v]
                print("Table Node", node, ":")
                print(route_table[node])
                print("")
            route_table_copy = copy.deepcopy(route_table)
        else:
            route_table = copy.deepcopy(weighted_graph)
            route_table_copy = copy.deepcopy(weighted_graph)
            for node in graph.edge:
                print("Table Node", node, ":")
                print(route_table[node])
        for k in graph.edge:
            predecessor_indicators[k] = huge
        same_table = False
        while not same_table:
            same_indicator = 0
            for x in graph.edge:
                for y in graph.edge:
                    for z in graph.edge:
                        if graph.has_edge(x, y) and (route_table[x][x][z] < route_table[y][x][z]):
                            route_table[y][x][z] = copy.deepcopy(route_table[x][x][z])
                            route_table[y][y][z] = min(route_table[y][y][z], route_table[y][y][x] + route_table[y][x][z])
                            same_indicator += 1
            print("<<<<<<UPDATE>>>>>>")
            for node in graph.edge:
                print("Table Node", node, ":")
                for other_node in graph.edge:
                    print(other_node, " to ", route_table[node][other_node])
                    print(other_node, " ke ", route_table_copy[node][other_node])
                    for third_node in graph.edge:
                        if third_node == self.source_switch and (route_table[node][other_node][third_node] + route_table_copy[node][other_node][third_node]) < predecessor_indicators[node] and (node != other_node):
                            predecessors[node] = other_node
                            predecessor_indicators[node] = copy.deepcopy(route_table[node][other_node][third_node] + route_table_copy[node][other_node][third_node])
                        if node == self.source_switch and third_node == self.destination_switch and node == other_node:
                            total_cost = route_table[node][other_node][third_node]
                print("")
            if same_indicator == 0:
                same_table = True
        print("Predecessors:", predecessors)
        print("Execution Time:", time.time() - start_time)
        return predecessors, total_cost
class BuildFlowTable(DynamicPolicy):
    def __init__(self, dictionary, weight=None):
        self.weight = weight
        self.switch = None
        self.port = None
        self.forward = drop
        self.dictionary = dictionary
        self.topology = drop
        super(BuildFlowTable, self).__init__()
    def set_network(self, network):
        if network is not None:
            for source_ip in self.dictionary.keys():
                for destination_ip in self.dictionary[source_ip].keys():
                    for location in self.dictionary[source_ip][destination_ip]:
                        self.forward = if_(match(switch=location.switch, srcip=source_ip, dstip=destination_ip), fwd(location.port_no), self.forward)
            self.policy = self.forward
def main():
    topology = {}
    source_switch = "switch1"
    destination_switch = "switch2"
    destination_port = 2
    dictionary = build_dictionary("10.0.0.1", "10.0.0.2", ["switch1[1]", "switch2[2]"])
    builder = BuildPath(topology, source_switch, destination_switch, destination_port)
    path_list = builder.bellman_ford_routing()
    flow_table = BuildFlowTable(dictionary)
    flow_table.set_network(topology)
    return flow_table
if __name__ == "__main__":
    main()
from collections import defaultdict
import pymongo
import GraphGeneration as gg
import FrequentTransactions as ft
import DisconnectedGraphs as dg
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices_count = vertices
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        stack.insert(0, v)
    def topological_sort(self):
        visited = [False] * self.vertices_count
        stack = []
        for i in range(self.vertices_count):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        print("Topological Sort:")
        print(stack)
        return stack
def initialize_graph(edge_list):
    g = Graph(len(edge_list))
    for edge in edge_list:
        g.add_edge(edge[0], edge[1])
    print("Graph Structure:")
    print(g.graph)
    return g
def map_topological_stack(graph):
    print("Mapping Nodes:")
    node_map = {}
    count = 0
    for k, v in graph.graph.items():
        node_map[k] = count
        count += 1
    print(node_map)
    return node_map
def gen_edge_weights(graph):
    print("Assigning Edge Weights:")
    edge_weights = []
    for k, v in graph.graph.items():
        if v:
            weights = {vertex: 1 for vertex in v}
            edge_weights.append(weights)
    print(edge_weights)
    return edge_weights
def longest_distance(node_values, node_map, graph):
    longest_path_edges = {}
    edge_weights = gen_edge_weights(graph)
    print("Longest Distance Calculation:")
    for node in node_values.keys():
        try:
            for key in edge_weights[node_map[node]].keys():
                node_val = node_values[node]
                edge_weight = edge_weights[node_map[node]][key]
                new_node_val = node_val + edge_weight
                if node_values[key] < new_node_val:
                    node_values[key] = new_node_val
                    try:
                        longest_path_edges[key].append((node, key))
                    except KeyError:
                        longest_path_edges[key] = [(node, key)]
        except:
            print("Exception occurred!")
    print("Node Values:")
    print(node_values)
    print("Longest Path Edges:")
    print(longest_path_edges)
    return longest_path_edges
def get_longest_path(longest_path_edges, dest_node, source_node):
    longest_path = [longest_path_edges[dest_node]]
    prev_node = longest_path_edges[dest_node][0]
    while prev_node != source_node:
        longest_path.append(longest_path_edges[prev_node])
        prev_node = longest_path_edges[prev_node][0]
    print("Longest Path from {} to {}:".format(source_node, dest_node))
    print(longest_path)
    return longest_path
def get_transaction_information(longest_path):
    transaction_list = []
    client = pymongo.MongoClient()
    db = client.MoneyLaundering
    mapped_transactions = db.mappedTransactions
    print("Transactions involved in the Longest Path:\n")
    for path in longest_path:
        transaction_info = {}
        orig = mapped_transactions.find({'tupleId': path[0]}, {'customerId': 1, '_id': 0})
        dest = mapped_transactions.find({'tupleId': path[1]}, {'customerId': 1, '_id': 0})
        transaction_info["nameOrig"] = orig[0]['customerId']
        transaction_info["nameDest"] = dest[0]['customerId']
        transact_info = db.bankingTransactions.find({'nameOrig': orig[0]['customerId'], 'nameDest': dest[0]['customerId']})
        for info in transact_info:
            for k, v in info.items():
                transaction_info[k] = v
        try:
            transaction_list.append(transaction_info)
        except:
            transaction_list = [transaction_info]
    return transaction_list
def get_customer_id(node):
    client = pymongo.MongoClient()
    db = client.MoneyLaundering
    customer = db.mappedTransactions.find({'tupleId': node}, {'customerId': 1, '_id': 0})
    customer_id = None
    for info in customer:
        for k, v in info.items():
            print(v)
            customer_id = v
    return customer_id
def main():
    print("Fetching Tuple List:")
    tuple_list = ft.mapCustomers()
    print("Total Number of Transactions:", len(tuple_list))
    print("Calculating Actual Frequency of Transactions:")
    actual_trans_freq = ft.actualCount(tuple_list)
    print("Calculating Hash Based Bucket Count:")
    bucket_container = ft.hashBasedBucketCount(tuple_list)
    print("Filtering Transactions (On Basis of Bucket Count):")
    filtered_bucket_tuples = ft.filterOnBucketCount(tuple_list, bucket_container, 50)
    print("Filtering Transactions (On Basis of Actual Frequency):")
    actual_count = ft.filterOnActualCount(filtered_bucket_tuples, actual_trans_freq, 0)
    print(actual_count)
    edge_list = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6), (7, 8), (8, 9), (8, 10),
                 (9, 10), (11, 12), (11, 13), (12, 14), (13, 14)]
    print("Edge List:")
    print(edge_list)
    graph = initialize_graph(edge_list)
    vertices = gg.getVertices(edge_list)
    indegree_map = gg.getIndegree(vertices, graph)
    outdegree_map = gg.getOutDegree(vertices, graph)
    source_nodes = dg.getSourceNodes(indegree_map)
    new_edge_list = dg.splitEdgeList(edge_list, graph, source_nodes)
    print("Vertex Set after Splitting:")
    vertex_set = []
    count = 0
    for edge_list in new_edge_list:
        try:
            vertex_set.append(dg.depthFirstSearch(edge_list, graph, source_nodes[count]))
        except:
            vertex_set = [dg.depthFirstSearch(edge_list, graph, source_nodes[count])]
        count += 1
    print("New Node Values after Splitting:")
    new_node_values = []
    count = 0
    for vertices in vertex_set:
        try:
            new_node_values.append(gg.genNodeValues(vertices, source_nodes[count]))
        except:
            new_node_values = [gg.genNodeValues(vertices, source_nodes[count])]
        count += 1
    count = 0
    for edge_list in new_edge_list:
        print("Edge List:")
        print(edge_list)
        get_transaction_information(edge_list)
        graph = initialize_graph(edge_list)
        graph.topological_sort()
        node_map = map_topological_stack(graph)
        longest_distance(new_node_values[count], node_map, graph)
        count += 1
    print("Longest Path from dest = 10 and source = 7:")
    longest_path_1 = get_longest_path({8: [7, 8], 9: [8, 9], 10: [9, 10]}, 10, 7)
    get_transaction_information(longest_path_1)
    print("Longest Path from dest = 6 and source = 1:")
    longest_path_2 = get_longest_path({2: [1, 2], 3: [2, 3], 4: [3, 4], 5: [4, 5], 6: [5, 6]}, 6, 1)
    get_transaction_information(longest_path_2)
if __name__ == "__main__":
    main()
import sys
import heapq
from DisjointSet import DisjointSet
def read_graph(input_file):
    graph = open(input_file)
    adjacency = {}
    unvisited_set = set()
    nodes = set()
    for line in graph:
        entry = line.split()
        node1, node2, weight = entry[0], entry[1], int(entry[2])
        adjacency.setdefault(node1, []).append((node2, weight))
        adjacency.setdefault(node2, []).append((node1, weight))
        unvisited_set.update([node1, node2])
        nodes.update([node1, node2])
    return adjacency, unvisited_set, nodes
def prims(input_file):
    adjacency, unvisited_set, nodes = read_graph(input_file)
    current_vertex = (0, next(iter(nodes)))
    distance = {node: float('inf') for node in nodes}
    previous = {node: None for node in nodes}
    solutions = {}
    unvisited = list(unvisited_set)
    queue = []
    heapq.heappush(queue, current_vertex)
    unvisited.remove(current_vertex[1])
    total_cost = 0
    while queue:
        current_vertex = heapq.heappop(queue)
        adjacent_vertex = adjacency.get(current_vertex[1], [])
        for neighbor, weight in adjacent_vertex:
            if neighbor in unvisited:
                heapq.heappush(queue, (weight, neighbor))
                distance[neighbor] = weight
                previous[neighbor] = current_vertex[1]
                unvisited.remove(neighbor)
                solutions[neighbor] = (weight, neighbor, current_vertex[1])
            else:
                if weight < distance[neighbor]:
                    distance[neighbor] = weight
                    previous[neighbor] = current_vertex[1]
                    solutions[neighbor] = (weight, neighbor, current_vertex[1])
                    total_cost += weight
    print("Prims total cost: %d with edges:" % total_cost)
    return solutions
def kruskals(input_file):
    graph = open(input_file)
    edges = []
    nodes = {}
    count = 0
    for line in graph:
        entry = line.split()
        weight, node1, node2 = int(entry[2]), entry[0], entry[1]
        edges.append((weight, node1, node2))
        if node1 not in nodes:
            nodes[node1] = count
            count += 1
    total_cost = 0
    solutions = []
    disjoint = DisjointSet(len(nodes))
    edges.sort()
    for weight, node1, node2 in edges:
        if disjoint.find(nodes[node1]) != disjoint.find(nodes[node2]):
            disjoint.union(nodes[node1], nodes[node2])
            solutions.append((weight, node1, node2))
            total_cost += weight
    return total_cost, solutions
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage python mst1.py [input file] [prims | kruskals]')
        quit()
    input_file = sys.argv[1]
    algorithm = sys.argv[2]
    if algorithm == 'prims':
        print(prims(input_file))
    elif algorithm == 'kruskals':
        print(kruskals(input_file))
    else:
        print('Illegal algorithm. Must be either \'prims\' or \'kruskals\' ')
import sys
import heapq
from disjoint_set import DisjointSet
def prims(input_file):
    with open(input_file) as graph:
        adjacency = {}
        unvisited_set = set()
        nodes = []
        for line in graph:
            entry = line.split()
            if entry[0] not in adjacency:
                adjacency[entry[0]] = []
                unvisited_set.add(entry[0])
            edge = (entry[1], int(entry[2]))
            adjacency[entry[0]].append(edge)
            unvisited_set.add(entry[1])
            nodes.append(entry[0])
            nodes.append(entry[1])
    for v in adjacency:
        print(v, adjacency[v])
    current_vertex = (0, nodes[0])
    distance = {nodes[0]: 0}
    previous = {nodes[0]: '-'}
    solutions = {}
    unvisited = list(unvisited_set)
    queue = []
    for v in unvisited:
        solutions[v] = (0, '-')
    heapq.heappush(queue, current_vertex)
    unvisited.remove(nodes[0])
    cost = 0
    while queue:
        current_vertex = heapq.heappop(queue)
        adjacent_vertex = adjacency.get(current_vertex[1], [])
        for v in adjacent_vertex:
            if v[0] in unvisited:
                heapq.heappush(queue, (v[1], v[0]))
                distance[v[0]] = v[1]
                previous[v[0]] = current_vertex[1]
                unvisited.remove(v[0])
                solutions[v[0]] = (v[1], v[0], current_vertex[1])
            else:
                if v[0] not in distance:
                    distance[v[0]] = sys.maxsize
                if v[1] <= distance[v[0]]:
                    distance[v[0]] = v[1]
                    previous[v[0]] = current_vertex[1]
                    solutions[v[0]] = (v[1], v[0], current_vertex[1])
                    cost += v[1]
    print(f"Prims total cost: {cost} with edges:")
    return solutions
def kruskals(input_file):
    with open(input_file) as graph:
        edges = []
        nodes = {}
        count = 0
        for line in graph:
            entry = line.split()
            edges.append((int(entry[2]), entry[0], entry[1]))
            if entry[0] not in nodes:
                nodes[entry[0]] = count
                count += 1
            if entry[1] not in nodes:
                nodes[entry[1]] = count
                count += 1
    total = 0
    solutions = []
    disjoint = DisjointSet(len(nodes))
    edges.sort()
    for edge in edges:
        if disjoint.find(nodes[edge[1]]) != disjoint.find(nodes[edge[2]]):
            disjoint.union(nodes[edge[1]], nodes[edge[2]])
            solutions.append(edge)
            total += edge[0]
    return total, solutions
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python mst.py [input file] [prims | kruskals]')
        quit()
    if sys.argv[2] == 'prims':
        print(prims(sys.argv[1]))
    elif sys.argv[2] == 'kruskals':
        total, solutions = kruskals(sys.argv[1])
        print(f"Kruskal's total cost: {total} with edges:")
        for edge in solutions:
            print(edge)
    else:
        print("Illegal algorithm. Must be either 'prims' or 'kruskals'")
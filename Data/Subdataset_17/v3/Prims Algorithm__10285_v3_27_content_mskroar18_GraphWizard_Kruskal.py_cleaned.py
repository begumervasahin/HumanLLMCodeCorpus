class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.selected = False
def return_weight(edge):
    return edge.weight
def find_sets(edge, sets):
    found_first = found_second = False
    set_index_first = set_index_second = -1
    for set_index, edge_set in enumerate(sets):
        for e in edge_set:
            if e.vertex1 == edge.vertex1 or e.vertex2 == edge.vertex1:
                found_first = True
                set_index_first = set_index
            if e.vertex1 == edge.vertex2 or e.vertex2 == edge.vertex2:
                found_second = True
                set_index_second = set_index
    return found_first, found_second, set_index_first, set_index_second
def merge_sets(edge, sets, set_index_first, set_index_second):
    if set_index_first < set_index_second:
        sets[set_index_first].update(sets[set_index_second])
        sets[set_index_first].add(edge)
        sets[set_index_second].clear()
    else:
        sets[set_index_second].update(sets[set_index_first])
        sets[set_index_first].clear()
        sets[set_index_second].add(edge)
    edge.selected = True
def run_kruskal(edgelist, node_count):
    edgelist.sort(key=return_weight)
    sets = [set([edgelist[0]])]
    edgelist[0].selected = True
    set_count = 1
    for edge in edgelist[1:]:
        found_first, found_second, set_index_first, set_index_second = find_sets(edge, sets)
        if found_first and found_second:
            if set_index_first != set_index_second:
                merge_sets(edge, sets, set_index_first, set_index_second)
        elif found_first:
            sets[set_index_first].add(edge)
            edge.selected = True
        elif found_second:
            sets[set_index_second].add(edge)
            edge.selected = True
        else:
            new_set = set([edge])
            sets.append(new_set)
            set_count += 1
            edge.selected = True
    return edgelist
edges = [
    Edge(1, 2, 1),
    Edge(2, 3, 2),
    Edge(3, 4, 3),
    Edge(1, 4, 4)
]
node_count = 4
selected_edges = run_kruskal(edges, node_count)
for edge in selected_edges:
    if edge.selected:
        print(f"Edge ({edge.vertex1}, {edge.vertex2}) with weight {edge.weight} is selected")
from heap import Min_Heap
from graph import Graph
from union_find import Set
def MST_Prim(graph):
    min_span_tree = Graph(numVertices=graph.numVertices(), numEdges=0, weightRange=0)
    queue = Min_Heap()
    parent = {}
    for vertex in graph.vertices():
        parent[vertex] = None
        queue.insert(float('inf'), vertex)
    while not queue.is_empty():
        key, vertex = queue.extract_min()
        predecessor = parent[vertex]
        if predecessor is not None:
            weight = graph.weight[(predecessor, vertex)]
            min_span_tree.addUndirectedEdge(predecessor, vertex, weight)
        for neighbor in graph.adjacent[vertex]:
            if neighbor in queue:
                new_key = graph.weight[(vertex, neighbor)]
                if new_key < queue.key(neighbor):
                    queue.decrease_key(neighbor, new_key)
                    parent[neighbor] = vertex
    return min_span_tree
def MST_Kruskal(graph):
    component = {vertex: Set(vertex) for vertex in graph.vertices()}
    min_span_tree = Graph(numVertices=graph.numVertices(), numEdges=0, weightRange=0)
    for (u, v) in sorted(graph.edges(), key=lambda e: graph.weight[e]):
        if component[u].findSet() != component[v].findSet():
            component[u].union(component[v])
            min_span_tree.addUndirectedEdge(u, v, graph.weight[(u, v)])
    return min_span_tree
def test(numVertices, numEdges, weightRange):
    graph = Graph(numVertices=numVertices, numEdges=numEdges, weightRange=weightRange, directed=False)
    mst_prim = MST_Prim(graph)
    prims_weight = sum(graph.weight[e] for e in mst_prim.edges())
    mst_kruskal = MST_Kruskal(graph)
    kruskals_weight = sum(graph.weight[e] for e in mst_kruskal.edges())
    return prims_weight == kruskals_weight
def runTests(numVertices, numEdges, weightRange, numTests):
    return all(test(numVertices, numEdges, weightRange) for _ in range(numTests))
if __name__ == "__main__":
    numVertices = 10
    numEdges = 20
    weightRange = 100
    numTests = 5
    if runTests(numVertices, numEdges, weightRange, numTests):
        print("All tests passed!")
    else:
        print("Some tests failed.")
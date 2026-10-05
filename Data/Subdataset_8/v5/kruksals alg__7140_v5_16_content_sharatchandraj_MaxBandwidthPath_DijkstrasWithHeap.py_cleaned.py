from collections import namedtuple
import MaxHeap
NumberOfVertices = 5000
Edge = namedtuple('Edge', ['vertex', 'weight'])
status = [None] * NumberOfVertices
wt = [None] * NumberOfVertices
def DijkstrasWithHeap(graph, source, destination):
    MaxHeap.initialize()
    dad = [None] * NumberOfVertices
    for i in graph.get_vertex():
        status[i] = 'unseen'
    status[source] = 'intree'
    for i in graph.get_edge(source):
        status[i.vertex] = 'fringe'
        wt[i.vertex] = i.weight
        MaxHeap.Insert(i.vertex, i.weight)
        dad[i.vertex] = source
    while 'fringe' in status:
        if destination in status and status[destination] == 'intree':
            break
        v = MaxHeap.Max()
        status[v] = 'intree'
        MaxHeap.Delete(v)
        for e in graph.get_edge(v):
            if status[e.vertex] == 'unseen':
                _handle_unseen_vertex(e, v, source, destination, dad)
            elif status[e.vertex] == 'fringe':
                _handle_fringe_vertex(e, v, source, destination, dad)
    maxBWPath = _reconstruct_path(destination, dad)
    return maxBWPath, wt[destination]
def _handle_unseen_vertex(e, v, source, destination, dad):
    status[e.vertex] = 'fringe'
    dad[e.vertex] = v
    wt[e.vertex] = min(wt[v], e.weight)
    MaxHeap.Insert(e.vertex, wt[e.vertex])
def _handle_fringe_vertex(e, v, source, destination, dad):
    if wt[e.vertex] < min(wt[v], e.weight):
        dad[e.vertex] = v
        MaxHeap.Delete(e.vertex)
        wt[e.vertex] = min(wt[v], e.weight)
        MaxHeap.Insert(e.vertex, wt[e.vertex])
def _reconstruct_path(destination, dad):
    maxBWPath = []
    end = destination
    while end is not None:
        maxBWPath.append(end)
        end = dad[end]
    maxBWPath.reverse()
    return maxBWPath
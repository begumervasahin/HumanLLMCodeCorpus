def edges_to_set(edges):
    nods = []
    for i in edges:
        if i[0] not in nods:
            nods.append(i[0])
        if i[1] not in nods:
            nods.append(i[1])
    return nods
class Dgraph:
    def __init__(self):
        self.nodes = []
        self.arrows = []
        self.dists = {}
    def add_node(self, n):
        self.nodes.append(n)
    def add_arrow(self, arrow, dist):
        self.arrows.append(arrow)
        self.dists[arrow] = dist
    def neighbors_of(self, node):
        set1 = []
        for i in self.arrows:
            if i[1] == node:
                set1.append(i[0])
            elif i[0] == node:
                set1.append(i[1])
        return set1
    def get_length(self, node1, node2):
        if (node1, node2) in self.arrows:
            return self.dists[(node1, node2)]
        elif (node2, node1) in self.arrows:
            return self.dists[(node2, node1)]
        return None
    def closest_neighb(self, node):
        mindist = float('inf')
        close_neighb = None
        for i in self.arrows:
            curdist = self.get_length(i[0], i[1])
            if i[1] == node and curdist < mindist:
                mindist = curdist
                close_neighb = i[0]
            elif i[0] == node and curdist < mindist:
                mindist = curdist
                close_neighb = i[1]
        return [close_neighb, mindist]
    def get_edges(self, arrowlist):
        near_edges = []
        searchlist = set(self.arrows) - set(arrowlist)
        nodes1 = edges_to_set(arrowlist)
        deletelist = []
        for k in searchlist:
            if (k[1] in nodes1) and (k[0] in nodes1):
                deletelist.append(k)
        searchlist = searchlist - set(deletelist)
        for i in searchlist:
            for j in arrowlist:
                if (i[0] == j[0]) or (i[0] == j[1]) or (i[1] == j[0]) or (i[1] == j[1]):
                    near_edges.append(i)
        return near_edges
if __name__ == "__main__":
    graph = Dgraph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_arrow(('A', 'B'), 5)
    graph.add_arrow(('B', 'C'), 10)
    graph.add_arrow(('A', 'C'), 15)
    print("Neighbors of B:", graph.neighbors_of('B'))
    print("Length between A and B:", graph.get_length('A', 'B'))
    print("Closest neighbor of A:", graph.closest_neighb('A'))
    print("Edges near [('A', 'B')]:", graph.get_edges([('A', 'B')]))
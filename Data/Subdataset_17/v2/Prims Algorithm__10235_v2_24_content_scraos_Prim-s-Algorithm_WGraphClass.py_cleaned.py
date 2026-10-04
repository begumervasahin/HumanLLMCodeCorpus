def edges_to_set(edges):
    nodes = set()
    for edge in edges:
        nodes.update(edge)
    return list(nodes)
class Dgraph:
    def __init__(self):
        self.nodes = []
        self.arrows = []
        self.dists = {}
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
    def add_arrow(self, arrow, dist):
        if arrow not in self.arrows:
            self.arrows.append(arrow)
            self.dists[arrow] = dist
    def neighbors_of(self, node):
        neighbors = []
        for arrow in self.arrows:
            if arrow[0] == node:
                neighbors.append(arrow[1])
            elif arrow[1] == node:
                neighbors.append(arrow[0])
        return neighbors
    def get_length(self, node1, node2):
        if (node1, node2) in self.dists:
            return self.dists[(node1, node2)]
        elif (node2, node1) in self.dists:
            return self.dists[(node2, node1)]
        return None
    def closest_neighb(self, node):
        min_dist = float('inf')
        closest_neighbor = None
        for arrow in self.arrows:
            cur_dist = self.get_length(arrow[0], arrow[1])
            if (arrow[0] == node or arrow[1] == node) and cur_dist < min_dist:
                min_dist = cur_dist
                closest_neighbor = arrow[1] if arrow[0] == node else arrow[0]
        return [closest_neighbor, min_dist]
    def get_edges(self, arrow_list):
        near_edges = []
        search_list = set(self.arrows) - set(arrow_list)
        nodes_in_arrows = edges_to_set(arrow_list)
        filtered_search_list = {arrow for arrow in search_list if not (arrow[0] in nodes_in_arrows and arrow[1] in nodes_in_arrows)}
        for arrow in filtered_search_list:
            if any(node in nodes_in_arrows for node in arrow):
                near_edges.append(arrow)
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
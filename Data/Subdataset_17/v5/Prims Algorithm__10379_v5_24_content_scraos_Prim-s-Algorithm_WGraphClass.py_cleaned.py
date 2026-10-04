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
    def closest_neighbor(self, node):
        min_dist = float('inf')
        closest_node = None
        for arrow in self.arrows:
            if node in arrow:
                neighbor = arrow[1] if arrow[0] == node else arrow[0]
                dist = self.dists[arrow]
                if dist < min_dist:
                    min_dist = dist
                    closest_node = neighbor
        return closest_node, min_dist
    def get_edges(self, arrow_list):
        near_edges = []
        current_edges = set(self.arrows) - set(arrow_list)
        nodes_in_arrows = set(edges_to_set(arrow_list))
        current_edges = {edge for edge in current_edges if not (edge[0] in nodes_in_arrows and edge[1] in nodes_in_arrows)}
        for edge in current_edges:
            if any(set(edge) & set(arrow) for arrow in arrow_list):
                near_edges.append(edge)
        return near_edges
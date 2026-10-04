from igraph import Graph
class Arrow:
    def __init__(self, origin='', target='', cost=0):
        self.origin = origin
        self.target = target
        self.cost = cost
    def __repr__(self):
        return f"{self.origin} -> {self.target} [cost: {self.cost}]"
def run_graph(graph, vertex):
    list_of_arrows = []
    for edge in graph.incident(vertex):
        edge_data = graph.es[edge]
        arrow = Arrow(
            origin=edge_data.source,
            target=edge_data.target,
            cost=edge_data['peso']
        )
        list_of_arrows.append(arrow)
    return list_of_arrows
def initialize_graph():
    graph = Graph(directed=True)
    graph.add_vertices(5)
    graph.vs['nome'] = ['a', 'b', 'c', 'd', 'e']
    graph.add_edges([(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4)])
    graph.es['peso'] = [3, 11, 3, 2, 7, 2]
    return graph
def calculate_shortest_paths(graph):
    num_vertices = len(graph.vs)
    cost_list = [float('inf')] * num_vertices
    cost_list[0] = 0
    for vertex in range(num_vertices):
        for arrow in run_graph(graph, vertex):
            new_cost = cost_list[arrow.origin] + arrow.cost
            if new_cost < cost_list[arrow.target]:
                cost_list[arrow.target] = new_cost
    return cost_list
def main():
    graph = initialize_graph()
    cost_list = calculate_shortest_paths(graph)
    print("Shortest path costs:", cost_list)
if __name__ == "__main__":
    main()
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
        a = Arrow(
            origin=edge_data.source,
            cost=edge_data['peso'],
            target=edge_data.target
        )
        list_of_arrows.append(a)
    return list_of_arrows
def initialize_graph():
    my_graph = Graph(directed=True)
    my_graph.add_vertices(5)
    my_graph.vs['nome'] = ['a', 'b', 'c', 'd', 'e']
    my_graph.add_edges([(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4)])
    my_graph.es['peso'] = [3, 11, 3, 2, 7, 2]
    return my_graph
def calculate_shortest_paths(graph):
    cost_list = [float('inf')] * len(graph.vs)
    cost_list[0] = 0
    for vertex in graph.vs:
        for arrow in run_graph(graph, vertex.index):
            new_cost = cost_list[arrow.origin] + arrow.cost
            if new_cost < cost_list[arrow.target]:
                cost_list[arrow.target] = new_cost
    return cost_list
def main():
    my_graph = initialize_graph()
    cost_list = calculate_shortest_paths(my_graph)
    print("Shortest path costs:", cost_list)
if __name__ == "__main__":
    main()
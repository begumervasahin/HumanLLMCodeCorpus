from igraph import Graph
class Arrow:
    def __init__(self, origin='', target='', cost=''):
        self.origin = origin
        self.target = target
        self.cost = cost
    def __repr__(self):
        return f"{self.origin} -> {self.target} [cost: {self.cost}]"
def run_graph(graph, vertex):
    list_of_arrows = []
    for edge in graph.incident(vertex):
        a = Arrow(
            origin=graph.vs[graph.es[edge].source]['nome'],
            cost=graph.es[edge]['peso'],
            target=graph.vs[graph.es[edge].target]['nome']
        )
        list_of_arrows.append(a)
    return list_of_arrows
def main():
    my_graph = Graph(directed=True)
    my_graph.add_vertices(5)
    my_graph.vs['nome'] = ['a', 'b', 'c', 'd', 'e']
    my_graph.add_edges([(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4)])
    my_graph.es['peso'] = [3, 11, 3, 2, 7, 2]
    cost_list = [999] * len(my_graph.vs)
    cost_list[0] = 0
    for vertex in my_graph.vs:
        for arrow in run_graph(my_graph, vertex.index):
            origin_idx = my_graph.vs.find(name=arrow.origin).index
            target_idx = my_graph.vs.find(name=arrow.target).index
            new_cost = cost_list[origin_idx] + arrow.cost
            if new_cost < cost_list[target_idx]:
                cost_list[target_idx] = new_cost
    print(cost_list)
if __name__ == "__main__":
    main()
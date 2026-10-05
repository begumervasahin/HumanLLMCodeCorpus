
from Weighted_Graph import Weighted_Graph
from functions import update, total_sum
def find_minimum_spanning_tree(edge_file_name, start_vertex=0, draw=False):
    minimum_spanning_tree = ({start_vertex}, [])
    graph = Weighted_Graph(edge_file_name)
    if draw:
        graph.draw_graph()
    while minimum_spanning_tree[0] != graph.vertex_set():
        minimum_spanning_tree = update(minimum_spanning_tree, graph)
        if draw:
            graph.draw_subgraph(minimum_spanning_tree)
    print("The minimum spanning tree costs: " + str(total_sum(minimum_spanning_tree, graph)))
    return minimum_spanning_tree
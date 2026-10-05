
from Weighted_Graph import Weighted_Graph
from functions import update, total_sum
def Prims(edge_file_name, start_vertex=0, draw=False):
    MST = ({start_vertex}, [])
    graph = Weighted_Graph(edge_file_name)
    if draw:
        graph.draw_graph()
    while MST[0] != graph.vertex_set():
        MST = update(MST, graph)
        if draw:
            graph.draw_subgraph(MST)
    print("The minimum spanning tree costs: " + str(total_sum(MST, graph)))
    return MST
if __name__ == "__main__":
    edge_file_name = "your_edge_file_name.txt"
    Prims(edge_file_name, start_vertex=0, draw=True)
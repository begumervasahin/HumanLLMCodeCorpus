
from Weighted_Graph import Weighted_Graph
from functions import update, total_sum
def fonk1(edge_file_name, b1 = 0, b4 = False):
    b2 = ({b1}, [])
    b3 = Weighted_Graph(edge_file_name)
    if b4 = = True:
        b3.draw_graph()
    while b2[0] != b3.vertex_set():
            b2 = update(b2,b3)
            b3.draw_subgraph(b2)
    print("The minimum spanning tree costs: " +str(total_sum(b2,b3)))
    return b2
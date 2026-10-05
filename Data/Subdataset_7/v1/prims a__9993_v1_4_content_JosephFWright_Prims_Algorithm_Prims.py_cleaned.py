from Weighted_Graph import Weighted_Graph
from functions import update, total_sum
def fonk1(b5, b1 = 0, draw=False):
    b2 = ({b1}, [])
    b3 = Weighted_Graph(b5)
    if draw:
        b3.draw_graph()
    while b2[0] != b3.vertex_set():
        b2 = update(b2, b3)
        if draw:
            b3.draw_subgraph(b2)
    print("The minimum spanning tree costs: " + str(total_sum(b2, b3)))
    return b2
if b4 = = "__main__":
    b5 = "your_edge_file_name.txt"
    fonk1(b5, b1 = 0, draw=True)
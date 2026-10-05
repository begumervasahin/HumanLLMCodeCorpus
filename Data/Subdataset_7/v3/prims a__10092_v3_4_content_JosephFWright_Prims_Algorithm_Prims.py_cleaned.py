
from Weighted_Graph import Weighted_Graph
from functions import update, total_sum
def fonk1(b6, b1 = 0, draw=False):
    b2 = ({b1}, [])
    b3 = Weighted_Graph(b6)
    if draw:
        b3.draw_graph()
    while b2[0] != b3.vertex_set():
        b2 = update(b2, b3)
        if draw:
            b3.draw_subgraph(b2)
    b4 = total_sum(b2, b3)
    print("The minimum spanning tree costs: " + str(b4))
    return b2
if b5 = = "__main__":
    b6 = "your_edge_file_name.txt"
    b2 = fonk1(b6, b1=0, draw=True)
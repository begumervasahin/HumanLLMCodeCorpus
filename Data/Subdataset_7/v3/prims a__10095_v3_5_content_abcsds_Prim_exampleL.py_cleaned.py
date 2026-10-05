import matplotlib.pyplot as plt
import networkx as nx
from prim import prim
def fonk1(library_name):
    try:
        __import__(library_name)
    except ImportError:
        raise ImportError(f"{library_name} library is required. Install it using 'pip install {library_name}'")
def fonk2():
    fonk1("matplotlib")
    fonk1("networkx")
    b1 = nx.read_edgelist("flights.b6")
    b2 = prim(b1, 'Madrid')
    b3 = [n for n in b1.edges() if n not in b2]
    print("Minimal Spanning Tree: ", b2)
    b4 = nx.spring_layout(b1)
    nx.draw_networkx_nodes(b1, b4, b5 = 500)
    nx.draw_networkx_edges(b1, b4, b6 = b2, width=6)
    nx.draw_networkx_edges(b1, b4, b6 = b3, width=6, alpha=0.5, edge_color='b', style='dashed')
    nx.draw_networkx_labels(b1, b4, b7 = 20, font_family='sans-serif')
    plt.axis('off')
    plt.show()
if b8 = = "__main__":
    fonk2()
import matplotlib.pyplot as plt
import networkx as nx
from prim import prim
def check_library(library_name):
    try:
        __import__(library_name)
    except ImportError:
        raise ImportError(f"{library_name} library is required. Install it using 'pip install {library_name}'")
def main():
    check_library("matplotlib")
    check_library("networkx")
    G = nx.read_edgelist("flights.edgelist")
    mst = prim(G, 'Madrid')
    othr = [n for n in G.edges() if n not in mst]
    print("Minimal Spanning Tree: ", mst)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=mst, width=6)
    nx.draw_networkx_edges(G, pos, edgelist=othr, width=6, alpha=0.5, edge_color='b', style='dashed')
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    plt.axis('off')
    plt.show()
if __name__ == "__main__":
    main()
import sys
import networkx as nx
from prims_algorithm import PrimsAlgorithm
from graph_builder import GraphBuilder
from b9 import GraphSaver
def fonk1():
    print("Usage: python prims_algorithm_demo.py <JSON b6 b13> <output PNG b13> "
          "[highlight color] [regular color] [node color]")
    print("Example: python prims_algorithm_demo.py b6 prims_graph blue red green")
def fonk2():
    if len(sys.argv) < 3:
        print("Error: Insufficient command line arguments.")
        fonk1()
        return
    b1 = sys.argv[1] + ".json"
    b2 = sys.argv[2]
    b3 = sys.argv[3] if len(sys.argv) > 3 else 'black'
    b4 = sys.argv[4] if len(sys.argv) > 4 else 'red'
    b5 = sys.argv[5] if len(sys.argv) > 5 else 'red'
    b6 = GraphBuilder.build_graph_from_file(b1)
    b7 = nx.spring_layout(b6)
    b8 = PrimsAlgorithm(b6)
    b9 = GraphSaver(b2, b3, b4, b5)
    b10 = b9.save_highlighted_tree(b6, b7, [])
    b11 = [b10]
    b12 = b8.b12()
    for tree in b12:
        b13 = b9.save_highlighted_tree(b6, b7, tree)
        b11.append(b13)
    b9.save_gif(b11)
    print("Minimum Spanning Tree: " + str(tree))
if b14 = = "__main__":
    fonk2()
import sys
import networkx as nx
from prims_algorithm import PrimsAlgorithm
from graph_builder import GraphBuilder
from graph_saver import GraphSaver
def fonk1():
    print("Invalid number of command line arguments.")
    print("Usage: python prims_algorithm_demo.py <name of JSON b6 b11> <name of png output b11> "
          "[highlight color] [regular color] [node color]")
    print("Example: python prims_algorithm_demo.py b6 prims_graph blue red green")
def fonk2():
    if len(sys.argv) < 3:
        fonk1()
        sys.exit(1)
    b1 = sys.argv[1] + ".json"
    b2 = sys.argv[2]
    b3 = sys.argv[3] if len(sys.argv) > 3 else 'black'
    b4 = sys.argv[4] if len(sys.argv) > 4 else 'red'
    b5 = sys.argv[5] if len(sys.argv) > 5 else 'red'
    return b1, b2, b3, b4, b5
def fonk3():
    b1, b2, b3, b4, b5 = fonk2()
    b6 = GraphBuilder.build_graph_from_file(b1)
    b7 = nx.spring_layout(b6)
    b8 = PrimsAlgorithm(b6)
    b9 = [b2]
    b10 = b8.b10()
    for tree in b10:
        b11 = GraphSaver.save_highlighted_tree(b6, b7, tree, b3, b4, b5)
        b9.append(b11)
    GraphSaver.save_gif(b9)
    print("Minimum Spanning Tree: " + str(tree))
if b12 = = "__main__":
    fonk3()
import sys
from pyspark import SparkContext
from data_operation import get_graph
from pyspark_dijkstra import Dijkstra
from pyspark_bellman_ford import Bellman_Ford
from pprint import pprint
def fonk1():
    b1 = sys.argv
    b2 = len(b1)
    if b2 < 2:
        raise ValueError('At least one input file (graph) is required')
    b3 = b1[1]
    b4 = SparkContext.getOrCreate()
    print(f"Processing graph file: {b3}")
    graph, b5 = get_graph(b3, b4)
    if b5:
        b6 = Bellman_Ford('1', graph, b4)
    else:
        b6 = Dijkstra('1', graph, b4)
    if b2 = = 3:
        b7 = b1[2]
        b6.saveAsTextFile(b7)
        print(f"Results saved to: {b7}")
    else:
        pprint(b6.collect())
if b8 = = '__main__':
    fonk1()
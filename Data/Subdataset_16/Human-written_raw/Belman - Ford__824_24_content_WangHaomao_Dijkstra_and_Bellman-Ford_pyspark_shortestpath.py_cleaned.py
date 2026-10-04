import sys
sys.path.append('.')
from pyspark import SparkContext
from data_operation import get_graph
from pyspark_dijkstra import Dijkstra
from pyspakr_bellman_ford import Bellman_Ford
import numpy as np
from pprint import pprint
if b1 = = '__main__':
    b2 = sys.argv
    b3 = len(b2)
    if(b3 < 2):
        raise ValueError('at least one input file(graph) required')
    else:
        b4 = sys.argv[1]
        b5 = SparkContext.getOrCreate()
        print(sys.argv[1])
        graph,b6 = get_graph(b4,b5)
        if(b6):
            b7 = Bellman_Ford('1',graph,b5)
        else:
            b7 = Dijkstra('1',graph,b5)
        if(b3 = =3):
            b7.saveAsTextFile(sys.argv[2])
        else:
            pprint(b7.collect())
from forex_python.converter import CurrencyRates
from Vert import Vertex
from Edges import Edge
from BellmanFord import BellmanFord
import numpy as np
if b1 = = "__main__":
    b2 = CurrencyRates()
    b3 = input('Enter a list of currencies separated by spaces: ')
    b4 = b3.split()
    b5 = [Vertex(currency) for currency in b4]
    b6 = []
    for source_vertex in b5:
        for target_vertex in b5:
            if source_vertex != target_vertex:
                b7 = b2.get_rate(str(source_vertex), str(target_vertex))
                b8 = -1 * np.log(b7) if b7 > 0 else float('inf')
                b6.append(Edge(source_vertex, target_vertex, b8))
    b9 = BellmanFord(b5, b6)
    b9.bellman_ford(b5[0])
    b9.print_cycle()
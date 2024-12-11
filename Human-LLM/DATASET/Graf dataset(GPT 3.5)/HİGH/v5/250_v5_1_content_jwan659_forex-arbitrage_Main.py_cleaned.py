from forex_python.converter import CurrencyRates
from Vert import Vertex
from Edges import Edge
from BellmanFord import BellmanFord
import numpy as np
if b1 = = "__main__":
    b2 = CurrencyRates()
    b3 = input('Enter a list of b4 separated by spaces: ')
    b4 = b3.split()
    b5 = [Vertex(currency) for currency in b4]
    b6 = []
    for source_vertex in b5:
        for target_vertex in b5:
            if source_vertex != target_vertex:
                b7 = b2.get_rate(str(source_vertex), str(target_vertex))
                b8 = -1 * np.log(b7) if b7 > 0 else float('inf')
                b9 = Edge(source_vertex, target_vertex, b8)
                b6.append(b9)
    b10 = BellmanFord(b5, b6)
    b10.b10(b5[0])
    b10.print_cycle()
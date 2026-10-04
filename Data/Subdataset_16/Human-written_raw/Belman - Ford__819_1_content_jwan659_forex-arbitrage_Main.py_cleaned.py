from BellmanFord import BellmanFord
from Edges import Edge
from Vert import Vertex
from forex_python.converter import CurrencyRates
import numpy as np
if b1 = = "__main__":
    b2 = CurrencyRates()
    b3 = raw_input('Enter a list of currencies: ')
    b4 = b3.split()
    b5 = []
    for item in b4:
        b5.append(Vertex(item))
    b6 = []
    for i in b5:
        for j in b5:
            if i != j:
                b6.append(Edge(i, j, (-1*np.log((b2.get_rate(str(i), str(j)))))))
    b7 = BellmanFord(b5, b6)
    b7.bellman_ford(b5[0])
    b7.print_cycle()
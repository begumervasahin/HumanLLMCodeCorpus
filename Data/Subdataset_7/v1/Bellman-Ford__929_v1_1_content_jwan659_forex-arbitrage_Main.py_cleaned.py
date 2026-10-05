from forex_python.converter import CurrencyRates
from math import log
from Vert import Vertex
from Edges import Edge
from BellmanFord import BellmanFord
if b1 = = "__main__":
    b2 = CurrencyRates()
    b3 = input('Enter a list of currencies separated by spaces: ')
    b4 = b3.split()
    b5 = [Vertex(currency) for currency in b4]
    b6 = []
    for i in b5:
        for j in b5:
            if i != j:
                b7 = b2.get_rate(i.name, j.name)
                b8 = -1 * log(b7) if b7 > 0 else float('inf')
                b6.append(Edge(i, j, b8))
    b9 = BellmanFord(b5, b6)
    b9.bellman_ford(b5[0])
    b9.print_cycle()
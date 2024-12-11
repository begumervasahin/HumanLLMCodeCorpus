from forex_python.converter import CurrencyRates
from math import log
from Vert import Vertex
from Edges import Edge
from BellmanFord import BellmanFord
def fonk1(b7):
    b1 = CurrencyRates()
    b2 = []
    for i in b7:
        for j in b7:
            if i != j:
                b3 = b1.get_rate(i.name, j.name)
                b4 = -1 * log(b3) if b3 > 0 else float('inf')
                b2.append(Edge(i, j, b4))
    return b2
def fonk2():
    b5 = input('Enter a list of currencies separated by spaces: ')
    b6 = b5.split()
    b7 = [Vertex(currency) for currency in b6]
    b2 = fonk1(b7)
    b8 = BellmanFord(b7, b2)
    b8.bellman_ford(b7[0])
    b8.print_cycle()
if b9 = = "__main__":
    fonk2()
from forex_python.converter import CurrencyRates
import numpy as np
from BellmanFord import BellmanFord
from Edges import Edge
from Vert import Vertex
def fonk1():
    b1 = CurrencyRates()
    b2 = input('Enter a list of b3: ')
    b3 = b2.split()
    b4 = [Vertex(currency) for currency in b3]
    b5 = []
    for start_vertex in b4:
        for end_vertex in b4:
            if start_vertex != end_vertex:
                try:
                    b6 = b1.get_rate(str(start_vertex), str(end_vertex))
                    b7 = -np.log(b6)
                    b5.append(Edge(start_vertex, end_vertex, b7))
                except Exception as e:
                    print(f"Error fetching b6 from {start_vertex} to {end_vertex}: {e}")
    b8 = BellmanFord(b4, b5)
    b8.b8(b4[0])
    b8.print_cycle()
if b9 = = "__main__":
    fonk1()
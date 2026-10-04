from forex_python.converter import CurrencyRates
import numpy as np
from BellmanFord import BellmanFord
from Edges import Edge
from Vert import Vertex
def main():
    c = CurrencyRates()
    input_string = input('Enter a list of currencies: ')
    currencies = input_string.split()
    vertex_list = [Vertex(currency) for currency in currencies]
    edge_list = []
    for i in vertex_list:
        for j in vertex_list:
            if i != j:
                try:
                    rate = c.get_rate(str(i), str(j))
                    weight = -1 * np.log(rate)
                    edge_list.append(Edge(i, j, weight))
                except Exception as e:
                    print(f"Error fetching rate for {i} to {j}: {e}")
    algo = BellmanFord(vertex_list, edge_list)
    algo.bellman_ford(vertex_list[0])
    algo.print_cycle()
if __name__ == "__main__":
    main()
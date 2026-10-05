from forex_python.converter import CurrencyRates
from Vert import Vertex
from Edges import Edge
from BellmanFord import BellmanFord
import numpy as np
if __name__ == "__main__":
    currency_rates = CurrencyRates()
    input_string = input('Enter a list of currencies separated by spaces: ')
    currency_list = input_string.split()
    vertex_list = [Vertex(currency) for currency in currency_list]
    edge_list = []
    for source_vertex in vertex_list:
        for target_vertex in vertex_list:
            if source_vertex != target_vertex:
                conversion_rate = currency_rates.get_rate(str(source_vertex), str(target_vertex))
                weight = -1 * np.log(conversion_rate) if conversion_rate > 0 else float('inf')
                edge_list.append(Edge(source_vertex, target_vertex, weight))
    bellman_ford_algo = BellmanFord(vertex_list, edge_list)
    bellman_ford_algo.bellman_ford(vertex_list[0])
    bellman_ford_algo.print_cycle()
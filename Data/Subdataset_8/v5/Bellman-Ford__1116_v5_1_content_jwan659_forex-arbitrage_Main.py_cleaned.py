from forex_python.converter import CurrencyRates
from Vert import Vertex
from Edges import Edge
from BellmanFord import BellmanFord
import numpy as np
if __name__ == "__main__":
    currency_rates = CurrencyRates()
    input_currencies = input('Enter a list of currencies separated by spaces: ')
    currencies = input_currencies.split()
    vertices = [Vertex(currency) for currency in currencies]
    edges = []
    for source_vertex in vertices:
        for target_vertex in vertices:
            if source_vertex != target_vertex:
                conversion_rate = currency_rates.get_rate(str(source_vertex), str(target_vertex))
                weight = -1 * np.log(conversion_rate) if conversion_rate > 0 else float('inf')
                edge = Edge(source_vertex, target_vertex, weight)
                edges.append(edge)
    bellman_ford = BellmanFord(vertices, edges)
    bellman_ford.bellman_ford(vertices[0])
    bellman_ford.print_cycle()
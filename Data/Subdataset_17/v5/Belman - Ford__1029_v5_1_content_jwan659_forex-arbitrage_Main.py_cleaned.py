from BellmanFord import BellmanFord
from Edges import Edge
from Vert import Vertex
from forex_python.converter import CurrencyRates
import numpy as np
def main():
    currency_rates = CurrencyRates()
    input_string = input('Enter a list of currencies separated by spaces: ')
    currencies = input_string.split()
    vertices = create_vertices(currencies)
    edges = create_edges(vertices, currency_rates)
    detect_arbitrage(vertices, edges)
def create_vertices(currencies):
    return [Vertex(currency) for currency in currencies]
def create_edges(vertices, currency_rates):
    edges = []
    for start_vertex in vertices:
        for end_vertex in vertices:
            if start_vertex != end_vertex:
                try:
                    rate = currency_rates.get_rate(str(start_vertex), str(end_vertex))
                    weight = -np.log(rate)
                    edges.append(Edge(start_vertex, end_vertex, weight))
                except Exception as e:
                    print(f"Error fetching rate from {start_vertex} to {end_vertex}: {e}")
    return edges
def detect_arbitrage(vertices, edges):
    bellman_ford = BellmanFord(vertices, edges)
    bellman_ford.bellman_ford(vertices[0])
    bellman_ford.print_cycle()
if __name__ == "__main__":
    main()
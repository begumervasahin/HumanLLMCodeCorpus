from BellmanFord import BellmanFord
from Edges import Edge
from Vert import Vertex
from forex_python.converter import CurrencyRates
import numpy as np
def main():
    currency_rates = CurrencyRates()
    input_string = input('Enter a list of currencies separated by spaces: ')
    currencies = input_string.split()
    vertex_list = create_vertices(currencies)
    edge_list = create_edges(vertex_list, currency_rates)
    run_bellman_ford(vertex_list, edge_list)
def create_vertices(currencies):
    return [Vertex(currency) for currency in currencies]
def create_edges(vertex_list, currency_rates):
    edge_list = []
    for start_vertex in vertex_list:
        for end_vertex in vertex_list:
            if start_vertex != end_vertex:
                try:
                    rate = currency_rates.get_rate(str(start_vertex), str(end_vertex))
                    weight = -np.log(rate)
                    edge_list.append(Edge(start_vertex, end_vertex, weight))
                except Exception as e:
                    print(f"Error fetching rate from {start_vertex} to {end_vertex}: {e}")
    return edge_list
def run_bellman_ford(vertex_list, edge_list):
    bellman_ford = BellmanFord(vertex_list, edge_list)
    bellman_ford.bellman_ford(vertex_list[0])
    bellman_ford.print_cycle()
if __name__ == "__main__":
    main()
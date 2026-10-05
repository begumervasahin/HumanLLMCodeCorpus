from forex_python.converter import CurrencyRates
from math import log
from Vert import Vertex
from Edges import Edge
from BellmanFord import BellmanFord
def get_currency_conversion_edges(vertex_list):
    c = CurrencyRates()
    edge_list = []
    for i in vertex_list:
        for j in vertex_list:
            if i != j:
                rate = c.get_rate(i.name, j.name)
                weight = -1 * log(rate) if rate > 0 else float('inf')
                edge_list.append(Edge(i, j, weight))
    return edge_list
def main():
    input_string = input('Enter a list of currencies separated by spaces: ')
    currency_list = input_string.split()
    vertex_list = [Vertex(currency) for currency in currency_list]
    edge_list = get_currency_conversion_edges(vertex_list)
    bellman_ford_algo = BellmanFord(vertex_list, edge_list)
    bellman_ford_algo.bellman_ford(vertex_list[0])
    bellman_ford_algo.print_cycle()
if __name__ == "__main__":
    main()
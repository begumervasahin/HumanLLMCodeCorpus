from grafo import Grafo
from dijkstra import dijkstra
from utils import caminho_minimo
class NegativeWeightException(Exception):
    pass
def create_test_graph():
    """
    Create a test graph based on the example from the book "Algorithms 3rd Edition (Cormen)", page 480.
    :return: A graph object.
    Run the Dijkstra algorithm on the graph and print the shortest paths and costs for each vertex.
    :param graph: The graph object.
    :param start_vertex_id: The starting vertex ID for the Dijkstra algorithm.
    Test the graph example from the book "Algorithms 3rd Edition (Cormen)", page 480.
    """
    print('Testing graph example from "Algorithms 3rd Edition (Cormen)", page 480.')
    graph = create_test_graph()
    print_shortest_paths(graph, 'a')
if __name__ == "__main__":
    test_graph()
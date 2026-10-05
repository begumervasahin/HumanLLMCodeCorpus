from ordered_linked_list.ordered_linked_list import LinkedList
from logger.timer import Timer
from graph_handler.edge import Edge
from graph_handler.vertex import Vertex
from graph_handler.graph import Graph
from dijkstra.closest_path import DijkstraArray
from data_loader.data_loader import Data_Loader
import gc
def main():
    data_loader = Data_Loader()
    timer = Timer()
    graph_set = data_loader.load_data('./problematic-data')
    for graph_data in graph_set:
        graph = create_graph(graph_data)
        print_separator()
        execution_result, time_difference = execute_dijkstra(graph, timer)
        generate_and_write_report(graph, execution_result, time_difference)
        gc.collect()
def create_graph(graph_data):
    graph = Graph(Vertex(graph_data['entry']), graph_data['name'], graph_data['path'])
    for edge_data in graph_data['edges']:
        origin_vertex = Vertex(edge_data['origin'])
        end_vertex = Vertex(edge_data['end'])
        edge_weight = edge_data['weight']
        graph.add_new_connection(origin_vertex, edge_weight, end_vertex)
    return graph
def execute_dijkstra(graph, timer):
    timer.start()
    result = DijkstraArray(graph.get_representation()['struct'], graph.get_entry().get_data(), None)
    timer.end()
    time_difference = timer.get_timer_difference()
    return result, time_difference
def generate_and_write_report(graph, execution_result, time_difference):
    report = {
        "strategy": "using array",
        "instance": graph.get_representation()['label'],
        "number_of_nodes": len(graph.get_vertices()),
        "number_of_edges": graph.get_num_edges(),
        "time_spent_in_milliseconds": time_difference,
        "origin_node": graph.get_entry().get_data().get_data(),
        "distance_from_origin_to_each_node": execution_result['distances'],
        "predecessors_set": execution_result['predecessors']
    }
    report_name = report["instance"].replace("\\", "-")
    with open(f'./reports/{report_name}report.txt', 'w') as file:
        for key, value in report.items():
            file.write(f'{key}:{value}\n')
        print("Completed Report for", report_name)
def print_separator():
    print("-----------------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    main()
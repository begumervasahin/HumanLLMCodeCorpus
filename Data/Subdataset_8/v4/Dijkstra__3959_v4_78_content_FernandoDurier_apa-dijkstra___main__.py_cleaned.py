from ordered_linked_list.ordered_linked_list import LinkedList
from logger.timer import Timer
from graph_handler.edge import Edge
from graph_handler.vertex import Vertex
from graph_handler.graph import Graph
from dijkstra.closest_path import DijkstraArray
from data_loader.data_loader import Data_Loader
import gc
def main():
    graphs = []
    data_loader = Data_Loader()
    timer = Timer()
    timer2 = Timer()
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
        graph.add_new_connection(Vertex(edge_data['origin']), edge_data['weight'], Vertex(edge_data['end']))
    return graph
def execute_dijkstra(graph, timer):
    timer.start()
    result = DijkstraArray(graph.get_representation()['struct'], graph.get_entry().get_data(), None)
    timer.end()
    time_difference = timer.get_timer_difference()
    return result, time_difference
def generate_and_write_report(graph, execution_result, time_difference):
    report = {}
    report["strategy"] = "using array"
    report["instance"] = graph.get_representation()['label']
    report["number_of_nodes"] = len(graph.get_vertices())
    report["number_of_edges"] = graph.get_num_edges()
    report["time_spent_in_milliseconds"] = time_difference
    report["origin_node"] = graph.get_entry().get_data().get_data()
    report["distance_from_origin_to_each_node"] = execution_result['distances']
    report["predecessors_set"] = execution_result['predecessors']
    report_name = report["instance"].replace("\\", "-")
    with open('./reports/' + report_name + 'report.txt', 'w') as file:
        for key, value in report.items():
            file.write('%s:%s\n' % (key, value))
        print("Completed Report for ", report_name)
def print_separator():
    print("-----------------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    main()
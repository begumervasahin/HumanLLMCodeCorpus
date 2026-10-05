from ordered_linked_list.ordered_linked_list import *
from logger.timer import Timer
from graph_handler.edge import Edge
from graph_handler.vertrix import Vertrix
from graph_handler.graph import Graph
from dijkstra.closest_path import DijkstraArray
from data_loader.data_loader import Data_Loader
import gc
def main():
    graphs = []
    data_loader = Data_Loader()
    timer1 = Timer()
    timer2 = Timer()
    graph_set = data_loader.loadData('./problematic-data')
    for graph_data in graph_set:
        graph = Graph(Vertrix(graph_data['entry']), graph_data['name'], graph_data['path'])
        for edge_data in graph_data['edges']:
            graph.addNewConnection(Vertrix(edge_data['origin']), edge_data['weigth'], Vertrix(edge_data['end']))
        print("-----------------------------------------------------------------------------------------------------")
        chosen_graph = graph
        timer1.set_timer_start()
        print("-----------------------------------------------------------------------------------------------------")
        graph_representation = chosen_graph.getRepresentation()
        execution_result = DijkstraArray(chosen_graph.getRepresentation()['struct'], chosen_graph.getEntry().getData(), None)
        timer1.set_timer_end()
        report = {}
        report["strategy"] = "using array"
        report["instance"] = graph_representation['label']
        report["number_of_nodes"] = len(chosen_graph.getVertrixes())
        report["number_of_edges"] = chosen_graph.getQuantityOfEdges()
        report["time_spent_in_miliseconds"] = timer1.get_timer_difference()
        start_node = chosen_graph.getEntry()
        report["origin_node"] = start_node.getData().getData()
        report["distance_from_origin_to_each_node"] = execution_result['distances']
        report["predecessors_set"] = execution_result['predecessors']
        report_name = graph_representation['label'].replace("\\", "-")
        with open('./reports/' + report_name + 'report.txt', 'w') as file:
            for key, value in report.items():
                file.write('%s:%s\n' % (key, value))
            print("Completed Report for ", report_name)
        gc.collect()
if __name__ == "__main__":
    main()
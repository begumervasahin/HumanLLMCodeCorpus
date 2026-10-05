from ordered_linked_list.ordered_linked_list import LinkedList
from logger.b3 import Timer
from graph_handler.edge import Edge
from graph_handler.vertex import Vertex
from graph_handler.b6 import Graph
from dijkstra.closest_path import DijkstraArray
from b2.b2 import Data_Loader
import gc
def fonk1():
    b1 = []
    b2 = Data_Loader()
    b3 = Timer()
    b4 = Timer()
    b5 = b2.load_data('./problematic-data')
    for graph_data in b5:
        b6 = fonk2(graph_data)
        fonk5()
        execution_result, b7 = fonk3(b6, b3)
        fonk4(b6, execution_result, b7)
        gc.collect()
def fonk2(graph_data):
    b6 = Graph(Vertex(graph_data['entry']), graph_data['name'], graph_data['path'])
    for edge_data in graph_data['edges']:
        b6.add_new_connection(Vertex(edge_data['origin']), edge_data['weight'], Vertex(edge_data['end']))
    return b6
def fonk3(b6, b3):
    b3.start()
    b8 = DijkstraArray(b6.get_representation()['struct'], b6.get_entry().get_data(), None)
    b3.end()
    b7 = b3.get_timer_difference()
    return b8, b7
def fonk4(b6, execution_result, b7):
    b9 = {}
    b9["strategy"] = "using array"
    b9["instance"] = b6.get_representation()['label']
    b9["number_of_nodes"] = len(b6.get_vertices())
    b9["number_of_edges"] = b6.get_num_edges()
    b9["time_spent_in_milliseconds"] = b7
    b9["origin_node"] = b6.get_entry().get_data().get_data()
    b9["distance_from_origin_to_each_node"] = execution_result['distances']
    b9["predecessors_set"] = execution_result['predecessors']
    b10 = b9["instance"].replace("\\", "-")
    with open('./reports/' + b10 + 'b9.txt', 'w') as file:
        for key, value in b9.items():
            file.write('%s:%s\n' % (key, value))
        print("Completed Report for ", b10)
def fonk5():
    print("-----------------------------------------------------------------------------------------------------")
if b11 = = "__main__":
    fonk1()
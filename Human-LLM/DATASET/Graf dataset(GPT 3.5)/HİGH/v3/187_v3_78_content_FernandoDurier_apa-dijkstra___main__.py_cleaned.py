from ordered_linked_list.ordered_linked_list import LinkedList
from logger.b2 import Timer
from graph_handler.edge import Edge
from graph_handler.vertex import Vertex
from graph_handler.b4 import Graph
from dijkstra.closest_path import DijkstraArray
from b1.b1 import DataLoader
import gc
def fonk1():
    b1 = DataLoader()
    b2 = Timer()
    b3 = b1.load_data('./problematic-data')
    for graph_data in b3:
        b4 = fonk2(graph_data)
        fonk6()
        fonk3(b4, b2)
def fonk2(graph_data):
    b4 = Graph(Vertex(graph_data['entry']), graph_data['name'], graph_data['path'])
    for edge_data in graph_data['edges']:
        b4.add_new_connection(Vertex(edge_data['origin']), edge_data['weight'], Vertex(edge_data['end']))
    return b4
def fonk3(b4, b2):
    b2.start()
    b5 = DijkstraArray(b4.get_representation()['struct'], b4.get_entry().get_data(), None)
    b2.end()
    b6 = fonk4(b4, b5, b2)
    fonk5(b6)
    gc.collect()
def fonk4(b4, b5, b2):
    b6 = {}
    b6["strategy"] = "using array"
    b6["instance"] = b4.get_representation()['label']
    b6["number_of_nodes"] = len(b4.get_vertices())
    b6["number_of_edges"] = b4.get_num_edges()
    b6["time_spent_in_milliseconds"] = b2.get_duration()
    b6["origin_node"] = b4.get_entry().get_data().get_data()
    b6["distance_from_origin_to_each_node"] = b5['distances']
    b6["predecessors_set"] = b5['predecessors']
    return b6
def fonk5(b6):
    b7 = b6["instance"].replace("\\", "-")
    with open('./reports/' + b7 + 'b6.txt', 'w') as file:
        for key, value in b6.items():
            file.write('%s:%s\n' % (key, value))
        print("Completed Report for ", b7)
def fonk6():
    print("-----------------------------------------------------------------------------------------------------")
if b8 = = "__main__":
    fonk1()
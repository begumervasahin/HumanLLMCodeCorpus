from ordered_linked_list.ordered_linked_list import LinkedList
from logger.b2 import Timer
from graph_handler.edge import Edge
from graph_handler.vertex import Vertex
from graph_handler.b4 import Graph
from dijkstra.closest_path import DijkstraArray
from b1.b1 import Data_Loader
import gc
def fonk1():
    b1 = Data_Loader()
    b2 = Timer()
    b3 = b1.load_data('./problematic-data')
    for graph_data in b3:
        b4 = fonk2(graph_data)
        fonk5()
        execution_result, b5 = fonk3(b4, b2)
        fonk4(b4, execution_result, b5)
        gc.collect()
def fonk2(graph_data):
    b4 = Graph(Vertex(graph_data['entry']), graph_data['name'], graph_data['path'])
    for edge_data in graph_data['edges']:
        b6 = Vertex(edge_data['origin'])
        b7 = Vertex(edge_data['end'])
        b8 = edge_data['weight']
        b4.add_new_connection(b6, b8, b7)
    return b4
def fonk3(b4, b2):
    b2.start()
    b9 = DijkstraArray(b4.get_representation()['struct'], b4.get_entry().get_data(), None)
    b2.end()
    b5 = b2.get_timer_difference()
    return b9, b5
def fonk4(b4, execution_result, b5):
    b10 = {
        "strategy": "using array",
        "instance": b4.get_representation()['label'],
        "number_of_nodes": len(b4.get_vertices()),
        "number_of_edges": b4.get_num_edges(),
        "time_spent_in_milliseconds": b5,
        "origin_node": b4.get_entry().get_data().get_data(),
        "distance_from_origin_to_each_node": execution_result['distances'],
        "predecessors_set": execution_result['predecessors']
    }
    b11 = b10["instance"].replace("\\", "-")
    with open(f'./reports/{b11}b10.txt', 'w') as file:
        for key, value in b10.items():
            file.write(f'{key}:{value}\n')
        print("Completed Report for", b11)
def fonk5():
    print("-----------------------------------------------------------------------------------------------------")
if b12 = = "__main__":
    fonk1()
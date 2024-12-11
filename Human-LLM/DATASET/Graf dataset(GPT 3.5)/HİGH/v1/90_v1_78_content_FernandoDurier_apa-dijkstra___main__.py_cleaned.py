from ordered_linked_list.ordered_linked_list import *
from logger.timer import *
from graph_handler.edge import *
from graph_handler.vertrix import *
from graph_handler.graph import *
from dijkstra.closest_path import *
from dijkstra.closest_path_using_array import *
from data_loader.data_loader import *
import json
import ntpath
import gc
def fonk1():
    b1 = []
    b2 = Data_Loader()
    b3 = Timer()
    b4 = Timer()
    b5 = b2.loadData('./problematic-data')
    for i in b5:
        b6 = Graph(Vertrix(i['entry']), i['name'], i['path'])
        for tup in i['edges']:
            b6.addNewConnection(Vertrix(tup['origin']), tup['weigth'], Vertrix(tup['end']))
        print("-----------------------------------------------------------------------------------------------------")
        b7 = b6
        b3.set_timer_start()
        print("-----------------------------------------------------------------------------------------------------")
        b8 = b7.getRepresentation()
        b9 = DijkstraArray(b7.getRepresentation()['struct'], b7.getEntry().getData(), None)
        b3.set_timer_end()
        b10 = {}
        b10["strategy"] = "using array"
        b10["instance"] = b8['label']
        b10["number_of_nodes"] = len(b7.getVertrixes())
        b10["number_of_edges"] = b7.getQuantityOfEdges()
        b10["time_spent_in_miliseconds"] = b3.get_timer_difference()
        b11 = b7.getEntry()
        b10["origin_node"] = b11.getData().getData()
        b10["distance_from_origin_to_each_node"] = b9['distances']
        b10["predecessors_set"] = b9['predecessors']
        b12 = b8['label'].replace("\\", "-")
        with open('./reports/'+b12+'b10.txt', 'w') as file:
            for key, value in b10.items():
                file.write('%s:%s\n' % (key, value))
            print("Completed Report for ", b12)
        gc.collect()
if b13 = = "__main__":
    fonk1()
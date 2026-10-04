import time
import networkx as nx
from filaprioritaria import PriorityQueue
import sys
def fonk1(b9, b11, b12):
    b1 = list()
    for node in b9:
        b9.nodes[node]['distance'] = sys.maxsize
        b9.nodes[node]['rotulado'] = False
    b9.nodes[b11]['distance']= 0
    b2 = PriorityQueue()
    for node in list(b9):
        b2.insert((b9.nodes[node]['distance'], node))
    while b2.getTamanho()!=0:
        b3 = b2.remove_min()
        b4 = b3[1]
        b9.nodes[b4]['rotulado']=True
        b1.append(b3)
        for j in list(b9.successors(b4)):
            if not b9.nodes[j]['rotulado']:
                b5 = b9.nodes[b4]['distance'] + b9.edges[b4, j]['weight']
                if b5 < b9.nodes[j]['distance']:
                    b9.nodes[j]['distance'] = b5
                    b9.nodes[j]['precedente'] = b4
                    b2.increase_key(j, b5)
    b6 = b9.nodes[b12]['distance']
    b7 = b12
    b8 = [{'peso':b6}]
    while True:
        try:
            b8.append(b7)
            b7 = b9.nodes[b7]['precedente']
        except:
            break
    return b8[::-1]
def fonk2():
    b9 = nx.DiGraph()
    b9.add_nodes_from(range(1, 10))
    b9.add_edges_from([(1,2,{'weight':11}),(1,3,{'weight':9}),(2,4,{'weight':4}),\
                        (2,5,{'weight':8}), (3,4,{'weight':8}), (3,5,{'weight':6}), \
                        (4,6,{'weight':6}),(4,7,{'weight':5}), (5,7,{'weight':6}),\
                        (5,8,{'weight':4}), (6,9,{'weight':6}),(7,9,{'weight':4}), (8,9,{'weight':6})])
    print("Nodes\n", b9.nodes())
    print("Edges\n", b9.edges(b10 = True))
    b11 = input("Digite o vÃ©rtice b11: ")
    try:
        b11 = int(b11)
    except():
        pass
    b12 = input("Digite o vÃ©rtice b12: ")
    try:
        b12 = int(b12)
    except():
        pass
    if b11 in b9:
        if b12 in b9:
            b13 = time.time()
            b8 = fonk1(b9, b11, b12)
            b14 = time.time()-b13
            print("Algoritmo dijkstra executado em ", b14,"segundos.")
            print("Caminho Minimo: ", b8)
        else:
            print("O vÃ©rtice b12 nÃ£o estÃ¡ no grafo")
    else:
        print("O vÃ©rtice b11 nÃ£o estÃ¡ no grafo")
if b15 = ="__main__":
    fonk2()
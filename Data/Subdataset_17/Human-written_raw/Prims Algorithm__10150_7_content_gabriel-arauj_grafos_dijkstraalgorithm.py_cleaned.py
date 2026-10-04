import time
import networkx as nx
from filaprioritaria import PriorityQueue
import sys
def dijkstra(digrafo, fonte, destino):
    r_dist = list()
    for node in digrafo:
        digrafo.nodes[node]['distance'] = sys.maxsize
        digrafo.nodes[node]['rotulado'] = False
    digrafo.nodes[fonte]['distance']= 0
    nr = PriorityQueue()
    for node in list(digrafo):
        nr.insert((digrafo.nodes[node]['distance'], node))
    while nr.getTamanho()!=0:
        u = nr.remove_min()
        k = u[1]
        digrafo.nodes[k]['rotulado']=True
        r_dist.append(u)
        for j in list(digrafo.successors(k)):
            if not digrafo.nodes[j]['rotulado']:
                novo_custo = digrafo.nodes[k]['distance'] + digrafo.edges[k, j]['weight']
                if novo_custo < digrafo.nodes[j]['distance']:
                    digrafo.nodes[j]['distance'] = novo_custo
                    digrafo.nodes[j]['precedente'] = k
                    nr.increase_key(j, novo_custo)
    z = digrafo.nodes[destino]['distance']
    i = destino
    caminho_minimo = [{'peso':z}]
    while True:
        try:
            caminho_minimo.append(i)
            i = digrafo.nodes[i]['precedente']
        except:
            break
    return caminho_minimo[::-1]
def teste():
    digrafo = nx.DiGraph()
    digrafo.add_nodes_from(range(1, 10))
    digrafo.add_edges_from([(1,2,{'weight':11}),(1,3,{'weight':9}),(2,4,{'weight':4}),\
                        (2,5,{'weight':8}), (3,4,{'weight':8}), (3,5,{'weight':6}), \
                        (4,6,{'weight':6}),(4,7,{'weight':5}), (5,7,{'weight':6}),\
                        (5,8,{'weight':4}), (6,9,{'weight':6}),(7,9,{'weight':4}), (8,9,{'weight':6})])
    print("Nodes\n", digrafo.nodes())
    print("Edges\n", digrafo.edges(data=True))
    fonte = input("Digite o vÃ©rtice fonte: ")
    try:
        fonte = int(fonte)
    except():
        pass
    destino = input("Digite o vÃ©rtice destino: ")
    try:
        destino = int(destino)
    except():
        pass
    if fonte in digrafo:
        if destino in digrafo:
            start= time.time()
            caminho_minimo=dijkstra(digrafo, fonte, destino)
            tempo = time.time()-start
            print("Algoritmo dijkstra executado em ", tempo,"segundos.")
            print("Caminho Minimo: ", caminho_minimo)
        else:
            print("O vÃ©rtice destino nÃ£o estÃ¡ no grafo")
    else:
        print("O vÃ©rtice fonte nÃ£o estÃ¡ no grafo")
if __name__=="__main__":
    teste()
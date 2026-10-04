from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
" > Funciones"
def Floydwarshall(graph):
    matrizfloyd=deepcopy(graph)
    V=len(graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                aux=matrizfloyd[i][k]+matrizfloyd[k][j]
                if (matrizfloyd[i][j]>aux):
                    matrizfloyd[i][j]=aux
    return matrizfloyd
def imprimir(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            print(graph[i][j], " , ")
        print("")
def pedirdatos():
    INF  = 99999
    g=nx.DiGraph()
    print("Crear Matriz De Adyacencia")
    V= int(input("Cantidad de vertices: "))
    graph = []
    for v1 in range(V):
        graph.append([])
        print(graph)
        for v2 in range(V):
            if v1 == v2:
                graph[v2].append(0)
            else:
                print("Distancia de: ", v1+1, "-", v2+1, " : ")
                aux=input()
                if aux == '':
                    distancia = INF
                else:
                    distancia = int(aux)
                    g.add_edge(v1,v2,weight=aux)
                graph[v1].append(distancia)
    return graph,g
matriz,g=pedirdatos()
matriz=Floydwarshall(matriz)
print(matriz)
nx.draw(g,with_labels=True)
plt.show()
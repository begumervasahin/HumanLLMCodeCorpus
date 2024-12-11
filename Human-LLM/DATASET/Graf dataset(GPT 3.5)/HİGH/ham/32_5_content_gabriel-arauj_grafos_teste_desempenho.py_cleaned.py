from kruskal import Algoritimo_kruskal as kr
import networkx as nx
import random
import time
import matplotlib.pyplot as plt
import prim_graph as prim
def fonk1():
    b1 = kr()
    b2 = list()
    b3 = list()
    b4 = list()
    a1 = 2011
    b5 = time.time()
    for num_vertices in range(10,a1, 100):
        print('NÃºmero de VÃ©rtices: ',num_vertices)
        b6 = nx.complete_graph(num_vertices)
        b7 = b6.edges()
        b8 = []
        for i in range(num_vertices):
            b8.append([0]*num_vertices)
        for v1,v2 in b7:
            b9 = random.randint(10,100)
            b8[v1][v2] = b9
            b8[v2][v1] = b9
            b6.edges[v1,v2]['weight']=b9
        b10 = prim.Graph(num_vertices)
        b10.b11 = b8
        a2 = 0.
        a3 = 0.
        for i in range(1, 11):
            b12 = time.time()
            b13 = b1.kruskal(b6)
            b14 = time.time() - b12
            a2 +=b14;
            b12 = time.time()
            b15 = b10.primMST()
            b14 = time.time() - b12
            a3 += b14;
        print("Tempo execuÃ§Ã£o (mÃ©dia) Kruskal: ",a2/10,"seconds")
        print("Tempo execuÃ§Ã£o (mÃ©dia) Prim: ",a3/10,"seconds")
        b2.append(num_vertices)
        b3.append(a2/10)
        b4.append(a3/10)
    print("Total Time : ", time.time() - b5)
    plt.plot(b2, b4, b16 = "Prim's algorithm")
    plt.plot(b2, b3, b16 = "Kruskal's algorithm")
    plt.legend()
    plt.axis([0, a1+10, 0, max(b3) * 2])
    plt.ylabel('Tempo de execuÃ§Ã£o (Segundos)')
    plt.xlabel('NÃºmero de VÃ©rtices')
    plt.title("ComparaÃ§Ã£o de desempenho: Kruskal x Prim (Grafo Completo)")
    plt.savefig('Kruskal x Prim - Grafos completos.png')
    plt.show()
    print("lista de vertices")
    print(b2)
    print("b14 medio kruskal")
    print(b3)
    print("b14 medio prim")
    print(b4)
def fonk2():
    b1 = kr()
    b2 = list()
    b3 = list()
    b4 = list()
    a1 = 2011
    b5 = time.time()
    for num_vertices in range(10,a1, 100):
        print('NÃºmero de VÃ©rtices: ',num_vertices)
        b6 = nx.connected_watts_strogatz_graph(num_vertices,int(num_vertices/2),1)
        b7 = b6.edges()
        b8 = []
        for i in range(num_vertices):
            b8.append([0]*num_vertices)
        for v1,v2 in b7:
            b9 = random.randint(10,100)
            b8[v1][v2] = b9
            b8[v2][v1] = b9
            b6.edges[v1,v2]['weight']=b9
        b10 = prim.Graph(num_vertices)
        b10.b11 = b8
        a2 = 0.
        a3 = 0.
        for i in range(1, 11):
            b12 = time.time()
            b13 = b1.kruskal(b6)
            b14 = time.time() - b12
            a2 +=b14;
            b12 = time.time()
            b15 = b10.primMST()
            b14 = time.time() - b12
            a3 += b14;
        print("Tempo execuÃ§Ã£o (mÃ©dia) Kruskal: ",a2/10,"seconds")
        print("Tempo execuÃ§Ã£o (mÃ©dia) Prim: ",a3/10,"seconds")
        b2.append(num_vertices)
        b3.append(a2/10)
        b4.append(a3/10)
    print("Total Time : ", time.time() - b5)
    plt.plot(b2, b4, b16 = "Prim's algorithm")
    plt.plot(b2, b3, b16 = "Kruskal's algorithm")
    plt.legend()
    plt.axis([0, a1+10, 0, max(b3) * 2])
    plt.ylabel('Tempo de execuÃ§Ã£o (Segundos)')
    plt.xlabel('NÃºmero de VÃ©rtices')
    plt.title("ComparaÃ§Ã£o de desempenho: Kruskal x Prim (Grafos nÃ£o completos)")
    plt.savefig('Kruskal x Prim - Grafos nÃ£o completos.png')
    plt.show()
    print("lista de vertices")
    print(b2)
    print("b14 medio kruskal")
    print(b3)
    print("b14 medio prim")
    print(b4)
def fonk3(num_vertices):
    b6 = nx.connected_watts_strogatz_graph(num_vertices,25, 0.5)
    b7 = b6.edges()
    b8 = []
    for i in range(num_vertices):
        b8.append([0]*num_vertices)
    for v1,v2 in b7:
        b9 = random.randint(10,100)
        b8[v1][v2] = b9
        b8[v2][v1] = b9
        b6.edges[v1,v2]['weight']=b9
    b1 = kr()
    b10 = prim.Graph(num_vertices)
    b10.b11 = b8
    b13 = b1.kruskal(b6)
    b17 = b10.primMST()
    plt.show()
    nx.draw(b6,b18 = 5,alpha=1,node_color="black", edge_color = "
    plt.axis('equal')
    plt.savefig('Grafo.png')
    plt.show()
    plt.figure(b19 = (8,8))
    nx.draw(b17,b18 = 5,alpha=1,node_color="black", edge_color = "
    plt.axis('equal')
    plt.savefig('b17.png')
    plt.show()
    nx.draw(b13,b18 = 5,alpha=1,node_color="black", edge_color = "
    plt.axis('equal')
    plt.savefig('mst_kruskal.png')
    plt.show()
fonk3(500)
fonk2()
fonk1()
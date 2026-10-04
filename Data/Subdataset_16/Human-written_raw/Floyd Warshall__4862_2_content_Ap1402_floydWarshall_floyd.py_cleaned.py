from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
" > Funciones"
def fonk1(b5):
    b1 = deepcopy(b5)
    b2 = len(b5)
    for k in range(b2):
        for i in range(b2):
            for j in range(b2):
                b3 = b1[i][k]+b1[k][j]
                if (b1[i][j]>b3):
                    b1[i][j]=b3
    return b1
def fonk2(b5):
    for i in range(len(b5)):
        for j in range(len(b5[i])):
            print(b5[i][j], " , ")
        print("")
def fonk3():
    a1 = 99999
    b4 = nx.DiGraph()
    print("Crear Matriz De Adyacencia")
    b2 = int(input("Cantidad de vertices: "))
    b5 = []
    for b6 in range(b2):
        b5.append([])
        print(b5)
        for v2 in range(b2):
            if b6 = = v2:
                b5[v2].append(0)
            else:
                print("Distancia de: ", b6+1, "-", v2+1, " : ")
                b3 = input()
                if b3 = = '':
                    a2 = a1
                else:
                    a2 = int(b3)
                    b4.add_edge(b6,v2,b7 = b3)
                b5[b6].append(a2)
    return b5,b4
b8,b4 = fonk3()
b8 = fonk1(b8)
print(b8)
nx.draw(b4,b9 = True)
plt.show()
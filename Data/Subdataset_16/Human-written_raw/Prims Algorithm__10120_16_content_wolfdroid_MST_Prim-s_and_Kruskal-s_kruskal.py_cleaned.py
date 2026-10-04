import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b26):
    b1 = []
    b1.append(b26[0])
    b2 = b26[0]
    for i in range(1, len(b26)):
        b3 = b26[i][2]
        a1 = 0
        while b3 > b1[a1][2] and a1 < len(b1) -1:
            a1 += 1
        b1.insert(a1 , b26[i])
    b4 = b1[len(b1)-1]
    b1.remove(b1[len(b1)-1])
    a1 = 0
    while b4[2] > b1[a1][2] and a1 < len(b1) -1:
        a1 += 1
    b1.insert(a1 , b4)
    return b1
def fonk2(b5, b7):
    while b5 != b7[b5]:
        b5 = b7[b5]
    return b5
def fonk3(b7, b12, b11, b8):
    if(b8[b12] > b8[b11]):
        b7[b11] = b12
    elif(b8[b12] < b8[b11]):
        b7[b12] = b11
    else:
        b7[b11] = b12
        b8[b12] += 1
def fonk4(b26):
    b6 = []
    b1 = fonk1(b26)
    b7 = []
    b8 = []
    for e in range(b25):
        b7.append(e)
        b8.append(0)
    a2 = 0
    a3 = 0
    while a2 < (b25 - 1):
        b9 = b1[a3][0]
        b10 = b1[a3][1]
        a3 += 1
        b11 = fonk2(b9, b7)
        b12 = fonk2(b10, b7)
        if b12 != b11:
            a2 = a2 +1
            b6.append([b9, b10, b1[a3][2]])
            fonk3(b7, b12, b11, b8)
    return b6
def fonk5( b6 ):
    b13 = nx.Graph()
    for i in range( len( b6 ) ):
        b13.add_edge(
                b24[b6[i][0]],
                b24[b6[i][1]],
                b14 = int( b6[i][2] )
                )
    b15 = [( b10,b9 ) for ( b10,b9,d ) in b13.edges( data=True )]
    b16 = nx.spring_layout( b13, a3=20, pos=None, fixed=None, iterations=150, b14='b14', scale=1.0 )
    b14 = dict( map( lambda x:( ( x[0],x[1] ), str( x[2]['b14'] ) ), b13.edges( data = True ) ) )
    nx.draw_networkx_edge_labels(b13, b16, b17 = b14)
    a4 = 0
    for i in range(b25):
        if len( b24[i] ) > a4:
            a4 = len( b24 )
    nx.draw_networkx_nodes( b13, b16, b18 = a4 * 180,  node_color='
    nx.draw_networkx_edges( b13, b16, b19 = b15, width=2, edge_color='black', alpha=0.5 )
    nx.draw_networkx_labels( b13, b16, b20 = 9, font_family='sans-serif' )
    plt.axis('off')
    plt.show()
b21 = sys.argv[1]
b22 = set()
with open( b21 ) as f:
   for a in f:
       b23 = a.strip().split(' ')
       b22.add(b23[0])
       b22.add(b23[1])
f.close()
b24 = list( b22 )
b25 = ( len( b22 ) )
b26 = []
with open(b21) as f:
   for i in f:
        b23 = i.strip().split(' ')
        b26.append([
            int(b24.index(b23[0])),
            int(b24.index(b23[1])),
            int(b23[2])])
f.close()
b6 = fonk4(b26)
a5 = 0
print("The minimum spanning tree : ")
for a in range( len( b6 ) ):
    print( b24[b6[a][0]], " to ", b24[b6[a][1]], " = ", b6[a][2], " units.")
    a5 += b6[a][2]
print("a5 b14: ", a5, " units.")
fonk5(b6)
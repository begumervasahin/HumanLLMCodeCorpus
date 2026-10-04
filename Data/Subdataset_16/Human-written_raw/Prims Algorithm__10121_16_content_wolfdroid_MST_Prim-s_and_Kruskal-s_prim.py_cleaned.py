import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1( b18 ):
    b1 = []
    b2 = []
    b3 = []
    b4 = [0, 1, b18[0][1]]
    a1 = 0
    for V in range( b17 - 1 ):
        b2.append(a1)
        for u in range(b17):
            if b18[a1][u] != 0:
                b3.append([a1, u, b18[a1][u]])
        for e in range(1, len(b3)):
            if b3[e][2] < b4[2] and b3[e][1] not in b2:
                b4 = b3[e]
        b1.append( b4 )
        a1 = b4[1]
        b3.remove( b4 )
        b4 = b3[0]
    return b1
def fonk2( b1 ):
    b5 = nx.Graph()
    for i in range( len( b1 ) ):
        b5.add_edge(
                b16[b1[i][0]],
                b16[b1[i][1]],
                b6 = int( b1[i][2] )
                )
    b7 = [( u,a1 ) for ( u,a1,d ) in b5.edges( data=True )]
    b8 = nx.spring_layout( b5, k=20, pos=None, fixed=None, iterations=150, b6='b6', scale=1.0 )
    b6 = dict( map( lambda x:( ( x[0],x[1] ), str( x[2]['b6'] ) ), b5.edges( data = True ) ) )
    nx.draw_networkx_edge_labels(b5, b8, b9 = b6)
    a2 = 0
    for i in range(b17):
        if len( b16[i] ) > a2:
            a2 = len( b16 )
    nx.draw_networkx_nodes( b5, b8, b10 = a2 * 180,  node_color='
    nx.draw_networkx_edges( b5, b8, b11 = b7, width=2, edge_color='black', alpha=0.5 )
    nx.draw_networkx_labels( b5, b8, b12 = 9, font_family='sans-serif' )
    plt.axis('off')
    plt.show()
b13 = sys.argv[1]
b14 = set()
with open( b13 ) as f:
   for a in f:
       b15 = a.strip().split(' ')
       b14.add(b15[0])
       b14.add(b15[1])
f.close()
b16 = list( b14 )
b17 = ( len( b14 ) )
b18 = [[0 for i in range( b17 )] for j in range( b17 )]
with open( b13 ) as f:
   for i in f:
       b15 = i.strip().split(' ')
       b18[int( b16.index(b15[0] ) )][int( b16.index( b15[1] ) )] = int( b15[2] )
       b18[int( b16.index(b15[1] ) )][int( b16.index( b15[0] ) )] = int( b15[2] )
f.close()
b1 = fonk1(b18)
a3 = 0
print("The minimum spanning tree : ")
for a in range( len( b1 ) ):
    print( b16[b1[a][0]], " to ", b16[b1[a][1]], " = ", b1[a][2], " units.")
    a3 += b1[a][2]
print("a3 b6: ", a3, " units.")
fonk2(b1)
import matplotlib.pyplot as plt
import networkx as nx
import sys
def prim( weighted_graph ):
    listMST = []
    visited = []
    edge_list = []
    min_edge = [0, 1, weighted_graph[0][1]]
    v = 0
    for V in range( vert_cout - 1 ):
        visited.append(v)
        for u in range(vert_cout):
            if weighted_graph[v][u] != 0:
                edge_list.append([v, u, weighted_graph[v][u]])
        for e in range(1, len(edge_list)):
            if edge_list[e][2] < min_edge[2] and edge_list[e][1] not in visited:
                min_edge = edge_list[e]
        listMST.append( min_edge )
        v = min_edge[1]
        edge_list.remove( min_edge )
        min_edge = edge_list[0]
    return listMST
def dGraph( listMST ):
    G = nx.Graph()
    for i in range( len( listMST ) ):
        G.add_edge(
                vert_list[listMST[i][0]],
                vert_list[listMST[i][1]],
                weight = int( listMST[i][2] )
                )
    edge=[( u,v ) for ( u,v,d ) in G.edges( data=True )]
    position=nx.spring_layout( G, k=20, pos=None, fixed=None, iterations=150, weight='weight', scale=1.0 )
    weight = dict( map( lambda x:( ( x[0],x[1] ), str( x[2]['weight'] ) ), G.edges( data = True ) ) )
    nx.draw_networkx_edge_labels(G, position, edge_labels = weight)
    node_len = 0
    for i in range(vert_cout):
        if len( vert_list[i] ) > node_len:
            node_len = len( vert_list )
    nx.draw_networkx_nodes( G, position, node_size=node_len * 180,  node_color='
    nx.draw_networkx_edges( G, position, edgelist=edge, width=2, edge_color='black', alpha=0.5 )
    nx.draw_networkx_labels( G, position, font_size=9, font_family='sans-serif' )
    plt.axis('off')
    plt.show()
file_name = sys.argv[1]
vert_set = set()
with open( file_name ) as f:
   for a in f:
       column = a.strip().split(' ')
       vert_set.add(column[0])
       vert_set.add(column[1])
f.close()
vert_list = list( vert_set )
vert_cout = ( len( vert_set ) )
weighted_graph = [[0 for i in range( vert_cout )] for j in range( vert_cout )]
with open( file_name ) as f:
   for i in f:
       column = i.strip().split(' ')
       weighted_graph[int( vert_list.index(column[0] ) )][int( vert_list.index( column[1] ) )] = int( column[2] )
       weighted_graph[int( vert_list.index(column[1] ) )][int( vert_list.index( column[0] ) )] = int( column[2] )
f.close()
listMST =  prim(weighted_graph)
total = 0
print("The minimum spanning tree : ")
for a in range( len( listMST ) ):
    print( vert_list[listMST[a][0]], " to ", vert_list[listMST[a][1]], " = ", listMST[a][2], " units.")
    total += listMST[a][2]
print("total weight: ", total, " units.")
dGraph(listMST)
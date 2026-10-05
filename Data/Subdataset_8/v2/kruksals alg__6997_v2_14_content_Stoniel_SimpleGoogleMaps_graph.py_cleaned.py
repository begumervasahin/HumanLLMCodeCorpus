import networkx as nx
import matplotlib.pyplot as plt
def display_graph(G):
    pos = nx.spring_layout(G)
    node_colors = [G.nodes[node]['color'] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_labels(G, pos)
    edge_colors = [G.edges[edge]['color'] for edge in G.edges()]
    weights = {(u, v): G.edges[u, v]['weight'] for u, v in G.edges()}
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.show()
def recolor_mst(mst):
    for edge in G.edges():
        G.edges[edge]['color'] = 'r'
        G.nodes[edge[0]]['color'] = 'r'
        G.nodes[edge[1]]['color'] = 'r'
    for u, v, _ in G.edges(data='weight'):
        if (u, v) in mst:
            G.edges[u, v]['color'] = 'b'
            G.nodes[u]['color'] = 'b'
            G.nodes[v]['color'] = 'b'
def dfs(mst, edge):
    visited[edge] = True
    for i in G.neighbors(edge):
        if i in mst and not visited[i]:
            parent[i] = edge
def find_cycle(mst, edge):
    visited = [False] * len(G.nodes())
    dfs(mst, edge)
def update_mst(min_tree, edge1, edge2, change):
    if (edge1, edge2) in min_tree and change > 0:
        print('Edge already present.')
    elif ((edge1, edge2) not in min_tree) and change < 0:
        min_tree.append((edge1, edge2, G[edge1][edge2]['weight']))
        del min_tree[len(min_tree) - 1]
        recolor_mst(min_tree)
    else:
        print('No changes needed.')
def find(node):
    if G.nodes[node]['pi'] == node:
        return node
    return find(G.nodes[node]['pi'])
def union(node, node1):
    root = find(node)
    root1 = find(node1)
    rank_root = G.nodes[root]['rank']
    rank_root1 = G.nodes[root1]['rank']
    if rank_root < rank_root1:
        G.nodes[root]['pi'] = root1
    elif rank_root > rank_root1:
        G.nodes[root1]['pi'] = root
    else:
        G.nodes[root1]['pi'] = root
        G.nodes[root]['rank'] += 1
def kruskal(G):
    edge_index = 0
    mst_index = 0
    sorted_edges = sorted(G.edges(data='weight'), key=lambda x: x[2])
    result = []
    for node, pi in G.nodes(data='pi'):
        G.nodes[node]['pi'] = node
    while mst_index < len(G.nodes()) - 1:
        u, v, weight = sorted_edges[edge_index]
        edge_index += 1
        parent_u = find(u)
        parent_v = find(v)
        if parent_u != parent_v:
            mst_index += 1
            result.append((u, v, weight))
            union(parent_u, parent_v)
    return result
G = nx.Graph()
nodes = ['a', 'b', 'c', 'd', 'e']
for node in nodes:
    G.add_node(node, rank=0, pi=None, color='r')
edges = [('a', 'b', 4), ('a', 'c', 3), ('a', 'd', 2), ('c', 'd', 5), ('b', 'c', 2), ('b', 'e', 9)]
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2], color='r')
MST = kruskal(G)
print("Minimum Spanning Tree:", MST)
recolor_mst(MST)
display_graph(G)
new_weight = 1
diff = new_weight - G['a']['b']['weight']
G['a']['b']['weight'] = new_weight
update_mst(MST, 'a', 'b', diff)
display_graph(G)
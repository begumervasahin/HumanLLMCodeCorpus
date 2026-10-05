43. Repository: odubno/ford-fulkerson-max-flow
   File: test_max_flow.py
   URL: https:
   Code Content:
import pytest
import networkx as nx
from max_flow import flow_with_demands
def divergence(flow):
    div = {k: 0 for k in flow.keys()}
    for node in flow.keys():
        forward_flow = sum(flow[node].values())
        backward_flow = sum(flow[i][node] for i in flow[node].keys())
        div[node] = backward_flow - forward_flow
    return div
def test_max_flow():
    G = nx.Graph()
    usa = open('contiguous-usa.dat')
    for i, line in enumerate(usa):
        s1, s2 = line.strip().split()
        G.add_edge(s1, s2)
    for state in G.nodes():
        if state != 'CA':
            G.node[state]['demand'] = 1
    G.node['CA']['demand'] = -48
    G = nx.DiGraph(G)
    uniform_capacity = 16
    for (s1, s2) in G.edges():
        G.edge[s1][s2]['capacity'] = uniform_capacity
    flow = flow_with_demands(G)
    div = divergence(flow)
    assert all(div[n] == G.node[n]['demand'] for n in G.nodes())
if __name__ == '__main__':
    test_max_flow()
   README Content:
Fulkerson uses the DFS approach and Edmonds-Karp uses the BFS approach. Towards the end of writing my algorithm I pivot to using BFS, making this algorithm actually the Edmonds-Karp approach and not the Ford Fulkerson approach.
Make sure that you're using `networkx==1.9`. See requirements.
**Bipartite Graph** -> **Directed Flow Network** -> **Maximum Flow**
1. Reduce the **Bipartite Graph** to a **Directed Flow Network** by adding a source and a sink and introduce capacity to each.
2. Use the Ford Fulkerson method and Breadth For Search to find augmenting paths and calculate the residual graph.
3. Using the residual graph, calculate the **Maximum Flow** for the original graph.
* This was a home work assignment for CSORW4246, an Algorithms course at Columbia.
- https:
- https:
- https:

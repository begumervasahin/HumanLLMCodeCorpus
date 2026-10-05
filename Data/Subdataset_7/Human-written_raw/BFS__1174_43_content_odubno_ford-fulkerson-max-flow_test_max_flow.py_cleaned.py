43. Repository: odubno/ford-fulkerson-max-b7
   File: test_max_flow.py
   URL: https:
   Code Content:
import pytest
import b9 as nx
from max_flow import flow_with_demands
def fonk1(b7):
    b1 = {k: 0 for k in b7.keys()}
    for node in b7.keys():
        b2 = sum(b7[node].values())
        b3 = sum(b7[i][node] for i in b7[node].keys())
        b1[node] = b3 - b2
    return b1
def fonk2():
    b4 = nx.Graph()
    b5 = open('contiguous-b5.dat')
    for i, line in enumerate(b5):
        s1, b6 = line.strip().split()
        b4.add_edge(s1, b6)
    for state in b4.nodes():
        if state != 'CA':
            b4.node[state]['demand'] = 1
    b4.node['CA']['demand'] = -48
    b4 = nx.DiGraph(b4)
    a1 = 16
    for (s1, b6) in b4.edges():
        b4.edge[s1][b6]['capacity'] = a1
    b7 = flow_with_demands(b4)
    b1 = fonk1(b7)
    assert all(b1[n] == b4.node[n]['demand'] for n in b4.nodes())
if b8 = = '__main__':
    fonk2()
   README Content:
Fulkerson uses the DFS approach and Edmonds-Karp uses the BFS approach. Towards the end of writing my algorithm I pivot to using BFS, making this algorithm actually the Edmonds-Karp approach and not the Ford Fulkerson approach.
Make sure that you're using `b9 = =1.9`. See requirements.
**Bipartite Graph** -> **Directed Flow Network** -> **Maximum Flow**
1. Reduce the **Bipartite Graph** to a **Directed Flow Network** by adding a source and a sink and introduce capacity to each.
2. Use the Ford Fulkerson method and Breadth For Search to find augmenting paths and calculate the residual graph.
3. Using the residual graph, calculate the **Maximum Flow** for the original graph.
* This was a home work assignment for CSORW4246, an Algorithms course at Columbia.
- https:
- https:
- https:

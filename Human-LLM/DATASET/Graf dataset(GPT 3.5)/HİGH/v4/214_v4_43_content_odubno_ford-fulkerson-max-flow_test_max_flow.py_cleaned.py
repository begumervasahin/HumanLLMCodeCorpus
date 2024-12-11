
import pytest
import networkx as nx
from max_flow import flow_with_demands
def fonk1(b6):
    b1 = {k: 0 for k in b6.keys()}
    for node in b6.keys():
        b2 = sum(b6[node].values())
        b3 = sum(b6[i][node] for i in b6[node].keys())
        b1[node] = b3 - b2
    return b1
def fonk2():
    b4 = nx.Graph()
    with open('contiguous-usa.dat') as usa:
        for i, line in enumerate(usa):
            s1, b5 = line.strip().split()
            b4.add_edge(s1, b5)
    for state in b4.nodes():
        if state != 'CA':
            b4.node[state]['demand'] = 1
    b4.node['CA']['demand'] = -48
    b4 = nx.DiGraph(b4)
    a1 = 16
    for (s1, b5) in b4.edges():
        b4.edge[s1][b5]['capacity'] = a1
    b6 = flow_with_demands(b4)
    b1 = fonk1(b6)
    assert all(b1[n] == b4.node[n]['demand'] for n in b4.nodes())
if b7 = = '__main__':
    fonk2()
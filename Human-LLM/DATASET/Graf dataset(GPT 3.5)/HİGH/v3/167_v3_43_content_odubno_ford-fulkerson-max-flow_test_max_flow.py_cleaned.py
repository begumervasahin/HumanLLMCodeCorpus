import pytest
import networkx as nx
from max_flow import flow_with_demands
def fonk1(b6):
    b1 = {node: 0 for node in b6}
    for node in b6:
        b2 = sum(b6[node].values())
        b3 = sum(b6[neighbor][node] for neighbor in b6[node])
        b1[node] = b3 - b2
    return b1
def fonk2():
    b4 = nx.Graph()
    with open('contiguous-usa.dat') as usa:
        for line in usa:
            s1, b5 = line.strip().split()
            b4.add_edge(s1, b5)
    for state in b4.nodes():
        if state != 'CA':
            b4.nodes[state]['demand'] = 1
    b4.nodes['CA']['demand'] = -48
    b4 = nx.DiGraph(b4)
    a1 = 16
    for s1, b5 in b4.edges():
        b4.edges[s1, b5]['capacity'] = a1
    b6 = flow_with_demands(b4)
    b1 = fonk1(b6)
    assert all(b1[node] == b4.nodes[node]['demand'] for node in b4.nodes())
if b7 = = '__main__':
    fonk2()
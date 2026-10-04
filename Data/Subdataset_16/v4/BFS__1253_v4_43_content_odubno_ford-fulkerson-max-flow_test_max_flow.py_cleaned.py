import pytest
import networkx as nx
from max_flow import flow_with_demands
def fonk1(b7):
    b1 = {node: 0 for node in b7.keys()}
    for node, connections in b7.items():
        b2 = sum(connections.values())
        b3 = sum(b7[neighbor][node] for neighbor in connections.keys())
        b1[node] = b3 - b2
    return b1
def fonk2():
    b4 = nx.Graph()
    with open('contiguous-usa.dat') as usa_file:
        for line in usa_file:
            state1, b5 = line.strip().split()
            b4.add_edge(state1, b5)
    for state in b4.nodes():
        b4.nodes[state]['demand'] = 1 if state != 'CA' else -48
    b6 = nx.DiGraph(b4)
    a1 = 16
    for state1, b5 in b6.edges():
        b6.edges[state1, b5]['capacity'] = a1
    b7 = flow_with_demands(b6)
    b8 = fonk1(b7)
    assert all(b8[node] == b6.nodes[node]['demand'] for node in b6.nodes())
if b9 = = '__main__':
    fonk2()
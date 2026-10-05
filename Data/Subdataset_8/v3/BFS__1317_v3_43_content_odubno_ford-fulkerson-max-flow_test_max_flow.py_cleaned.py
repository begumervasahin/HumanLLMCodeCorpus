import pytest
import networkx as nx
from max_flow import flow_with_demands
def divergence(flow):
    div = {node: 0 for node in flow}
    for node in flow:
        forward_flow = sum(flow[node].values())
        backward_flow = sum(flow[neighbor][node] for neighbor in flow[node])
        div[node] = backward_flow - forward_flow
    return div
def test_max_flow():
    G = nx.Graph()
    with open('contiguous-usa.dat') as usa:
        for line in usa:
            s1, s2 = line.strip().split()
            G.add_edge(s1, s2)
    for state in G.nodes():
        if state != 'CA':
            G.nodes[state]['demand'] = 1
    G.nodes['CA']['demand'] = -48
    G = nx.DiGraph(G)
    uniform_capacity = 16
    for s1, s2 in G.edges():
        G.edges[s1, s2]['capacity'] = uniform_capacity
    flow = flow_with_demands(G)
    div = divergence(flow)
    assert all(div[node] == G.nodes[node]['demand'] for node in G.nodes())
if __name__ == '__main__':
    test_max_flow()
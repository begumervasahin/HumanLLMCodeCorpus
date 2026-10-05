import pytest
import networkx as nx
from max_flow import flow_with_demands
def compute_divergence(flow):
    divergence = {node: 0 for node in flow}
    for node in flow:
        forward_flow = sum(flow[node].values())
        backward_flow = sum(flow[neighbor][node] for neighbor in flow[node])
        divergence[node] = backward_flow - forward_flow
    return divergence
def test_max_flow():
    G = nx.Graph()
    with open('contiguous-usa.dat') as usa_file:
        for line in usa_file:
            source, destination = line.strip().split()
            G.add_edge(source, destination)
    for state in G.nodes():
        if state != 'CA':
            G.nodes[state]['demand'] = 1
    G.nodes['CA']['demand'] = -48
    G = nx.DiGraph(G)
    uniform_capacity = 16
    for source, destination in G.edges():
        G.edges[source, destination]['capacity'] = uniform_capacity
    flow = flow_with_demands(G)
    divergence = compute_divergence(flow)
    assert all(divergence[node] == G.nodes[node]['demand'] for node in G.nodes())
if __name__ == '__main__':
    test_max_flow()
import pytest
import networkx as nx
from max_flow import flow_with_demands
def compute_divergence(flow):
    divergence = {node: 0 for node in flow.keys()}
    for node, connections in flow.items():
        forward_flow = sum(connections.values())
        backward_flow = sum(flow[neighbor][node] for neighbor in connections.keys())
        divergence[node] = backward_flow - forward_flow
    return divergence
def test_max_flow():
    graph = nx.Graph()
    with open('contiguous-usa.dat') as usa_file:
        for line in usa_file:
            state1, state2 = line.strip().split()
            graph.add_edge(state1, state2)
    for state in graph.nodes():
        graph.nodes[state]['demand'] = 1 if state != 'CA' else -48
    directed_graph = nx.DiGraph(graph)
    uniform_capacity = 16
    for state1, state2 in directed_graph.edges():
        directed_graph.edges[state1, state2]['capacity'] = uniform_capacity
    flow = flow_with_demands(directed_graph)
    div = compute_divergence(flow)
    for node in directed_graph.nodes():
        assert div[node] == directed_graph.nodes[node]['demand'], f"Node {node} has incorrect divergence"
if __name__ == '__main__':
    test_max_flow()
import networkx as nx
def bfs_capacity_path(G, source, sink, parent):
    visited = set()
    queue = [source]
    visited.add(source)
    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if v not in visited and G[u][v]['capacity'] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False
def ford_fulkerson(G, source, sink):
    parent = {node: -1 for node in G}
    max_flow = 0
    while bfs_capacity_path(G, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, G[parent[s]][s]['capacity'])
            s = parent[s]
        v = sink
        while v != source:
            u = parent[v]
            G[u][v]['capacity'] -= path_flow
            if G.has_edge(v, u):
                G[v][u]['capacity'] += path_flow
            else:
                G.add_edge(v, u, capacity=path_flow)
            v = parent[v]
        max_flow += path_flow
    return max_flow
def create_bipartite_graph():
    G = nx.Graph()
    usa = [
        'AL MS', 'AR LA', 'AR MO', 'AR OK', 'AR TN', 'AZ CA', 'AZ NM', 'AZ NV', 'AZ UT',
        'CA NV', 'CA OR', 'CO KS', 'CO NE', 'CO NM', 'CO OK', 'CO UT', 'CO WY', 'CT MA',
        'CT NY', 'DC MD', 'DC VA', 'DE MD', 'DE NJ', 'DE PA', 'FL AL', 'FL GA', 'GA AL',
        'GA FL', 'GA NC', 'GA SC', 'GA TN', 'IA IL', 'IA MN', 'IA MO', 'IA NE', 'IA SD',
        'ID MT', 'ID NV', 'ID OR', 'ID UT', 'ID WA', 'ID WY', 'IL IN', 'IL KY', 'IL MO',
        'IL WI', 'IN KY', 'IN MI', 'IN OH', 'KS MO', 'KS NE', 'KS OK', 'KY MO', 'KY OH',
        'KY TN', 'KY VA', 'KY WV', 'LA MS', 'LA TX', 'MA NH', 'MA NY', 'MA RI', 'MA VT',
        'MD PA', 'MD VA', 'ME NH', 'MI OH', 'MI WI', 'MN ND', 'MN SD', 'MN WI', 'MO NE',
        'MO OK', 'MO TN', 'MO AR', 'MO IA', 'MO IL', 'MO KS', 'MS TN', 'MS AL', 'MS AR',
        'MS LA', 'MT ND', 'MT SD', 'MT WY', 'NC SC', 'NC TN', 'NC VA', 'ND SD', 'ND MN',
        'NE SD', 'NE CO', 'NE IA', 'NE KS', 'NE MO', 'NE WY', 'NH VT', 'NJ NY', 'NJ PA',
        'NM OK', 'NM TX', 'NM AZ', 'NM CO', 'NV OR', 'NV UT', 'NV CA', 'NY PA', 'OH PA',
        'OH WV', 'OK TX', 'OK AR', 'OK CO', 'OK KS', 'OK MO', 'OR WA', 'PA WV', 'PA NY',
        'PA NJ', 'PA OH', 'RI CT', 'RI MA', 'SC GA', 'SC NC', 'SD WY', 'SD IA', 'SD MN',
        'SD MT', 'SD ND', 'SD NE', 'TN VA', 'TN AL', 'TN AR', 'TN GA', 'TN KY', 'TN MO',
        'TX AR', 'TX LA', 'TX NM', 'TX OK', 'UT WY', 'UT AZ', 'UT CO', 'UT ID', 'UT NV',
        'VA WV', 'VA KY', 'VA MD', 'VA NC', 'VA TN', 'VT NY', 'VT NH', 'WA ID', 'WA OR',
        'WI MI', 'WI MN', 'WI IA', 'WI IL', 'WV KY', 'WV MD', 'WV OH', 'WV PA'
    ]
    for line in usa:
        s1, s2 = line.strip().split()
        G.add_edge(s1, s2)
    return G
def convert_to_flow_network(G):
    DG = nx.DiGraph()
    for u, v in G.edges():
        DG.add_edge(u, v, capacity=16)
        DG.add_edge(v, u, capacity=0)
    for node in G.nodes():
        DG.nodes[node]['demand'] = 1 if node != 'CA' else -48
    return DG
def flow_with_demands(G):
    source = 'Source'
    sink = 'Sink'
    total_demand = 0
    for node in G.nodes():
        demand = G.nodes[node]['demand']
        if demand > 0:
            G.add_edge(source, node, capacity=demand)
            total_demand += demand
        elif demand < 0:
            G.add_edge(node, sink, capacity=-demand)
    max_flow = ford_fulkerson(G, source, sink)
    if max_flow != total_demand:
        raise Exception("Flow does not meet demand requirements")
    return {node: {nbr: G[node][nbr]['capacity'] for nbr in G[node]} for node in G.nodes()}
def test_max_flow():
    G = create_bipartite_graph()
    G = convert_to_flow_network(G)
    flow = flow_with_demands(G)
    for node in flow:
        forward_flow = sum(flow[node].values())
        backward_flow = sum(flow[nbr][node] for nbr in flow if node in flow[nbr])
        net_flow = backward_flow - forward_flow
        assert net_flow == G.nodes[node]['demand'], f"Flow mismatch at {node}: {net_flow} != {G.nodes[node]['demand']}"
if __name__ == '__main__':
    test_max_flow()
    print("All tests passed.")
import networkx as nx
def fonk1(b9, b13, b14, b5):
    b1 = set()
    b2 = [b13]
    b1.add(b13)
    while b2:
        b3 = b2.pop(0)
        for b4 in b9[b3]:
            if b4 not in b1 and b9[b3][b4]['b8'] > 0:
                b2.append(b4)
                b1.add(b4)
                b5[b4] = b3
                if b4 = = b14:
                    return True
    return False
def fonk2(b9, b13, b14):
    b5 = {node: -1 for node in b9}
    a1 = 0
    while fonk1(b9, b13, b14, b5):
        b6 = float('Inf')
        b7 = b14
        while b7 != b13:
            b6 = min(b6, b9[b5[b7]][b7]['b8'])
            b7 = b5[b7]
        b4 = b14
        while b4 != b13:
            b3 = b5[b4]
            b9[b3][b4]['b8'] -= b6
            if b9.has_edge(b4, b3):
                b9[b4][b3]['b8'] += b6
            else:
                b9.add_edge(b4, b3, b8 = b6)
            b4 = b5[b4]
        a1 += b6
    return a1
def fonk3():
    b9 = nx.Graph()
    b10 = [
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
    for line in b10:
        s1, b11 = line.strip().split()
        b9.add_edge(s1, b11)
    return b9
def fonk4(b9):
    b12 = nx.DiGraph()
    for b3, b4 in b9.edges():
        b12.add_edge(b3, b4, b8 = 16)
        b12.add_edge(b4, b3, b8 = 0)
    for node in b9.nodes():
        b12.nodes[node]['b15'] = 1 if node != 'CA' else -48
    return b12
def fonk5(b9):
    b13 = 'Source'
    b14 = 'Sink'
    a2 = 0
    for node in b9.nodes():
        b15 = b9.nodes[node]['b15']
        if b15 > 0:
            b9.add_edge(b13, node, b8 = b15)
            a2 += b15
        elif b15 < 0:
            b9.add_edge(node, b14, b8 = -b15)
    a1 = fonk2(b9, b13, b14)
    if a1 != a2:
        raise Exception("Flow does not meet b15 requirements")
    return {node: {nbr: b9[node][nbr]['b8'] for nbr in b9[node]} for node in b9.nodes()}
def fonk6():
    b9 = fonk3()
    b9 = fonk4(b9)
    b16 = fonk5(b9)
    for node in b16:
        b17 = sum(b16[node].values())
        b18 = sum(b16[nbr][node] for nbr in b16 if node in b16[nbr])
        b19 = b18 - b17
        assert b19 = = b9.nodes[node]['b15'], f"Flow mismatch at {node}: {b19} != {b9.nodes[node]['b15']}"
if b20 = = '__main__':
    fonk6()
    print("All tests passed.")
import networkx as nx
import b2 as q
import matplotlib.pyplot as plt
import sys
if len(sys.argv) > 1:
	b1 = nx.read_pajek(sys.argv[1])
else:
	b1 = nx.complete_graph(10)
def fonk1(b1, b5):
	for node in b1.node:
		b1.nodes[node]['color'] = 'white'
		b1.nodes[node]['delta'] = float('inf')
		b1.nodes[node]['pi'] = None
	b1.nodes[b5]['color'] = 'gray'
	b1.nodes[b5]['delta'] = 0
	b2 = q.Queue()
	b2.put(b5)
	while b2.qsize()!= 0:
		b3 = b2.get()
		for node in b1.neighbors(b3):
			if b1.nodes[node]['color'] == 'white':
				b1.nodes[node]['color'] = 'gray'
				b1.nodes[node]['delta'] = b1.node[b3]['delta'] + 1
				b1.nodes[node]['pi'] = b3
				b2.put(node)
		b1.nodes[b3]['color'] = 'black'
	b4 = nx.Graph()
	for node in b1.node:
		b4.add_node(node)
	for node in b1.node:
		b4.add_edge(node, b1.nodes[node]['pi'])
	return b4
if (len(sys.argv) > 2):
	b5 = sys.argv[2]
else:
	b5 = list(b1.nodes)[0]
b6 = fonk1(b1, b5)
nx.draw(b1)
plt.show()
nx.draw(b6)
plt.show()
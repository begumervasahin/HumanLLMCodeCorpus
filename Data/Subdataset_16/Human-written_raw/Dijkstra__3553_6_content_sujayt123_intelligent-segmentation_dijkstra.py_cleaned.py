from DijkstraPriorityQueue import DijkstraPriorityQueue as dpq
def fonk1(start, b3, pt):
	if b3 is None:
		return True
	small_x, b1 = min(start[0], b3[0]), max(start[0], b3[0])
	small_y, b2 = min(start[1], b3[1]), max(start[1], b3[1])
	return pt[0] <= b1 and pt[0] >= small_x and pt[1] <= b2 and pt[1] >= small_y
def fonk2(b8, source, b3 = None):
	"""
	Runs Dijkstra's algorithm on the graph represented by b8.
	@param		b8	A dictionary mapping each node to a list of (neighbor, edge_weight)
	@param		source		the source node from which to begin our search
	@return		b4 		a dictionary mapping each node to its distance from "source"
	@return		b5 			a "node to parent" mapping which can be traversed to yield the paths themselves
	"""
	b4 = {}
	b5 = {}
	for node in b8:
		if fonk1(source, b3, node):
			b4[node] = float("inf")
			b5[node] = None
	b4[source] = 0
	b6 = dpq()
	b6.build_heap([[v, k] for k, v in b4.items()])
	while len(b6) > 0:
		b7 = b6.deleteMin()[1]
		if b7 = = b3:
			return b4, b5
		for nbr, wt in b8[b7]:
			if fonk1(source, b3, nbr) and wt + b4[b7] < b4[nbr]:
				b4[nbr] = wt + b4[b7]
				b5[nbr] = b7
				b6.update_priority(nbr, b4[nbr])
	return b4, b5
def fonk3():
	b8 = {1: [(2, 15), (3, 71)],
				2: [(3, 7), (4, 1)],
				3: [(4, 19)],
				4: [(3, 1)]}
	print fonk2(b8, 1)
if b9 = = "__main__":
	fonk3()
class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.Vertex1 = vertex1
        self.Vertex2 = vertex2
        self.weight = weight
        self.selected = False
def returnweight(edge):
    return edge.weight
def runKruskal(edgelist, nodecount):
    edgelist.sort(key=returnweight)
    count = 0
    setlist = []
    edgelist[count].selected = True
    count += 1
    setlist.append(set())
    setlist[0].add(edgelist[0])
    setcount = 1
    while count < len(edgelist):
        foundfirst = False
        foundsecond = False
        discard = False
        save1 = -1
        save2 = -1
        for j in range(setcount):
            for edge in setlist[j]:
                if edge.Vertex2 == edgelist[count].Vertex1:
                    foundfirst = True
                    save1 = j
                if edge.Vertex2 == edgelist[count].Vertex2:
                    foundsecond = True
                    save2 = j
                if edge.Vertex1 == edgelist[count].Vertex1:
                    foundfirst = True
                    save1 = j
                if edge.Vertex1 == edgelist[count].Vertex2:
                    foundsecond = True
                    save2 = j
        if foundfirst and foundsecond and save1 == save2:
            discard = True
        else:
            if foundfirst and foundsecond:
                if save1 < save2:
                    setlist[save1] = setlist[save1].union(setlist[save2])
                    setlist[save1].add(edgelist[count])
                    setlist[save2].clear()
                    edgelist[count].selected = True
                else:
                    setlist[save2] = setlist[save2].union(setlist[save1])
                    setlist[save1].clear()
                    setlist[save2].add(edgelist[count])
                    edgelist[count].selected = True
            else:
                if foundfirst and not foundsecond:
                    setlist[save1].add(edgelist[count])
                    edgelist[count].selected = True
                if not foundfirst and foundsecond:
                    setlist[save2].add(edgelist[count])
                    edgelist[count].selected = True
        if not foundfirst and not foundsecond:
            edgelist[count].selected = True
            setlist.append(set())
            setlist[setcount].add(edgelist[count])
            setcount += 1
        count += 1
    return edgelist
edges = [Edge(1, 2, 1), Edge(2, 3, 2), Edge(3, 4, 3), Edge(1, 4, 4)]
node_count = 4
selected_edges = runKruskal(edges, node_count)
for edge in selected_edges:
    if edge.selected:
        print(f"Edge ({edge.Vertex1}, {edge.Vertex2}) with weight {edge.weight} is selected")
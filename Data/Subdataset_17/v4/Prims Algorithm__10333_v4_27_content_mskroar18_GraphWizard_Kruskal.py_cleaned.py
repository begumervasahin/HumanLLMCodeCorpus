class Graph:
    def runKruskal(self, edgelist, nodecount):
        edgelist.sort(key=lambda edge: edge.weight)
        count = 0
        setlist = []
        setcount = 0
        edgelist[count].selected = True
        setlist.append({edgelist[count]})
        count += 1
        setcount += 1
        while count < len(edgelist):
            edge = edgelist[count]
            foundfirst, foundsecond = False, False
            discard = False
            save1, save2 = -1, -1
            for j in range(setcount):
                for i in setlist[j]:
                    if i.Vertex2 == edge.Vertex1 or i.Vertex1 == edge.Vertex1:
                        foundfirst = True
                        save1 = j
                    if i.Vertex2 == edge.Vertex2 or i.Vertex1 == edge.Vertex2:
                        foundsecond = True
                        save2 = j
            if foundfirst and foundsecond and save1 == save2:
                discard = True
            else:
                if foundfirst and foundsecond:
                    if save1 < save2:
                        setlist[save1].update(setlist[save2])
                        setlist[save1].add(edge)
                        setlist[save2].clear()
                    else:
                        setlist[save2].update(setlist[save1])
                        setlist[save1].clear()
                        setlist[save2].add(edge)
                    edge.selected = True
                else:
                    if foundfirst and not foundsecond:
                        setlist[save1].add(edge)
                    if not foundfirst and foundsecond:
                        setlist[save2].add(edge)
                    edge.selected = True
            if not foundfirst and not foundsecond:
                edge.selected = True
                setlist.append({edge})
                setcount += 1
            count += 1
        return
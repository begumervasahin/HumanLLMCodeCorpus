class Graph:
    def runKruskal(self, edgelist, nodecount):
        edgelist.sort(key=lambda edge: edge.weight)
        selected_edges = []
        disjoint_sets = []
        def find_set(vertex):
            for index, subset in enumerate(disjoint_sets):
                if vertex in subset:
                    return index
            return -1
        for edge in edgelist:
            set1 = find_set(edge.Vertex1)
            set2 = find_set(edge.Vertex2)
            if set1 == set2 and set1 != -1:
                continue
            elif set1 == -1 and set2 == -1:
                disjoint_sets.append({edge.Vertex1, edge.Vertex2})
            elif set1 != -1 and set2 == -1:
                disjoint_sets=set1.add(edge.Vertex2)
            elif set1 == -1 and set2 != -1:
                disjoint_sets[set2].add(edge.Vertex1)
            else:
                disjoint_sets[set1].update(disjoint_sets[set2])
                disjoint_sets.pop(set2)
            edge.selected = True
            selected_edges.append(edge)
        return selected_edges
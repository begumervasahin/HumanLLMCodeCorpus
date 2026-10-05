def create_graph():
    graph = []
    with open("input", 'r') as inp:
        for line in inp:
            nameF, nameS, weight = line.strip().split(',')
            weight = int(weight)
            myelement = (nameF, [(nameS, weight)])
            graph.append(myelement)
    return graph
def get_edges(graph):
    edges = []
    for x, y_list in graph:
        for i, j in y_list:
            ttemp = (x, i, j)
            edges.append(ttemp)
    return edges
def ord_edges(edges):
    smaller = []
    greater = []
    if not edges:
        return []
    pivot = edges.pop(0)
    for (x, y, z) in edges:
        if z <= pivot[2]:
            smaller.append((x, y, z))
        else:
            greater.append((x, y, z))
    smaller = ord_edges(smaller)
    greater = ord_edges(greater)
    return smaller + [pivot] + greater
def create_classes(graph):
    vtemp = []
    for x, y_list in graph:
        vtemp.append([x])
    return vtemp
def get_class(x, vert):
    for tmp in vert:
        if x in tmp:
            return tmp
    return []
def join_classes(x, y, vert):
    class_x = get_class(x, vert)
    if y in class_x:
        return vert
    else:
        class_y = get_class(y, vert)
        vertX = remove_class(class_x, vert)
        vertY = remove_class(class_y, vertX)
        return [class_x + class_y] + vertY
def remove_class(class_x, vert):
    if not vert:
        return []
    head = vert.pop(0)
    if set(head) == set(class_x):
        return vert
    else:
        return [head] + (remove_class(class_x, vert))
def kruskal(graph):
    tree_edges = []
    edges = get_edges(graph)
    classes = create_classes(graph)
    edges = ord_edges(edges)
    for (x, y, z) in edges:
        if y in get_class(x, classes):
            tree_edges = tree_edges
        else:
            tree_edges.append((x, y, z))
            classes = join_classes(x, y, classes)
    return tree_edges
def main():
    mygraph = create_graph()
    print("Graph: \n", mygraph)
    print("\nMinimum graph: \n", kruskal(mygraph))
if __name__ == "__main__":
    main()
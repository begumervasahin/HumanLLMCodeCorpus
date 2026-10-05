def create_graph():
    graph = []
    with open("input", 'r') as inp:
        for line in inp:
            name_first, name_second, weight = line.strip().split(',')
            graph.append((name_first, [(name_second, int(weight))]))
    return graph
def get_edges(graph):
    edges = []
    for node, neighbors in graph:
        for neighbor, weight in neighbors:
            edges.append((node, neighbor, weight))
    return edges
def sort_edges(edges):
    if not edges:
        return []
    pivot = edges.pop(0)
    smaller = [(x, y, z) for x, y, z in edges if z <= pivot[2]]
    greater = [(x, y, z) for x, y, z in edges if z > pivot[2]]
    return sort_edges(smaller) + [pivot] + sort_edges(greater)
def create_classes(graph):
    classes = []
    for node, _ in graph:
        classes.append([node])
    return classes
def find_class(node, classes):
    for class_node in classes:
        if node in class_node:
            return class_node
    return []
def merge_classes(x, y, classes):
    class_x = find_class(x, classes)
    if y in class_x:
        return classes
    else:
        class_y = find_class(y, classes)
        updated_classes = remove_class(class_x, classes)
        updated_classes = remove_class(class_y, updated_classes)
        return [class_x + class_y] + updated_classes
def remove_class(class_x, classes):
    if not classes:
        return []
    head = classes.pop(0)
    if set(head) == set(class_x):
        return classes
    else:
        return [head] + remove_class(class_x, classes)
def kruskal(graph):
    tree_edges = []
    edges = get_edges(graph)
    classes = create_classes(graph)
    edges = sort_edges(edges)
    for x, y, z in edges:
        if y in find_class(x, classes):
            tree_edges = tree_edges
        else:
            tree_edges.append((x, y, z))
            classes = merge_classes(x, y, classes)
    return tree_edges
def main():
    my_graph = create_graph()
    print("Graph: \n", my_graph)
    print("\nMinimum graph: \n", kruskal(my_graph))
if __name__ == "__main__":
    main()
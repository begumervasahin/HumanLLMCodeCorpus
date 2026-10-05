def read_graph_from_file(filename):
    graph = []
    with open(filename, 'r') as file:
        for line in file:
            name1, name2, weight = line.strip().split(',')
            weight = int(weight)
            element = (name1, [(name2, weight)])
            graph.append(element)
    return graph
def extract_edges(graph):
    edges = []
    for vertex, adj_list in graph:
        for neighbor, weight in adj_list:
            edge = (vertex, neighbor, weight)
            edges.append(edge)
    return edges
def order_edges_by_weight(edges):
    if not edges:
        return []
    pivot = edges[0]
    smaller = [edge for edge in edges[1:] if edge[2] <= pivot[2]]
    greater = [edge for edge in edges[1:] if edge[2] > pivot[2]]
    return order_edges_by_weight(smaller) + [pivot] + order_edges_by_weight(greater)
def create_initial_classes(graph):
    classes = []
    for vertex, _ in graph:
        classes.append([vertex])
    return classes
def find_class(vertex, classes):
    for class_ in classes:
        if vertex in class_:
            return class_
    return []
def merge_classes(vertex1, vertex2, classes):
    class_1 = find_class(vertex1, classes)
    class_2 = find_class(vertex2, classes)
    if vertex2 in class_1:
        return classes
    else:
        updated_classes = remove_class(class_2, classes)
        return [class_1 + class_2] + updated_classes
def remove_class(class_, classes):
    if not classes:
        return []
    head = classes[0]
    if set(head) == set(class_):
        return classes[1:]
    else:
        return [head] + remove_class(class_, classes[1:])
def kruskal_minimum_spanning_tree(graph):
    tree_edges = []
    edges = extract_edges(graph)
    classes = create_initial_classes(graph)
    sorted_edges = order_edges_by_weight(edges)
    for edge in sorted_edges:
        vertex1, vertex2, weight = edge
        if vertex2 in find_class(vertex1, classes):
            continue
        else:
            tree_edges.append(edge)
            classes = merge_classes(vertex1, vertex2, classes)
    return tree_edges
def main():
    filename = "input"
    graph = read_graph_from_file(filename)
    print("Graph:\n", graph)
    print("\nMinimum Spanning Tree:\n", kruskal_minimum_spanning_tree(graph))
if __name__ == "__main__":
    main()
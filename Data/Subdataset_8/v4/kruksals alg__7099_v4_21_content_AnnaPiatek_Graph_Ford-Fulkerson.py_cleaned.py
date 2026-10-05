import graphviz as gv
class Edge:
    def __init__(self, start_node, end_node, capacity):
        self.start_node = start_node
        self.end_node = end_node
        self.capacity = capacity
        self.flow = 0
class Graph:
    def __init__(self):
        self.edges = []
        self.max_flow = 0
    def add_edge(self, start, end, capacity):
        self.edges.append(Edge(start, end, capacity))
        return self
    def list_nodes(self):
        nodes = []
        for edge in self.edges:
            if edge.start_node not in nodes:
                nodes.append(edge.start_node)
            if edge.end_node not in nodes:
                nodes.append(edge.end_node)
        return nodes
    def get_neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if edge.start_node == node:
                neighbors.append(edge)
        return neighbors
    def print_edges(self):
        edge_list = []
        for edge in self.edges:
            edge_list.append([edge.start_node, edge.end_node, edge.flow, edge.capacity])
        return edge_list
    def create_predecessors(self):
        predecessors = {}
        for node in self.list_nodes():
            predecessors[str(node)] = 0
        return predecessors
    def find_path(self, start_node, end_node):
        predecessors = self.create_predecessors()
        visited_nodes = [str(start_node)]
        visited_edges = []
        friends = []
        roar = 1
        while roar != 20:
            for node in visited_nodes:
                if roar == 20:
                    break
                friends_i = self.get_neighbors(node)
                for edge in friends_i:
                    if edge.capacity != edge.flow:
                        predecessors[edge.end_node] = edge.start_node
                friends.extend(friends_i)
                for edge in friends_i:
                    if edge not in visited_edges and edge.end_node not in visited_nodes and edge.start_node != end_node and edge.capacity != edge.flow:
                        visited_edges.append(edge)
                        if edge.start_node not in visited_nodes:
                            visited_nodes.append(edge.start_node)
                            if edge.start_node == end_node:
                                roar = 20
                                break
                        if edge.end_node not in visited_nodes:
                            visited_nodes.append(edge.end_node)
                            if edge.end_node == end_node:
                                roar = 20
                                break
        node = end_node
        path = []
        node_ant = predecessors[node]
        end = 0
        while node_ant != 0:
            for edge in self.edges:
                if edge.end_node == node and edge.start_node == node_ant:
                    path.insert(0, edge)
                    node = edge.start_node
                    node_ant = predecessors[node]
        max_flow = 0
        minimum = path[0]
        for edge in path:
            if (edge.capacity - edge.flow) < (minimum.capacity - minimum.flow):
                minimum = edge
        min_flow = minimum.capacity - minimum.flow
        max_flow += min_flow
        final_path = []
        for edge in path:
            edge.flow += min_flow
            final_path.append([edge.start_node, edge.end_node, edge.flow, edge.capacity])
        visited_nodes = []
        visited_edges = []
        predecessors = self.create_predecessors()
        end = 0
        path = []
        return [final_path, max_flow]
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('Start', 'B', 5)\
         .add_edge('Start', 'C', 4)\
         .add_edge('C', 'B', 6)\
         .add_edge('B', 'E', 4)\
         .add_edge('C', 'E', 4)\
         .add_edge('E', 'Sink', 7)\
         .add_edge('C', 'Sink', 4)
    paths = []
    total_max_flow = 0
    max_flow = []
    for _ in range(3):
        path = graph.find_path('Start', 'Sink')
        paths.append(path)
        total_max_flow += path[1]
        max_flow.append(total_max_flow)
    drawing = gv.Digraph(format='png')
    for edge in graph.print_edges():
        drawing.edge(str(edge[0]), str(edge[1]), '0/%s' % str(edge[3]), color='black')
    drawing = apply_styles(drawing, styles)
    paths_list = [[]]
    a = 0
    for path in paths:
        for item in path[0]:
            paths_list[a].append([item[0], item[1]])
        paths_list.append([])
        a += 1
    edges_path = []
    for edge in graph.print_edges():
        edges_path.append([edge[0], edge[1]])
    def find_edge(edge, path_index):
        for item in paths[path_index][0]:
            if edge[0] == item[0] and edge[1] == item[1]:
                return item
    def find_in_list(edge):
        for item in graph.print_edges():
            if edge[0] == item[0] and edge[1] == item[1]:
                return item
    path_index = -1
    edge_index = -1
    lol = 1
    for found_path in paths_list[0:3]:
        path_index += 1
        edge_index = -1
        edge_list = []
        for found_edge in found_path:
            edge_list.append(found_edge)
        lol = 0
        for found_edge in found_path:
            edge_index += 1
            minimum = paths[path_index][1]
            drawing = gv.Digraph(format='png')
            drawing = apply_styles(drawing, styles)
            styles['graph']['label'] = str('minimum %s,max flow %s' % (minimum, max_flow[path_index]))
            for edge in edges_path:
                if edge in edge_list:
                    new_edge = find_edge(edge, path_index)
                    weight = str('%s/%s' % (str(new_edge[2]), str(new_edge[3])))
                    drawing.edge(new_edge[0], new_edge[1], weight, color='red')
                else:
                    if path_index == 0:
                        new_edge = find_in_list(edge)
                        weight = str('0/%s' % new_edge[3])
                        drawing.edge(edge[0], edge[1], weight, color='black')
                    if path_index == 1:
                        if find_edge(edge, path_index - 1) is not None:
                            new_edge = find_edge(edge, path_index - 1)
                            weight = str('%s/%s' % (new_edge[2], new_edge[3]))
                            drawing.edge(edge[0], edge[1], weight, color='black')
                        else:
                            new_edge = find_in_list(edge)
                            weight = str('%s/%s' % (new_edge[2], new_edge[3]))
                            drawing.edge(edge[0], edge[1], weight, color='black')
                    if path_index == 2:
                        if find_edge(edge, path_index - 1) is not None:
                            new_edge = find_edge(edge, path_index - 1)
                            weight = str('%s/%s' % (new_edge[2], new_edge[3]))
                            drawing.edge(edge[0], edge[1], weight, color='black')
                        elif find_edge(edge, path_index - 2) is not None:
                            new_edge = find_edge(edge, path_index - 2)
                            weight = str('%s/%s' % (new_edge[2], new_edge[3]))
                            drawing.edge(edge[0], edge[1], weight, color='black')
                        else:
                            new_edge = find_in_list(edge)
                            weight = str('%s/%s' % (new_edge[2], new_edge[3]))
                            drawing.edge(edge[0], edge[1], weight, color='black')
        drawing.render(view=True, filename=str(lol))
        lol += 1
    print(paths)
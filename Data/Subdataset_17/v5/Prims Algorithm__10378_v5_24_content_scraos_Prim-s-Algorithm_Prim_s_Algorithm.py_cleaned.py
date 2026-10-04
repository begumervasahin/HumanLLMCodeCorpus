from WGraphClass import *
from tkinter import *
root = Tk()
root.title("Graph Visualization with Prim's Algorithm")
canvas = Canvas(root, width=600, height=400)
canvas.pack()
vertex_buttons = []
graph = Dgraph()
vertex_coords = []
vertex_positions = {}
available_labels = [chr(i) for i in range(65, 115)]
selected_vertices = []
edge_distances = {}
edge_lines = {}
def create_vertex(event):
    x, y = event.x, event.y
    label = available_labels.pop(0)
    button = Button(root, text=label, bg='white', command=lambda: vertex_clicked(label))
    button.place(x=x, y=y)
    vertex_buttons.append(button)
    vertex_positions[label] = (x, y)
    graph.addnode(label)
def vertex_clicked(label):
    selected_vertices.append(label)
    if len(selected_vertices) == 2:
        add_edge(selected_vertices[0], selected_vertices[1], int(distance_entry.get()))
        selected_vertices.clear()
def add_edge(vertex1, vertex2, distance):
    graph.addarrow((vertex1, vertex2), distance)
    x1, y1 = vertex_positions[vertex1]
    x2, y2 = vertex_positions[vertex2]
    edge_lines[(vertex1, vertex2)] = (x1, y1, x2, y2)
    canvas.create_line(x1, y1, x2, y2)
    distance_label = Label(root, text=str(graph.dists[(vertex1, vertex2)]))
    distance_label.place(x=(x1 + x2) / 2, y=(y1 + y2) / 2 + 10)
    edge_distances[(vertex1, vertex2)] = distance_label
def prims(graph):
    start_vertex = graph.closest_neighb(graph.nodes[0])[0]
    tree = [(start_vertex, graph.nodes[0])] if (start_vertex, graph.nodes[0]) in graph.arrows else [(graph.nodes[0], start_vertex)]
    while len(tree) < len(graph.nodes) - 1:
        least_cost = float('inf')
        new_edge = None
        for edge in graph.get_edges(tree):
            if graph.dists[edge] < least_cost:
                least_cost = graph.dists[edge]
                new_edge = edge if edge in graph.arrows else (edge[1], edge[0])
        tree.append(new_edge)
    for edge in tree:
        x1, y1, x2, y2 = edge_lines[edge]
        canvas.create_line(x1, y1, x2, y2, fill='green')
def execute_prims():
    prims(graph)
canvas.bind("<Button-1>", create_vertex)
distance_entry = Entry(root)
distance_entry.pack(side=RIGHT)
distance_label = Label(root, text='Distance entry')
distance_label.pack(side=RIGHT)
prims_button = Button(root, text='Execute Prim\'s Algorithm', command=execute_prims)
prims_button.pack(side=LEFT)
root.mainloop()
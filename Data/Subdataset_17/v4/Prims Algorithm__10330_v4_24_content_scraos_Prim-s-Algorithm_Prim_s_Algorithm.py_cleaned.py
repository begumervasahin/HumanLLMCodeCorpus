from WGraphClass import *
from tkinter import *
root = Tk()
w = Canvas(root, width=600, height=400)
w.pack()
widgetlist = []
g1 = Dgraph()
coords = []
vertices_save = {}
alphab = [chr(i) for i in range(65, 115)]
connecter = []
distsT = {}
linescolor = {}
def createcoor(event):
    coords.append((event.x, event.y))
    if len(coords) == 1:
        btn = Button(root, text=alphab[0], bg='white', command=lambda j=alphab[0]: clickbutton(j))
        btn.place(x=coords[0][0], y=coords[0][1])
        widgetlist.append(btn)
        vertices_save[alphab[0]] = (coords[0][0], coords[0][1])
        g1.addnode(alphab[0])
        del alphab[0]
        coords.clear()
def clickbutton(a):
    connecter.append(a)
    if len(connecter) == 2:
        g1.addarrow((connecter[0], connecter[1]), int(entry3.get()))
        x1, y1 = vertices_save[connecter[0]]
        x2, y2 = vertices_save[connecter[1]]
        linescolor[(connecter[0], connecter[1])] = (x1, y1, x2, y2)
        w.create_line(x1, y1, x2, y2)
        distsT[(connecter[0], connecter[1])] = Label(root, text=str(g1.dists[(connecter[0], connecter[1])]))
        distsT[(connecter[0], connecter[1])].place(x=(x1 + x2) / 2, y=(y1 + y2) / 2 + 10)
        connecter.clear()
def prims(graph):
    start = graph.closest_neighb(graph.nodes[0])[0]
    tree = [(start, graph.nodes[0])] if (start, graph.nodes[0]) in graph.arrows else [(graph.nodes[0], start)]
    while len(tree) < len(graph.nodes) - 1:
        least = float('inf')
        new_edge = None
        for edge in graph.get_edges(tree):
            if graph.dists[edge] < least:
                least = graph.dists[edge]
                new_edge = edge if edge in graph.arrows else (edge[1], edge[0])
        tree.append(new_edge)
    for edge in tree:
        x1, y1, x2, y2 = linescolor[edge]
        w.create_line(x1, y1, x2, y2, fill='green')
def exec_prims():
    prims(g1)
w.bind("<Button-1>", createcoor)
entry3 = Entry(root)
entry3.pack(side=RIGHT)
label3 = Label(root, text='Distance entry')
label3.pack(side=RIGHT)
prims_Btn = Button(root, text='Execute Prim\'s Algorithm', command=exec_prims)
prims_Btn.pack(side=LEFT)
root.mainloop()
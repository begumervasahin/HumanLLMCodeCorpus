from WGraphClass import Dgraph
from tkinter import *
b1 = Tk()
b1.title("Graph Creator with Prim's Algorithm")
b2 = Canvas(b1, width=600, height=400)
b2.pack()
b3 = []
b4 = Dgraph()
b5 = []
b6 = {}
b7 = [chr(i) for i in range(65, 115)]
b8 = []
b9 = {}
b10 = {}
def fonk1(event):
    b5.append((event.b12, event.y))
    if len(b5) == 1:
        b11 = Button(b1, b15=b7[0], bg='white', command=lambda j=b7[0]: fonk2(j))
        b11.place(b12 = b5[0][0], y=b5[0][1])
        b3.append(b11)
        b6[b7[0]] = (b5[0][0], b5[0][1])
        b4.addnode(b7[0])
        del b7[0]
    if len(b5) == 1:
        del b5[0]
def fonk2(a):
    b8.append(a)
    if len(b8) == 2:
        b4.addarrow((b8[0], b8[1]), int(b21.get()))
        x1, b13 = b6[b8[0]]
        x2, b14 = b6[b8[1]]
        b10[(b8[0], b8[1])] = (x1, b13, x2, b14)
        b2.create_line(x1, b13, x2, b14)
        b9[(b8[0], b8[1])] = Label(b1, b15 = str(b4.dists[(b8[0], b8[1])]))
        b9[(b8[0], b8[1])].place(b12 = (x1 + x2) / 2, y=(b13 + b14) / 2 + 10)
        b8.clear()
def fonk3(graph):
    b16 = graph.closest_neighb(graph.nodes[0])[0]
    b17 = [(b16, graph.nodes[0])] if (b16, graph.nodes[0]) in graph.arrows else [(graph.nodes[0], b16)]
    while len(b17) < len(graph.nodes) - 1:
        b18 = float('inf')
        b19 = None
        for i in graph.get_edges(b17):
            if graph.dists[i] < b18:
                b18 = graph.dists[i]
                b19 = i if i in graph.arrows else (i[1], i[0])
        b17.append(b19)
    for k in b17:
        x1, b13, x2, b14 = b10[k]
        b2.create_line(x1, b13, x2, b14, b20 = 'green')
def fonk4():
    fonk3(b4)
b2.bind("<Button-1>", createcoor)
b21 = Entry(b1)
b21.pack(b22 = RIGHT)
b23 = Label(b1, b15='Distance entry')
b23.pack(b22 = RIGHT)
b24 = Button(b1, b15='Execute Prim\'s Algorithm', command=exec_prims)
b24.pack(b22 = LEFT)
b1.mainloop()
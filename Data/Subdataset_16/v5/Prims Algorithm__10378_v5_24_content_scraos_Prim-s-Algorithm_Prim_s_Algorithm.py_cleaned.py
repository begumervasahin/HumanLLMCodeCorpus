from WGraphClass import *
from tkinter import *
b1 = Tk()
b1.title("Graph Visualization with Prim's Algorithm")
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
    b14, b11 = event.b14, event.b11
    b12 = b7.pop(0)
    b13 = Button(b1, text=b12, bg='white', command=lambda: fonk2(b12))
    b13.place(b14 = b14, b11=b11)
    b3.append(b13)
    b6[b12] = (b14, b11)
    b4.addnode(b12)
def fonk2(b12):
    b8.append(b12)
    if len(b8) == 2:
        fonk3(b8[0], b8[1], int(b23.get()))
        b8.clear()
def fonk3(vertex1, vertex2, distance):
    b4.addarrow((vertex1, vertex2), distance)
    x1, b15 = b6[vertex1]
    x2, b16 = b6[vertex2]
    b10[(vertex1, vertex2)] = (x1, b15, x2, b16)
    b2.create_line(x1, b15, x2, b16)
    b17 = Label(b1, text=str(b4.dists[(vertex1, vertex2)]))
    b17.place(b14 = (x1 + x2) / 2, b11=(b15 + b16) / 2 + 10)
    b9[(vertex1, vertex2)] = b17
def fonk4(b4):
    b18 = b4.closest_neighb(b4.nodes[0])[0]
    b19 = [(b18, b4.nodes[0])] if (b18, b4.nodes[0]) in b4.arrows else [(b4.nodes[0], b18)]
    while len(b19) < len(b4.nodes) - 1:
        b20 = float('inf')
        b21 = None
        for edge in b4.get_edges(b19):
            if b4.dists[edge] < b20:
                b20 = b4.dists[edge]
                b21 = edge if edge in b4.arrows else (edge[1], edge[0])
        b19.append(b21)
    for edge in b19:
        x1, b15, x2, b16 = b10[edge]
        b2.create_line(x1, b15, x2, b16, b22 = 'green')
def fonk5():
    fonk4(b4)
b2.bind("<Button-1>", create_vertex)
b23 = Entry(b1)
b23.pack(b24 = RIGHT)
b17 = Label(b1, text='Distance entry')
b17.pack(b24 = RIGHT)
b25 = Button(b1, text='Execute Prim\'s Algorithm', command=execute_prims)
b25.pack(b24 = LEFT)
b1.mainloop()
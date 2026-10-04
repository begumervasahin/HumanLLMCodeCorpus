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
        b11 = Button(b1, b17=b7[0], bg='white', command=lambda j=b7[0]: fonk2(j))
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
        b4.addarrow((b8[0], b8[1]), int(b22.get()))
        b13 = b6[b8[0]][0]
        b14 = b6[b8[0]][1]
        b15 = b6[b8[1]][0]
        b16 = b6[b8[1]][1]
        b10[(b8[0], b8[1])] = (b13, b14, b15, b16)
        b2.create_line(b13, b14, b15, b16)
        b9[(b8[0], b8[1])] = Label(b1, b17 = '{}'.format(b4.dists[(b8[0], b8[1])]))
        b9[(b8[0], b8[1])].place(b12 = (b13 + b15) / 2, y=(b14 + b16) / 2 + 10)
        del b8[0]
        del b8[0]
def fonk3(graph):
    b18 = graph.closest_neighb(graph.nodes[0])[0]
    b19 = []
    if (b18, graph.nodes[0]) in graph.arrows:
        b19 = [(b18, graph.nodes[0])]
    else:
        b19 = [(graph.nodes[0], b18)]
    while len(b19) < len(graph.nodes) - 1:
        a1 = 10e3
        b20 = None
        for i in graph.get_edges(b19):
            if graph.dists[i] < a1:
                a1 = graph.dists[i]
                if i in graph.arrows:
                    b20 = i
                else:
                    b20 = (i[1], i[0])
        b19.append(b20)
    print(b19)
    for k in b19:
        b2.create_line(b10[k][0], b10[k][1], b10[k][2], b10[k][3], b21 = 'green')
def fonk4():
    fonk3(b4)
b2.bind("<Button-1>", createcoor)
b22 = Entry(b1)
b22.pack(b23 = RIGHT)
b24 = Label(b1, b17='Distance entry')
b24.pack(b23 = RIGHT)
b25 = Button(b1, b17='Execute Prim\'s Algorithm', command=exec_prims)
b25.pack(b23 = LEFT)
b1.mainloop()
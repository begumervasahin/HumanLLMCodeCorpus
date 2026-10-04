from WGraphClass import *
from tkinter import *
b1 = Tk()
b2 = Canvas(b1, width=600, height=400)
b2.pack()
b3 = []
b4 = Dgraph()
b5 = []
b6 = {}
b7 = [i for i in range(50)]
def fonk1(event):
    b5.append((event.b9, event.y))
    if len(b5) == 1:
        b8 = Button(b1, b20=b7[0], bg='white', command=lambda j=b7[0]: fonk2(j))
        b8.place(b9 = b5[0][0], y=b5[0][1])
        b3.append(b8)
        b6[b7[0]] = (b5[0][0], b5[0][1])
        b4.addnode(b7[0])
        del b7[0]
    if len(b5) == 1:
        del b5[0]
b2.bind("<Button-1>", createcoor)
b10 = Entry(b1)
b10.pack(b11 = RIGHT)
b12 = Label(b1, b20='Distance entry')
b12.pack(b11 = RIGHT)
b13 = []
b14 = {}
b15 = {}
def fonk2(a):
    b13.append(a)
    if len(b13) == 2:
        b4.addarrow((b13[0], b13[1]), int(b10.get()))
        b16 = b6[b13[0]][0]
        b17 = b6[b13[0]][1]
        b18 = b6[b13[1]][0]
        b19 = b6[b13[1]][1]
        b15[(b13[0], b13[1])] = (b16, b17, b18, b19)
        b2.create_line(b16, b17, b18, b19)
        b14[(b13[0], b13[1])] = Label(b1, b20 = '{}'.format(b4.dists[(b13[0], b13[1])]))
        b14[(b13[0], b13[1])].place(b9 = (b16 + b18)/2,y=(b17 + b19)/2+10)
        del b13[0]
        del b13[0]
def fonk3(graph):
    b21 = graph.closest_neighb(graph.nodes[0])[0]
    b22 = []
    if (b21,graph.nodes[0]) in graph.arrows:
        b22 = [(b21,graph.nodes[0])]
    else:
        b22 = [(graph.nodes[0],b21)]
    while len(b22) < len(graph.nodes)-1:
        a1 = 10e3
        b23 = None
        for i in graph.get_edges(b22):
            if graph.dists[i] < a1:
                a1 = graph.dists[i]
                if i in graph.arrows:
                    b23 = i
                else:
                    b23 = (i[1],i[0])
        b22.append(b23)
    print(b22)
    for k in b22:
        b2.create_line(b15[k][0],b15[k][1],b15[k][2],b15[k][3],b24 = 'green')
def fonk4():
    fonk3(b4)
b25 = Button(b1, b20='Execute Prims Algorithm', command=exec_prims)
b25.pack(b11 = LEFT)
b1.mainloop()
from WGraphClass import Dgraph
from tkinter import *
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b1.title("Graph Creator with Prim's Algorithm")
        self.b2 = Canvas(b1, width=600, height=400)
        self.b2.pack()
        self.b3 = []
        self.b4 = Dgraph()
        self.b5 = []
        self.b6 = {}
        self.b7 = [chr(i) for i in range(65, 115)]
        self.b8 = []
        self.b9 = {}
        self.b10 = {}
        self.b11 = Entry(b1)
        self.b11.pack(b12 = RIGHT)
        self.b13 = Label(b1, b20='Distance entry')
        self.b13.pack(b12 = RIGHT)
        self.b14 = Button(b1, b20='Execute Prim\'s Algorithm', command=self.exec_prims)
        self.b14.pack(b12 = LEFT)
        self.b2.bind("<Button-1>", self.create_vertex)
    def fonk2(self, event):
        self.b5.append((event.b17, event.y))
        if len(self.b5) == 1:
            b15 = self.b7.pop(0)
            b16 = Button(self.b1, b20=b15, bg='white', command=lambda v=b15: self.fonk3(v))
            b16.place(b17 = self.b5[0][0], y=self.b5[0][1])
            self.b3.append(b16)
            self.b6[b15] = (self.b5[0][0], self.b5[0][1])
            self.b4.addnode(b15)
            self.b5.clear()
    def fonk3(self, vertex):
        self.b8.append(vertex)
        if len(self.b8) == 2:
            self.b4.addarrow((self.b8[0], self.b8[1]), int(self.b11.get()))
            x1, b18 = self.b6[self.b8[0]]
            x2, b19 = self.b6[self.b8[1]]
            self.b10[(self.b8[0], self.b8[1])] = (x1, b18, x2, b19)
            self.b2.create_line(x1, b18, x2, b19)
            self.b9[(self.b8[0], self.b8[1])] = Label(self.b1, b20 = str(self.b4.dists[(self.b8[0], self.b8[1])]))
            self.b9[(self.b8[0], self.b8[1])].place(b17 = (x1 + x2) / 2, y=(b18 + b19) / 2 + 10)
            self.b8.clear()
    def fonk4(self):
        self.fonk5(self.b4)
    def fonk5(self, b4):
        b21 = b4.closest_neighb(b4.nodes[0])[0]
        b22 = [(b21, b4.nodes[0])] if (b21, b4.nodes[0]) in b4.arrows else [(b4.nodes[0], b21)]
        while len(b22) < len(b4.nodes) - 1:
            b23 = float('inf')
            b24 = None
            for edge in b4.get_edges(b22):
                if b4.dists[edge] < b23:
                    b23 = b4.dists[edge]
                    b24 = edge if edge in b4.arrows else (edge[1], edge[0])
            b22.append(b24)
        for edge in b22:
            x1, b18, x2, b19 = self.b10[edge]
            self.b2.create_line(x1, b18, x2, b19, b25 = 'green')
if b26 = = "__main__":
    b1 = Tk()
    b27 = class1(b1)
    b1.mainloop()
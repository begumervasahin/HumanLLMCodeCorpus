import graphviz as gv
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.a1 = 0
class class2:
    def fonk2(self):
        self.b4 = []
        self.a2 = 0
    def fonk3(self, start, a4, b3):
        self.b4.append(class1(start, a4, b3))
        return self
    def fonk4(self):
        b5 = []
        for edge in self.b4:
            if edge.b1 not in b5:
                b5.append(edge.b1)
            if edge.b2 not in b5:
                b5.append(edge.b2)
        return b5
    def fonk5(self, b13):
        b6 = []
        for edge in self.b4:
            if edge.b1 = = b13:
                b6.append(edge)
        return b6
    def fonk6(self):
        b7 = []
        for edge in self.b4:
            b7.append([edge.b1, edge.b2, edge.a1, edge.b3])
        return b7
    def fonk7(self):
        b8 = {}
        for b13 in self.fonk4():
            b8[str(b13)] = 0
        return b8
    def fonk8(self, b1, b2):
        b8 = self.fonk7()
        b9 = [str(b1)]
        b10 = []
        b11 = []
        a3 = 1
        while a3 != 20:
            for b13 in b9:
                if a3 = = 20:
                    break
                b12 = self.fonk5(b13)
                for edge in b12:
                    if edge.b3 != edge.a1:
                        b8[edge.b2] = edge.b1
                b11.extend(b12)
                for edge in b12:
                    if edge not in b10 and edge.b2 not in b9 and edge.b1 != b2 and edge.b3 != edge.a1:
                        b10.append(edge)
                        if edge.b1 not in b9:
                            b9.append(edge.b1)
                            if edge.b1 = = b2:
                                a3 = 20
                                break
                        if edge.b2 not in b9:
                            b9.append(edge.b2)
                            if edge.b2 = = b2:
                                a3 = 20
                                break
        b13 = b2
        b14 = []
        b15 = b8[b13]
        a4 = 0
        while b15 != 0:
            for edge in self.b4:
                if edge.b2 = = b13 and edge.b1 == b15:
                    b14.insert(0, edge)
                    b13 = edge.b1
                    b15 = b8[b13]
        a2 = 0
        b16 = b14[0]
        for edge in b14:
            if (edge.b3 - edge.a1) < (b16.b3 - b16.a1):
                b16 = edge
        b17 = b16.b3 - b16.a1
        a2 += b17
        b18 = []
        for edge in b14:
            edge.a1 += b17
            b18.append([edge.b1, edge.b2, edge.a1, edge.b3])
        b9 = []
        b10 = []
        b8 = self.fonk7()
        a4 = 0
        b14 = []
        return [b18, a2]
if b19 = = "__main__":
    b20 = class2()
    b20.fonk3('Start', 'B', 5)\
         .fonk3('Start', 'C', 4)\
         .fonk3('C', 'B', 6)\
         .fonk3('B', 'E', 4)\
         .fonk3('C', 'E', 4)\
         .fonk3('E', 'Sink', 7)\
         .fonk3('C', 'Sink', 4)
    b21 = []
    a5 = 0
    a2 = []
    for _ in range(3):
        b14 = b20.fonk8('Start', 'Sink')
        b21.append(b14)
        a5 += b14[1]
        a2.append(a5)
    b22 = gv.Digraph(format='png')
    for edge in b20.fonk6():
        b22.edge(str(edge[0]), str(edge[1]), '0/%s' % str(edge[3]), b23 = 'black')
    b22 = apply_styles(b22, styles)
    b24 = [[]]
    a6 = 0
    for b14 in b21:
        for item in b14[0]:
            b24[a6].append([item[0], item[1]])
        b24.append([])
        a6 += 1
    b25 = []
    for edge in b20.fonk6():
        b25.append([edge[0], edge[1]])
    def fonk9(edge, a7):
        for item in b21[a7][0]:
            if edge[0] == item[0] and edge[1] == item[1]:
                return item
    def fonk10(edge):
        for item in b20.fonk6():
            if edge[0] == item[0] and edge[1] == item[1]:
                return item
    a7 = -1
    a8 = -1
    a9 = 1
    for found_path in b24[0:3]:
        a7 += 1
        a8 = -1
        b7 = []
        for found_edge in found_path:
            b7.append(found_edge)
        a9 = 0
        for found_edge in found_path:
            a8 += 1
            b16 = b21[a7][1]
            b22 = gv.Digraph(format='png')
            b22 = apply_styles(b22, styles)
            styles['b20']['label'] = str('b16 %s,max a1 %s' % (b16, a2[a7]))
            for edge in b25:
                if edge in b7:
                    b26 = fonk9(edge, a7)
                    b27 = str('%s/%s' % (str(b26[2]), str(b26[3])))
                    b22.edge(b26[0], b26[1], b27, b23 = 'red')
                else:
                    if a7 = = 0:
                        b26 = fonk10(edge)
                        b27 = str('0/%s' % b26[3])
                        b22.edge(edge[0], edge[1], b27, b23 = 'black')
                    if a7 = = 1:
                        if fonk9(edge, a7 - 1) is not None:
                            b26 = fonk9(edge, a7 - 1)
                            b27 = str('%s/%s' % (b26[2], b26[3]))
                            b22.edge(edge[0], edge[1], b27, b23 = 'black')
                        else:
                            b26 = fonk10(edge)
                            b27 = str('%s/%s' % (b26[2], b26[3]))
                            b22.edge(edge[0], edge[1], b27, b23 = 'black')
                    if a7 = = 2:
                        if fonk9(edge, a7 - 1) is not None:
                            b26 = fonk9(edge, a7 - 1)
                            b27 = str('%s/%s' % (b26[2], b26[3]))
                            b22.edge(edge[0], edge[1], b27, b23 = 'black')
                        elif fonk9(edge, a7 - 2) is not None:
                            b26 = fonk9(edge, a7 - 2)
                            b27 = str('%s/%s' % (b26[2], b26[3]))
                            b22.edge(edge[0], edge[1], b27, b23 = 'black')
                        else:
                            b26 = fonk10(edge)
                            b27 = str('%s/%s' % (b26[2], b26[3]))
                            b22.edge(edge[0], edge[1], b27, b23 = 'black')
        b22.render(b28 = True, filename=str(a9))
        a9 += 1
    print(b21)
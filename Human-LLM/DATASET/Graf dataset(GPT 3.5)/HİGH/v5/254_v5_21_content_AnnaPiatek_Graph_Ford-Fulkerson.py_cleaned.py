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
    def fonk3(self, start, end, b3):
        self.b4.append(class1(start, end, b3))
        return self
    def fonk4(self):
        b5 = set()
        for edge in self.b4:
            b5.add(edge.b1)
            b5.add(edge.b2)
        return list(b5)
    def fonk5(self, b12):
        b6 = []
        for edge in self.b4:
            if edge.b1 = = b12:
                b6.append(edge)
        return b6
    def fonk6(self):
        b7 = []
        for edge in self.b4:
            b7.append([edge.b1, edge.b2, edge.a1, edge.b3])
        return b7
    def fonk7(self, b1, b2):
        b8 = {b12: 0 for b12 in self.fonk4()}
        b9 = [b1]
        while b9:
            b10 = b9.pop(0)
            for edge in self.fonk5(b10):
                if edge.b3 != edge.a1:
                    b8[edge.b2] = edge.b1
                    if edge.b2 = = b2:
                        b11 = []
                        b12 = b2
                        while b12 != b1:
                            for e in self.b4:
                                if e.b2 = = b12 and e.b1 == b8[b12]:
                                    b11.insert(0, e)
                                    b12 = e.b1
                                    break
                        b13 = min(edge.b3 - edge.a1 for edge in b11)
                        for e in b11:
                            e.a1 += b13
                        return [b11, b13]
                    b9.append(edge.b2)
        return None
def fonk8():
    b14 = class2()
    b14.fonk3('Start', 'B', 5)\
         .fonk3('Start', 'C', 4)\
         .fonk3('C', 'B', 6)\
         .fonk3('B', 'E', 4)\
         .fonk3('C', 'E', 4)\
         .fonk3('E', 'Sink', 7)\
         .fonk3('C', 'Sink', 4)
    b15 = []
    a2 = 0
    for _ in range(3):
        b11 = b14.fonk7('Start', 'Sink')
        if b11:
            b15.append(b11)
            a2 += b11[1]
    b16 = gv.Digraph(format='png')
    for edge in b14.fonk6():
        b16.edge(str(edge[0]), str(edge[1]), '0/%s' % str(edge[3]), b17 = 'black')
    b16.render(b18 = True)
if b19 = = "__main__":
    fonk8()
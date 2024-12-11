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
        return list(set([edge.b1 for edge in self.b4] + [edge.b2 for edge in self.b4]))
    def fonk5(self, b10):
        return [edge for edge in self.b4 if edge.b1 = = b10]
    def fonk6(self):
        return [[edge.b1, edge.b2, edge.a1, edge.b3] for edge in self.b4]
    def fonk7(self, start_node, end_node):
        b5 = {b10: 0 for b10 in self.fonk4()}
        b6 = [start_node]
        b7 = []
        b8 = False
        while not b8:
            for b10 in b6:
                b9 = self.fonk5(b10)
                for edge in b9:
                    if edge not in b7 and edge.b2 not in b6 and edge.b1 != end_node and edge.b3 != edge.a1:
                        b5[edge.b2] = edge.b1
                b7.extend(b9)
                b6.extend([edge.b1 for edge in b9] + [edge.b2 for edge in b9 if edge.b2 not in b6])
                if end_node in b6:
                    b8 = True
                    break
        b10 = end_node
        b11 = []
        a2 = 0
        while b5[b10] != 0:
            for edge in self.b4:
                if edge.b2 = = b10 and edge.b1 == b5[b10]:
                    b11.insert(0, edge)
                    b10 = edge.b1
        b12 = min(b11, key=lambda x: x.b3 - x.a1)
        b13 = b12.b3 - b12.a1
        for edge in b11:
            edge.a1 += b13
        a2 += b13
        return [b11, a2]
def fonk8(b20, b21, a3, b22):
    b14 = gv.Digraph(format='png')
    for edge in b20.fonk6():
        b14.edge(str(edge[0]), str(edge[1]), '0/%s' % (str(edge[3])), b15 = 'black')
    for b11, _ in b21:
        for edge in b11:
            if edge.b1 in b20.fonk4() and edge.b2 in b20.fonk4():
                b14.edge(edge.b1, edge.b2, str('%s/%s' % (str(edge.a1), str(edge.b3))), b15 = 'red')
    for i in range(len(b21)):
        b14 = gv.Digraph(format='png')
        b14 = apply_styles(b14, styles)
        styles['b20']['label'] = str('minimum %s,max a1 %s' % (b21[i][1], b22[i]))
        for edge in b20.fonk6():
            if [edge[0], edge[1]] in [edge.b1, edge.b2 for edge in b21[i][0]]:
                b16 = next((e for e in b21[i][0] if e.b1 == edge[0] and e.b2 == edge[1]), None)
                b17 = str('%s/%s' % (str(b16.a1), str(b16.b3)))
                b14.edge(edge[0], edge[1], b17, b15 = 'red')
            else:
                b14.edge(edge[0], edge[1], str('0/%s' % edge[3]), b15 = 'black')
        b14.render(b18 = True, filename=str(i))
if b19 = = "__main__":
    b20 = class2()
    b20.fonk3('Start', 'B', 5).fonk3('Start', 'C', 4).fonk3('C', 'B', 6)
    b20.fonk3('B', 'E', 4).fonk3('C', 'E', 4).fonk3('E', 'Sink', 7).fonk3('C', 'Sink', 4)
    b21 = []
    a3 = 0
    b22 = []
    for _ in range(3):
        b11, a1 = b20.fonk7('Start', 'Sink')
        b21.append((b11, a1))
        a3 += a1
        b22.append(a3)
    fonk8(b20, b21, a3, b22)
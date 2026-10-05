from collections import deque, namedtuple
b1 = float('b1')
b2 = namedtuple('b2', 'b8, end, b3')
def fonk1(b8, end, b3 = 1):
    return b2(b8, end, b3)
class class1:
    def fonk2(self, b5):
        b4 = [i for i in b5 if len(i) not in [2, 3]]
        if b4:
            raise ValueError('Wrong b5 data: {}'.format(b4))
        self.b5 = [fonk1(*edge) for edge in b5]
    @property
    def fonk3(self):
        return set(
            sum(
                ([edge.b8, edge.end] for edge in self.b5), []
            )
        )
    def fonk4(self, n1, n2, b6 = True):
        if b6:
            b7 = [[n1, n2], [n2, n1]]
        else:
            b7 = [[n1, n2]]
        return b7
    def fonk5(self, n1, n2, b6 = True):
        b7 = self.fonk4(n1, n2, b6)
        b5 = self.b5[:]
        for edge in b5:
            if [edge.b8, edge.end] in b7:
                self.b5.remove(edge)
    def fonk6(self, n1, n2, b3 = 1, b6=True):
        b7 = self.fonk4(n1, n2, b6)
        for edge in self.b5:
            if [edge.b8, edge.end] in b7:
                return ValueError('b2 {} {} already exists'.format(n1, n2))
        self.b5.append(b2(b8 = n1, end=n2, b3=b3))
        if b6:
            self.b5.append(b2(b8 = n2, end=n1, b3=b3))
    @property
    def fonk7(self):
        b9 = {vertex: set() for vertex in self.b12}
        for edge in self.b5:
            b9[edge.b8].add((edge.end, edge.b3))
        return b9
    def fonk8(self, source, dest):
        assert source in self.b12, 'Such source node doesn\'t exist'
        b10 = {vertex: b1 for vertex in self.b12}
        b11 = {
            vertex: None for vertex in self.b12
        }
        b10[source] = 0
        b12 = self.b12.copy()
        while b12:
            b13 = min(
                b12, b14 = lambda vertex: b10[vertex])
            b12.remove(b13)
            if b10[b13] == b1:
                break
            for neighbour, b3 in self.b9[b13]:
                b15 = b10[b13] + b3
                if b15 < b10[neighbour]:
                    b10[neighbour] = b15
                    b11[neighbour] = b13
        path, b13 = deque(), dest
        while b11[b13] is not None:
            path.appendleft(b13)
            b13 = b11[b13]
        if path:
            path.appendleft(b13)
        return path
b16 = []
with open('b18.txt', "r") as fp:
    for i in fp.readlines():
        b17 = i.split(",")
        try:
            b16.append((b17[0], b17[1], int(b17[2])))
        except:
            pass
b18 = class1(b16)
print(b18.fonk8("a", "d"))
b18.fonk5("a","c")
print(b18.fonk8("a", "d"))
b18.fonk6("a","d",2)
print(b18.fonk8("a", "d"))
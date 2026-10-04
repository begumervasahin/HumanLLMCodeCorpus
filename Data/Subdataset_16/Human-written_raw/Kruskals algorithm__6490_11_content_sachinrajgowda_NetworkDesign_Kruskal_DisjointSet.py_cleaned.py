
class class1(dict):
    def fonk1(self, item):
        self[item] = item
    def fonk2(self, item):
        b1 = self[item]
        while self[b1] != b1:
            b1 = self[b1]
        self[item] = b1
        return b1
    def fonk3(self, item1, item2):
        self[item2] = self[item1]
def fonk4( nodes, sorted_edge ):
    b2 = class1()
    b3 = []
    for n in nodes:
        b2.fonk1( n )
    b4 = len(nodes) - 1
    for edge in sorted_edge:
        src, dest, b5 = edge
        b6 = b2.fonk2(src)
        b7 = b2.fonk2(dest)
        if b6 != b7:
            b3.append(edge)
            b4 -= 1
            if b4 = = 0:
                return b3
            b2.fonk3(b6, b7)
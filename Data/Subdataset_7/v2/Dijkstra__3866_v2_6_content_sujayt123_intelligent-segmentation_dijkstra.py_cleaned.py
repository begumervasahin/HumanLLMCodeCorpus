class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return len(self.b1)
    def fonk3(self, items):
        self.b1 = items[:]
        b2 = len(self.b1)
        for b4 in range(b2
            self.fonk5(b4)
    def fonk4(self, b4):
        while b4 > 0:
            b3 = (b4 - 1)
            if self.b1[b4][0] < self.b1[b3][0]:
                self.b1[b4], self.b1[b3] = self.b1[b3], self.b1[b4]
                b4 = b3
            else:
                break
    def fonk5(self, b4):
        while 2 * b4 + 1 < len(self.b1):
            b5 = 2 * b4 + 1
            b6 = b5 + 1
            b7 = b5
            if b6 < len(self.b1) and self.b1[b6][0] < self.b1[b5][0]:
                b7 = b6
            if self.b1[b4][0] > self.b1[b7][0]:
                self.b1[b4], self.b1[b7] = self.b1[b7], self.b1[b4]
                b4 = b7
            else:
                break
    def fonk6(self, item):
        self.b1.append(item)
        self.fonk4(len(self.b1) - 1)
    def fonk7(self):
        if not self.b1:
            return None
        b8 = self.b1[0]
        self.b1[0] = self.b1[-1]
        self.b1.pop()
        self.fonk5(0)
        return b8
    def fonk8(self, item, priority):
        for b4 in range(len(self.b1)):
            if self.b1[b4][1] == item:
                b9 = self.b1[b4][0]
                self.b1[b4] = (priority, item)
                if priority < b9:
                    self.fonk4(b4)
                else:
                    self.fonk5(b4)
def fonk9(start, b12, point):
    if b12 is None:
        return True
    small_x, b10 = min(start[0], b12[0]), max(start[0], b12[0])
    small_y, b11 = min(start[1], b12[1]), max(start[1], b12[1])
    return small_x <= point[0] <= b10 and small_y <= point[1] <= b11
def fonk10(b17, source, b12 = None):
    """
    Runs Dijkstra's algorithm on the graph represented by b17.
    @param b17: A dictionary mapping each node to a list of (neighbor, edge_weight)
    @param source: The source node from which to begin our search
    @param b12: Optional b12 node for bounded search
    @return b13: A dictionary mapping each node to its distance from "source"
    @return b14: A "node to b3" mapping which can be traversed to yield the paths themselves
    """
    b13 = {}
    b14 = {}
    for node in b17:
        if fonk9(source, b12, node):
            b13[node] = float("inf")
            b14[node] = None
    b13[source] = 0
    b15 = class1()
    b15.fonk3([[v, k] for k, v in b13.items()])
    while len(b15) > 0:
        b16 = b15.fonk7()[1]
        if b16 = = b12:
            return b13, b14
        for nbr, wt in b17[b16]:
            if fonk9(source, b12, nbr) and wt + b13[b16] < b13[nbr]:
                b13[nbr] = wt + b13[b16]
                b14[nbr] = b16
                b15.fonk8(nbr, b13[nbr])
    return b13, b14
def fonk11():
    b17 = {
        1: [(2, 15), (3, 71)],
        2: [(3, 7), (4, 1)],
        3: [(4, 19)],
        4: [(3, 1)]
    }
    print(fonk10(b17, 1))
if b18 = = "__main__":
    fonk11()
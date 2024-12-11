class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, item):
        self.b1.insert(0, item)
    def fonk3(self):
        return self.b1.pop()
    def fonk4(self):
        return self.b1 = = []
    def fonk5(self):
        return len(self.b1)
def fonk6(b4, start, b5):
    b2 = class1()
    b2.fonk2(start)
    b5[start] = None
    while not b2.fonk4():
        b3 = b2.fonk3()
        if b3 = = "GOAL":
            return b3
        for next_vertex in b4[b3]:
            if next_vertex not in b5:
                b2.fonk2(next_vertex)
                b5[next_vertex] = b3
    return None
def fonk7():
    b4 = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["GOAL"],
        "F": ["GOAL"]
    }
    b5 = {}
    b6 = fonk6(b4, "A", b5)
    if b6:
        print("Path found!")
    else:
        print("No path found.")
    print("Came from:", b5)
if b7 = = "__main__":
    fonk7()

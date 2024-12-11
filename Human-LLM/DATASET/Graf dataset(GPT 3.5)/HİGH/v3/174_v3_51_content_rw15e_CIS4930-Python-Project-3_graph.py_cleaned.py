class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
    def fonk2(self, name):
        if name in self.b1:
            print(f"A vertex with name '{name}' already exists.")
        else:
            self.b1.append(name)
    def fonk3(self, start, end):
        if end not in self.b1:
            self.b1.append(end)
        if start not in self.b1:
            self.b1.append(start)
        if start in self.b1 and end in self.b1:
            self.b2.append((start, end))
    def fonk4(self, name):
        if name in self.b1:
            self.b1.remove(name)
            self.b2 = [b3 for b3 in self.b2 if name not in b3]
        else:
            print(f"Vertex '{name}' not found.")
    def fonk5(self, start, end):
        if (start, end) in self.b2:
            self.b2.remove((start, end))
        else:
            print(f"Edge '{start}' -> '{end}' not found.")
    def fonk6(self):
        return self.b1
    def fonk7(self):
        for b3 in self.b2:
            print(f"{b3[0]} -> {b3[1]}")
    def fonk8(self, start, end):
        return any(b3 = = (start, end) for b3 in self.b2)
    def fonk9(self, start, end):
        b4 = []
        for b3 in self.b2:
            if b3[0] == start:
                b4.append(b3[1])
            elif b3[1] == start:
                b4.append(b3[0])
        for vertex in b4:
            print(f"{start} -> {vertex} -> {end}")
class class2(class1):
    def fonk10(self, start, end):
        super().fonk10(start, end)
        self.b2.append((end, start))
    def fonk11(self, start, end):
        super().fonk11(start, end)
        self.b2.remove((end, start))
    def fonk12(self):
        for b3 in self.b2:
            print(f"{b3[0]} <-> {b3[1]}")
    def fonk13(self, start, end):
        b4 = []
        for b3 in self.b2:
            if b3[0] == start:
                b4.append(b3[1])
            elif b3[1] == start:
                b4.append(b3[0])
        for vertex in b4:
            print(f"{start} <-> {vertex} <-> {end}")
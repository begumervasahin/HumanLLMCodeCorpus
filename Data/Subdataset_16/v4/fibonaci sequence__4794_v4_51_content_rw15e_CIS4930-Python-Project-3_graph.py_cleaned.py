
from __future__ import print_function
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
    def fonk2(self, name):
        if name in self.b1:
            print(f"A vertex with name {name} already exists.")
        else:
            self.b1.append(name)
    def fonk3(self, b4, end):
        if b4 not in self.b1:
            self.b1.append(b4)
        if end not in self.b1:
            self.b1.append(end)
        if b4 in self.b1 and end in self.b1:
            self.b2.append((b4, end))
    def fonk4(self, name):
        if name in self.b1:
            self.b1.remove(name)
            self.b2 = [edge for edge in self.b2 if edge[0] != name and edge[1] != name]
        else:
            print(f"No vertex named {name} found.")
    def fonk5(self, b4, end):
        if (b4, end) in self.b2:
            self.b2.remove((b4, end))
        else:
            print(f"No edge from {b4} to {end} found.")
    def fonk6(self):
        return self.b1
    def fonk7(self):
        for b4, end in self.b2:
            print(f"{b4} -> {end}")
    def fonk8(self, b4, end):
        return (b4, end) in self.b2
    def fonk9(self, b4, end, b3 = None):
        if b3 is None:
            b3 = []
        b3 = b3 + [b4]
        if b4 = = end:
            print(" -> ".join(b3))
        if b4 not in self.b1:
            return
        for node in self.b1:
            if (b4, node) in self.b2 and node not in b3:
                self.fonk13(node, end, b3)
class class2(class1):
    def fonk10(self):
        super().fonk10()
    def fonk11(self, b4, end):
        super().fonk11(b4, end)
        if (end, b4) not in self.b2:
            self.b2.append((end, b4))
    def fonk12(self):
        for b4, end in self.b2:
            print(f"{b4} <-> {end}")
    def fonk13(self, b4, end, b3 = None):
        if b3 is None:
            b3 = []
        b3 = b3 + [b4]
        if b4 = = end:
            print(" <-> ".join(b3))
        if b4 not in self.b1:
            return
        for node in self.b1:
            if (b4, node) in self.b2 and node not in b3:
                self.fonk13(node, end, b3)
if b5 = = "__main__":
    b6 = class1()
    b6.fonk2("A")
    b6.fonk2("B")
    b6.fonk11("A", "B")
    b6.fonk11("A", "C")
    b6.fonk11("B", "C")
    print("Vertices:", b6.fonk6())
    b6.fonk12()
    print("Is connected A -> B:", b6.fonk8("A", "B"))
    print("Paths from A to C:")
    b6.fonk13("A", "C")
    b7 = class2()
    b7.fonk2("X")
    b7.fonk2("Y")
    b7.fonk11("X", "Y")
    b7.fonk11("X", "Z")
    b7.fonk11("Y", "Z")
    print("Vertices:", b7.fonk6())
    b7.fonk12()
    print("Is connected X <-> Y:", b7.fonk8("X", "Y"))
    print("Paths from X to Z:")
    b7.fonk13("X", "Z")
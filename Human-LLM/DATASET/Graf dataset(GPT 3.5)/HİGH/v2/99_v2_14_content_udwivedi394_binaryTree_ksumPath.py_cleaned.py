class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b5, k):
    def fonk3(b5, path, k):
        if b5 is None:
            return
        path.append(b5.b1)
        fonk3(b5.b2, path, k)
        fonk3(b5.b3, path, k)
        a1 = 0
        for j in range(len(path) - 1, -1, -1):
            a1 += path[j]
            if a1 = = k:
                print(*path[j:], b4 = " ")
        path.pop()
    def fonk4(b5, k, path):
        if b5 is None:
            return
        path.append(b5.b1)
        fonk3(b5, path, k)
        fonk4(b5.b2, k, path)
        fonk4(b5.b3, k, path)
        path.pop()
    fonk4(b5, k, [])
b5 = class1(1)
b5.b2 = class1(3)
b5.b2.b2 = class1(2)
b5.b2.b3 = class1(1)
b5.b2.b3.b2 = class1(1)
b5.b3 = class1(-1)
b5.b3.b2 = class1(4)
b5.b3.b2.b2 = class1(1)
b5.b3.b2.b3 = class1(2)
b5.b3.b3 = class1(5)
b5.b3.b3.b3 = class1(6)
print("Paths with sum 5:")
fonk2(b5, 5)
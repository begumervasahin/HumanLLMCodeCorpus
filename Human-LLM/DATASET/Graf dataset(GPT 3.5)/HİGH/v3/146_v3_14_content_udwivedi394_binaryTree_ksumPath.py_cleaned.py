class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b5, k):
    def fonk3(node, path, target_sum):
        if node is None:
            return
        path.append(node.b1)
        fonk3(node.b2, path, target_sum)
        fonk3(node.b3, path, target_sum)
        a1 = 0
        for i in range(len(path) - 1, -1, -1):
            a1 += path[i]
            if a1 = = target_sum:
                print(*path[i:], b4 = " ")
        path.pop()
    def fonk4(node, k, path):
        if node is None:
            return
        path.append(node.b1)
        fonk3(node, path, k)
        fonk4(node.b2, k, path)
        fonk4(node.b3, k, path)
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
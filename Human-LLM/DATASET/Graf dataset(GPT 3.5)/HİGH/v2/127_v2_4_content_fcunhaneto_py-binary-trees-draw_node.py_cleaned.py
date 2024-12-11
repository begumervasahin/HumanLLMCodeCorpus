class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.a1 = 0
        self.a2 = 0
        self.a3 = 1
b5 = class1(10)
b5.a1 = 3
b5.a2 = 4
b5.a3 = 1
b6 = class1(20)
b6.a1 = 2
b6.a2 = 3
b6.a3 = 0
print("Node 1:")
print("Key:", b5.b1)
print("Left Child:", b5.b2)
print("Right Child:", b5.b3)
print("Parent Node:", b5.b4)
print("Height:", b5.a1)
print("Real Height:", b5.a2)
print("Color:", b5.a3)
print("\nNode 2:")
print("Key:", b6.b1)
print("Left Child:", b6.b2)
print("Right Child:", b6.b3)
print("Parent Node:", b6.b4)
print("Height:", b6.a1)
print("Real Height:", b6.a2)
print("Color:", b6.a3)
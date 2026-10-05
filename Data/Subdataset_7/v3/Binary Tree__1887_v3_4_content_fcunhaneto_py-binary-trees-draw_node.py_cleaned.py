class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.a1 = 0
        self.a2 = 0
        self.a3 = 1
def fonk2(node):
    print(f"Key: {node.b1}")
    print(f"Left Child: {node.b2}")
    print(f"Right Child: {node.b3}")
    print(f"Parent Node: {node.b4}")
    print(f"Height: {node.a1}")
    print(f"Real Height: {node.a2}")
    print(f"Color: {'Red' if node.a3 = = 1 else 'Black'}")
if b5 = = "__main__":
    b6 = class1(10)
    b6.a1 = 3
    b6.a2 = 4
    b6.a3 = 1
    b7 = class1(20)
    b7.a1 = 2
    b7.a2 = 3
    b7.a3 = 0
    print("Node 1:")
    fonk2(b6)
    print("\nNode 2:")
    fonk2(b7)
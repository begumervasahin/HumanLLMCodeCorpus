class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.a1 = 0
        self.a2 = 0
        self.a3 = 1
if b5 = = "__main__":
    b6 = class1(10)
    b6.b2 = class1(5)
    b6.b3 = class1(15)
    b6.b2.b4 = b6
    b6.b3.b4 = b6
    print(f"class1 b1: {b6.b1}")
    print(f"Left child b1: {b6.b2.b1}")
    print(f"Right child b1: {b6.b3.b1}")
    print(f"Parent of b2 child: {b6.b2.b4.b1}")
    print(f"Parent of b3 child: {b6.b3.b4.b1}")
    print(f"class1 a1: {b6.a1}")
    print(f"class1 real a1: {b6.a2}")
    print(f"class1 a3: {b6.a3}")
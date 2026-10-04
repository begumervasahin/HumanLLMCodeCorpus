class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = set()
    def fonk2(self, b3):
        self.b1.append(b3)
        self.b2.add(tuple(b3.b1))
    def fonk3(self):
        if not self.fonk4():
            b3 = self.b1.pop(0)
            self.b2.remove(tuple(b3.b1))
            return b3
        else:
            return None
    def fonk4(self):
        return len(self.b1) == 0
if b4 = = "__main__":
    class class2:
        def fonk5(self, state_list):
            self.b1 = state_list
        def fonk6(self):
            return f"class2({self.b1})"
    b5 = class1()
    b5.fonk2(class2([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    b5.fonk2(class2([1, 2, 3, 4, 5, 6, 7, 0, 8]))
    print(f"class1 is empty: {b5.fonk4()}")
    b6 = b5.fonk3()
    print(f"Dequeued: {b6}")
    print(f"class1 is empty: {b5.fonk4()}")
    b6 = b5.fonk3()
    print(f"Dequeued: {b6}")
    print(f"class1 is empty: {b5.fonk4()}")
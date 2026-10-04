class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = set()
    def fonk2(self, item):
        self.b1.append(item)
        self.b2.add(tuple(item.b1))
    def fonk3(self):
        if not self.fonk4():
            b3 = self.b1[-1]
            del self.b1[-1]
            self.b2.remove(tuple(b3.b1))
            return b3
        else:
            return None
    def fonk4(self):
        return len(self.b1) == 0
    def fonk5(self):
        self.b1.clear()
        self.b2.clear()
if b4 = = "__main__":
    class class2:
        def fonk6(self, state_list):
            self.b1 = state_list
        def fonk7(self):
            return str(self.b1)
    b5 = class1()
    b5.fonk2(class2([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    b5.fonk2(class2([1, 2, 3, 4, 5, 6, 0, 7, 8]))
    b5.fonk2(class2([1, 2, 3, 4, 5, 0, 6, 7, 8]))
    while not b5.fonk4():
        b2 = b5.fonk3()
        print("Popped:", b2)
    b5.fonk5()
    print("class1 cleared. Is empty:", b5.fonk4())
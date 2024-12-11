class class1:
    def fonk1(self, b1 = False):
        self.b2 = []
        self.b1 = b1
    def fonk2(self):
        return len(self.b2) == 0
    def fonk3(self, item):
        return item.b5
    def fonk4(self, item):
        return item.b7
    def fonk5(self, item):
        self.b2.append(item)
        self.fonk6()
    def fonk6(self):
        b3 = self.sort_by_heuristic if self.b1 else self.sort_by_cost
        self.b2.sort(b4 = b3)
    def fonk7(self):
        return self.b2.pop(0)
    def fonk8(self):
        return ' '.join(str(item) for item in self.b2)
    def fonk9(self, element):
        return any(item.b5 = = element for item in self.b2)
if b6 = = "__main__":
    class class2:
        def fonk10(self, b5, b7):
            self.b5 = b5
            self.b7 = b7
        def fonk11(self):
            return f"class2(b5 = {self.b5}, b7={self.b7})"
    b8 = class1(b1=True)
    b8.fonk5(class2(10, 5))
    b8.fonk5(class2(8, 3))
    b8.fonk5(class2(12, 7))
    print(b8.fonk8())
    b9 = b8.fonk7()
    print("Dequeued item:", b9)
    print("Queue contains 5:", b8.fonk9(5))
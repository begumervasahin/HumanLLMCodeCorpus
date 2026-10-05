class class1:
    def fonk1(self, b1 = False):
        self.b2 = []
        self.b1 = b1
    def fonk2(self):
        return len(self.b2) == 0
    def fonk3(self, item):
        return item.b5
    def fonk4(self, item):
        return item.b6
    def fonk5(self, item):
        self.b2.append(item)
        if self.b1:
            self.b2.sort(b3 = self.sort_by_heuristic)
        else:
            self.b2.sort(b3 = self.sort_by_cost)
    def fonk6(self):
        return self.b2.pop(0)
    def fonk7(self):
        return ' '.join(str(item) for item in self.b2)
    def fonk8(self, element):
        return element in self.b2
if b4 = = "__main__":
    class class2:
        def fonk9(self, b5, b6):
            self.b5 = b5
            self.b6 = b6
        def fonk10(self):
            return f"class2(b5 = {self.b5}, b6={self.b6})"
    b7 = class1(b1=True)
    b7.fonk5(class2(10, 5))
    b7.fonk5(class2(8, 3))
    b7.fonk5(class2(12, 7))
    print(b7.fonk7())
    b8 = b7.fonk6()
    print("Dequeued item:", b8)
    print("Queue contains element with b5 5:", b7.fonk8(5))
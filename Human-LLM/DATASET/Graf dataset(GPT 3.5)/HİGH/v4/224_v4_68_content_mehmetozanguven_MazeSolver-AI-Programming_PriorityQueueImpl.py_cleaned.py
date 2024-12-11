class class1:
    def fonk1(self, b1 = False):
        self.b2 = []
        self.b1 = b1
    def fonk2(self):
        return len(self.b2) == 0
    def fonk3(self, item):
        return item.b6
    def fonk4(self, item):
        return item.b7
    def fonk5(self, item):
        self.b2.append(item)
        if self.b1:
            self.b2.sort(b3 = self.sort_by_heuristic)
        else:
            self.b2.sort(b3 = self.sort_by_cost)
    def fonk6(self):
        return self.b2.pop(0)
    def fonk7(self):
        return ' '.join(str(each_item) for each_item in self.b2)
    def fonk8(self, element):
        for b4 in self.b2:
            if b4 = = element:
                return True
        return False
if b5 = = "__main__":
    class class2:
        def fonk9(self, b6, b7):
            self.b6 = b6
            self.b7 = b7
        def fonk10(self):
            return f"class2(b6 = {self.b6}, b7={self.b7})"
    b8 = class1(b1=True)
    b8.fonk5(class2(10, 5))
    b8.fonk5(class2(8, 3))
    b8.fonk5(class2(12, 7))
    print(b8.fonk7())
    b9 = b8.fonk6()
    print("Dequeued item:", b9)
    print("Queue contains element with b6 5:", b8.fonk8(5))
class class1:
    def fonk1(self, b2):
        self.b1 = []
        self.b2 = b2
    def fonk2(self):
        return len(self.b1) == 0
    def fonk3(self, item):
        return item.b5
    def fonk4(self, item):
        return item.b6
    def fonk5(self, item):
        self.b1.append(item)
        if self.b2:
            self.b1.sort(b3 = self.sortComparatorByHeuristic)
        else:
            self.b1.sort(b3 = self.sortComparatorByCost)
    def fonk6(self):
        return self.b1.pop(0)
    def fonk7(self):
        return ' '.join(str(eachItem) for eachItem in self.b1)
    def fonk8(self, element):
        for eachElement in self.b1:
            if eachElement[0] == element:
                return True
        return False
if b4 = = "__main__":
    class class2:
        def fonk9(self, b5, b6):
            self.b5 = b5
            self.b6 = b6
        def fonk10(self):
            return f"class2(b5 = {self.b5}, b6={self.b6})"
    b7 = class1(b2=True)
    b7.fonk5(class2(10, 5))
    b7.fonk5(class2(8, 3))
    b7.fonk5(class2(12, 7))
    print(b7.fonk7())
    b8 = b7.fonk6()
    print("Dequeued item:", b8)
    print("Queue contains 5:", b7.fonk8(5))
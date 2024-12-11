class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        return "class1 object containing: {}".format(self.b1)
    def fonk3(self):
        b2 = len(self.b1)
        for i in range(b2):
            for j in range(0, b2-i-1):
                if self.b1[j] > self.b1[j+1]:
                    self.b1[j], self.b1[j+1] = self.b1[j+1], self.b1[j]
        return self.b1
    def fonk4(self):
        b2 = len(self.b1)
        for i in range(b2):
            for j in range(0, b2-i-1):
                if self.b1[j] < self.b1[j+1]:
                    self.b1[j], self.b1[j+1] = self.b1[j+1], self.b1[j]
        return self.b1
def fonk5(lst, b2):
    a1 = 0
    b3 = len(lst) - 1
    while a1 <= b3:
        b4 = (a1 + b3)
        if lst[b4] < b2:
            a1 = b4 + 1
        elif lst[b4] > b2:
            b3 = b4 - 1
        else:
            return b4
    return a1
def fonk6(b2, lst):
    b5 = fonk5(lst, b2)
    lst.insert(b5, b2)
    return lst
b1 = [5, 2, 9, 1, 7]
b6 = class1(b1)
print("Ascending:", b6.fonk3())
print("Descending:", b6.fonk4())
b7 = [1, 3, 5, 7, 9]
print("Updated list:", fonk6(4, b7))
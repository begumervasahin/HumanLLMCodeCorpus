class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        return f"class1 object containing: {self.b1}"
    def fonk3(self, b2 = False):
        b3 = len(self.b1)
        for i in range(b3):
            for j in range(0, b3-i-1):
                if b2:
                    if self.b1[j] < self.b1[j+1]:
                        self.b1[j], self.b1[j+1] = self.b1[j+1], self.b1[j]
                else:
                    if self.b1[j] > self.b1[j+1]:
                        self.b1[j], self.b1[j+1] = self.b1[j+1], self.b1[j]
        return self.b1
def fonk4(lst, target):
    a1 = 0
    b4 = len(lst) - 1
    while a1 <= b4:
        b5 = (a1 + b4)
        if lst[b5] < target:
            a1 = b5 + 1
        elif lst[b5] > target:
            b4 = b5 - 1
        else:
            return b5
    return a1
def fonk5(lst, b3):
    b6 = fonk4(lst, b3)
    lst.insert(b6, b3)
    return lst
b1 = [5, 2, 9, 1, 7]
b7 = class1(b1)
print("Ascending:", b7.fonk3())
print("Descending:", b7.fonk3(b2 = True))
b8 = [1, 3, 5, 7, 9]
print("Updated list:", fonk5(b8, 4))
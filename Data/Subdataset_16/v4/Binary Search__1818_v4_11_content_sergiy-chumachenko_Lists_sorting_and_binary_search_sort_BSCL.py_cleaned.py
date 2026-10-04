class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        return "class1 method can be used to sort your list:\b2{}".format(self.b1)
    def fonk3(self):
        b2 = len(self.b1)
        for i in range(b2 - 1):
            b3 = False
            for j in range(b2 - 1 - i):
                if self.b1[j] > self.b1[j + 1]:
                    self.b1[j], self.b1[j + 1] = self.b1[j + 1], self.b1[j]
                    b3 = True
            if not b3:
                break
        return self.b1
    def fonk4(self):
        b2 = len(self.b1)
        for i in range(b2 - 1):
            b3 = False
            for j in range(b2 - 1 - i):
                if self.b1[j] < self.b1[j + 1]:
                    self.b1[j], self.b1[j + 1] = self.b1[j + 1], self.b1[j]
                    b3 = True
            if not b3:
                break
        return self.b1
def fonk5(b11, b6):
    b7, b4 = 0, len(b11) - 1
    while b7 <= b4:
        b5 = (b7 + b4)
        if b6 = = b11[b5]:
            return b5
        elif b6 > b11[b5]:
            b7 = b5 + 1
        else:
            b4 = b5 - 1
    return b7
def fonk6(b2, b11):
    if not b11:
        b11.append(b2)
    else:
        b8 = fonk5(b11, b2)
        b11.insert(b8, b2)
    return b11
if b9 = = "__main__":
    b10 = class1([34, 10, -5, 72, 0, 8])
    print(b10)
    print("Sorted in ascending order:", b10.fonk3())
    print("Sorted in descending order:", b10.fonk4())
    b11 = [10, 20, 30, 40]
    print("Inserting 25 into sorted list:", fonk6(25, b11))
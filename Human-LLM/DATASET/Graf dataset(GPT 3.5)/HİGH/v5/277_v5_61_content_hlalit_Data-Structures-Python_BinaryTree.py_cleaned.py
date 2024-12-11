class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, data_list):
        self.b4 = self.fonk4(data_list, self.b4, 0)
    def fonk4(self, data_list, b6, index):
        if index < len(data_list):
            if data_list[index] is not None:
                b5 = class1(data_list[index])
                b6 = b5
                b6.b2 = self.fonk4(data_list, b6.b2, 2 * index + 1)
                b6.b3 = self.fonk4(data_list, b6.b3, 2 * index + 2)
        return b6
    def fonk5(self, b6):
        if b6 is None:
            return
        self.fonk5(b6.b2)
        print(b6.b1)
        self.fonk5(b6.b3)
    def fonk6(self, b6):
        if b6 is None:
            return
        b7 = [b6]
        while b7:
            b8 = b7.pop(0)
            print(b8.b1)
            if b8.b2:
                b7.append(b8.b2)
            if b8.b3:
                b7.append(b8.b3)
    def fonk7(self, b6):
        if b6 is None:
            return -1
        b9 = self.fonk7(b6.b2)
        b10 = self.fonk7(b6.b3)
        return max(b9, b10) + 1
b11 = class2()
b11.fonk3([2, 3, 5, 7, 1, 10, 9, 8])
b11.fonk5(b11.b4)
print()
b11.fonk6(b11.b4)
print()
print(b11.fonk7(b11.b4))
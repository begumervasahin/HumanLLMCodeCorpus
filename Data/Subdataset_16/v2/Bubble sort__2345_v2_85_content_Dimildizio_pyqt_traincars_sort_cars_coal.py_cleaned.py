from random import randint, choice
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return f'class1(b2 = {self.b2}, b1={self.b1})'
    def fonk3(self, other):
        return self.b1 = = other.b1
    def fonk4(self, other):
        return self.b1 > other.b1
    def fonk5(self, other):
        return self.b1 < other.b1
    def fonk6(self, other):
        return self.b1 >= other.b1
    def fonk7(self, other):
        return self.b1 <= other.b1
    def fonk8(self, other):
        return self.b1 != other.b1
class class2:
    def fonk9(self, num_cars):
        self.b3 = [class1(randint(1, 74), randint(1, 1000)) for _ in range(num_cars)]
    def fonk10(self):
        return f'This is a b15 with {len(self.b3)} b3:\n' + '\n'.join(f'\t{car}' for car in self.b3)
    def fonk11(self, b4, value):
        if b4 = = 'b1':
            b5 = class1(value, randint(1, 1000))
        else:
            b5 = class1(randint(1, 74), value)
        self.b3.append(b5)
        return b5
    def fonk12(self, b6 = True, b4='b1'):
        for _ in range(len(self.b3) - 1):
            b7 = False
            for i in range(len(self.b3) - 1):
                if (getattr(self.b3[i], b4) > getattr(self.b3[i + 1], b4)) == b6:
                    self.b3[i], self.b3[i + 1] = self.b3[i + 1], self.b3[i]
                    b7 = True
            if not b7:
                break
    def fonk13(self, b6 = True, b4='b1'):
        for i in range(1, len(self.b3)):
            b8 = self.b3[i]
            b9 = i - 1
            while b9 >= 0 and (getattr(b8, b4) < getattr(self.b3[b9], b4)) == b6:
                self.b3[b9 + 1] = self.b3[b9]
                b9 -= 1
            self.b3[b9 + 1] = b8
    def fonk14(self, b6 = True, b4='b1'):
        for i in range(len(self.b3)):
            b10 = i
            for b9 in range(i + 1, len(self.b3)):
                if (getattr(self.b3[b9], b4) < getattr(self.b3[b10], b4)) == b6:
                    b10 = b9
            if b10 != i:
                self.b3[i], self.b3[b10] = self.b3[b10], self.b3[i]
    def fonk15(self, value, b4 = 'b1', b6=True):
        b13, b11 = 0, len(self.b3) - 1
        while b13 <= b11:
            b12 = (b13 + b11)
            if getattr(self.b3[b12], b4) == value:
                return self.b3[b12]
            elif (getattr(self.b3[b12], b4) < value) == b6:
                b13 = b12 + 1
            else:
                b11 = b12 - 1
        return None
    def fonk16(self, value, b4 = 'b1', b6=True):
        b14 = choice([self.bubble_sort, self.insertion_sort, self.selection_sort])
        b14(b6 = b6, b4=b4)
        return self.fonk15(value, b4 = b4, b6=b6)
    def fonk17(self, car):
        self.b3.remove(car)
class class3:
    b15 = None
    @classmethod
    def fonk18(cls, num_cars):
        cls.b15 = class2(num_cars)
    @classmethod
    def fonk19(cls):
        cls.b15 = None
if b16 = = '__main__':
    class3.fonk18(10)
    print(class3.b15)
    class3.b15.fonk12(b6 = True)
    print("After bubble sort (b6):", class3.b15)
    b17 = class3.b15.fonk16(50)
    print("Found car:", b17)
    if b17:
        class3.b15.fonk17(b17)
        print("After destroying a car:", class3.b15)
    class3.fonk19()
    print("class2 after demolish:", class3.b15)
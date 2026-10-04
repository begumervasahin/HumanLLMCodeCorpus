from random import randint, choice
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return f'class1(b1 = {self.b1}, b2={self.b2})'
    def fonk3(self, other):
        if isinstance(other, class1):
            return self.b2 = = other.b2
        return self.b2 = = other
    def fonk4(self, other):
        if isinstance(other, class1):
            return self.b2 > other.b2
        return self.b2 > other
    def fonk5(self, other):
        if isinstance(other, class1):
            return self.b2 < other.b2
        return self.b2 < other
    def fonk6(self, other):
        if isinstance(other, class1):
            return self.b2 >= other.b2
        return self.b2 >= other
    def fonk7(self, other):
        if isinstance(other, class1):
            return self.b2 <= other.b2
        return self.b2 <= other
    def fonk8(self, other):
        if isinstance(other, class1):
            return self.b2 != other.b2
        return self.b2 != other
class class2:
    def fonk9(self, num_cars):
        self.b3 = [class1(randint(1, 74), randint(1, 1000)) for _ in range(num_cars)]
    def fonk10(self):
        return f'This is a b17 with {len(self.b3)} b3:\b6' + '\b6\t'.join(map(str, self.b3))
    def fonk11(self, b2, b1 = None):
        b1 = b1 if b1 else randint(1, 1000)
        b4 = class1(b2, b1)
        self.b3.append(b4)
        return b4
    def fonk12(self, b5 = True, b11='b2'):
        b6 = len(self.b3)
        for i in range(b6 - 1):
            b7 = False
            for b9 in range(b6 - 1 - i):
                if (getattr(self.b3[b9], b11) > getattr(self.b3[b9 + 1], b11)) == b5:
                    self.b3[b9], self.b3[b9 + 1] = self.b3[b9 + 1], self.b3[b9]
                    b7 = True
            if not b7:
                break
    def fonk13(self, b5 = True, b11='b2'):
        for i in range(1, len(self.b3)):
            b8 = self.b3[i]
            b9 = i - 1
            while b9 >= 0 and (getattr(b8, b11) < getattr(self.b3[b9], b11)) == b5:
                self.b3[b9 + 1] = self.b3[b9]
                b9 -= 1
            self.b3[b9 + 1] = b8
    def fonk14(self, b5 = True, b11='b2'):
        for i in range(len(self.b3)):
            b10 = i
            for b9 in range(i + 1, len(self.b3)):
                if (getattr(self.b3[b9], b11) < getattr(self.b3[b10], b11)) == b5:
                    b10 = b9
            if b10 != i:
                self.b3[i], self.b3[b10] = self.b3[b10], self.b3[i]
    def fonk15(self, value, b11 = 'b2', b5=True):
        b15, b12 = 0, len(self.b3) - 1
        while b15 <= b12:
            b13 = (b15 + b12)
            b14 = getattr(self.b3[b13], b11)
            if b14 = = value:
                return self.b3[b13]
            elif (b14 < value) == b5:
                b15 = b13 + 1
            else:
                b12 = b13 - 1
        return None
    def fonk16(self, value, b11 = 'b2', b5=True):
        b16 = choice([self.selection_sort, self.insertion_sort, self.bubble_sort])
        b16(b5, b11)
        return self.fonk15(value, b11, b5)
    def fonk17(self, b1):
        self.fonk13(b11 = 'b1')
        return self.fonk15(b1, b11 = 'b1')
    def fonk18(self, b4):
        self.b3.remove(b4)
        return b4
class class3:
    b17 = None
    @classmethod
    def fonk19(cls, num_cars):
        cls.b17 = class2(num_cars)
    @classmethod
    def fonk20(cls):
        cls.b17 = None
if b18 = = "__main__":
    class3.fonk19(10)
    print(class3.b17)
    print("\nAdding a b4 with 50 b2:")
    class3.b17.fonk11(50)
    print(class3.b17)
    print("\nFinding a b4 with 50 b2:")
    b19 = class3.b17.fonk16(50, 'b2')
    print(b19)
    print("\nSorting b3 by b2 in b5 order:")
    class3.b17.fonk12()
    print(class3.b17)
    if b19:
        print("\nDestroying the found b4:")
        class3.b17.fonk18(b19)
        print(class3.b17)
'''
b3 with random amount of b2
sort b3
override operators <=> for binary search
create class class1 of b3
sorting algorithm Bubble, insertion sorting algorithm
method of binary search of a b6 with certain amount of b2
'''
from random import randint, choice
class class2:
    def fonk1(self, b2, b1):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return f'class2
    def fonk3(self, another):
        return self.b2 = = another
    def fonk4(self, another):
        return self.b2 > another
    def fonk5(self, another):
        return self.b2 < another
    def fonk6(self, another):
        return self.b2 >= another
    def fonk7(self, another):
        return self.b2 <= another
    def fonk8(self, another):
        return self.b2 != another
class class3:
    def fonk9(self, b3):
        self.b3 = [class2(randint(1,74), randint(1,1000)) for x in range(b3)]
    def fonk10(self):
        b4 = f'This is a b17 with {len(self.b3)} b3: '
        for x in self.b3:
            b4 += '\n\t' + str(x)
        return b4
    def fonk11(self, b5, num):
        if b5 = = 'b2':
            b6 = class2(num, randint(1,1000))
        else:
            b6 = class2(randint(1,74), num)
        self.b3.append(b6)
        return b6
    def fonk12(self, b7 = True):
        b7 = 'b2' if b7 else 'b1'
        for x in range (len(self.b3)-1, 0, -1):
            b8 = True
            for y in range (x):
                if getattr(self.b3[y],b7) > getattr(self.b3[y+1], b7):
                    self.b3[y],self.b3[y+1] = self.b3[y+1], \
                    self.b3[y]
                    b8 = False
            if b8:
                break
    def fonk13(self, b7 = True):
        b7 = 'b2' if b7 else 'b1'
        for x in range (len(self.b3)-1):
            b8 = True
            for y in range (len(self.b3)-x-1):
                if getattr(self.b3[y], b7) < getattr(
                    self.b3[y+1], b7):
                    self.b3[y],self.b3[y+1] = self.b3[y+1], \
                    self.b3[y]
                    b8 = False
            if b8: break
    def fonk14(self, b7 = True):
        b7 = 'b2' if b7 else 'b1'
        for x in range(1, len(self.b3)):
            b9 = self.b3[x]
            b10 = x - 1
            while getattr(b9, b7 )< getattr(self.b3[
                b10], b7) and b10 >= 0:
                self.b3[b10+1] = self.b3[b10]
                b10 -= 1
            self.b3[b10+1] = b9
    def fonk15(self, b7 = True):
        b7 = 'b2' if b7 else 'b1'
        for x in range(1, len(self.b3)):
            b9 = self.b3[x]
            b10 = x - 1
            while getattr(b9, b7) > getattr(
                self.b3[b10], b7) and b10 >= 0:
                self.b3[b10+1] = self.b3[b10]
                b10 -= 1
            self.b3[b10+1] = b9
    def fonk16(self, b7 = True):
        b7 = 'b2' if b7 else 'b1'
        for i in range(len(self.b3)-1):
            b11 = i
            for j in range(i+1, len(self.b3)):
                if getattr(self.b3[j], b7) < getattr(
                    self.b3[b11], b7):
                    b11 = j
            if b11 != i:
                self.b3[b11], self.b3[i] = \
                                       self.b3[i], self.b3[b11]
    def fonk17(self, b7 = True):
        b7 = 'b2' if b7 else 'b1'
        for i in range(len(self.b3)-1):
            b11 = i
            for j in range(i+1, len(self.b3)):
                if getattr(self.b3[j], b7) > getattr(
                    self.b3[b11], b7):
                    b11 = j
            if b11 != i:
                self.b3[b11], self.b3[i] = \
                                       self.b3[i], self.b3[b11]
    def fonk18(self, value):
        b12 = len(self.b3)-1
        a1 = 0
        while a1 <= b12:
            b13 = (b12 + a1)
            if self.b3[b13] == value:
                return self.b3[b13]
            elif self.b3[b13] > value:
                b12 = b13 - 1
            else:
                a1 = b13 + 1
        return False
    def fonk19(self, value):
        b12 = len(self.b3)-1
        a1 = 0
        while a1 <= b12:
            b13 = (b12 + a1)
            if self.b3[b13] == value:
                return self.b3[b13]
            elif self.b3[b13] < value:
                b12 = b13 - 1
            else:
                a1 = b13 + 1
        return False
    def fonk20(self, value):
        self.fonk14(0)
        b12 = len(self.b3)-1
        a1 = 0
        while a1 <= b12:
            b13 = (b12 + a1)
            if self.b3[b13].b1 = = value:
                return self.b3[b13]
            elif self.b3[b13].b1 > value:
                b12 = b13 - 1
            else:
                a1 = b13 + 1
        return False
    def fonk21(self, value, b14 = True):
        if b14:
            b15 = choice([self.select_sort_to_right,
                             self.insertion_sort_to_right,
                             self.bubble_sort_to_right])
            b15()
            return self.fonk18(value)
        else:
            b15 = choice([self.select_sort_to_left,
                             self.insertion_sort_to_left,
                             self.bubble_sort_to_left])
            b15()
            return self.fonk19(value)
    def fonk22(self, value, b16):
        if b16 = = 'b2':
            return self.fonk21(value)
        elif b16 = = 'b1':
            return self.fonk20(value)
        else:
            try:
                return self.b3[value]
            except IndexError:
                return False
    def fonk23(self, b6):
        self.b3.remove(b6)
        return b6
class class4:
    b17 = False
    @classmethod
    def fonk24(cls, value):
        cls.b17 = class3(value)
    @classmethod
    def fonk25(cls):
        cls.b17 = False
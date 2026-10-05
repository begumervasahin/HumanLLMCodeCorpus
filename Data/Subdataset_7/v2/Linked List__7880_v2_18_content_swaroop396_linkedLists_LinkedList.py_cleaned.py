class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b5):
        b2 = class2(b5)
        b2.fonk7(self.b1)
        self.b1 = b2
    def fonk3(self, b5):
        b3 = self.b1
        b2 = class2(b5)
        while b3.fonk9():
            b3 = b3.fonk9()
        b3.fonk7(b2)
    def fonk4(self):
        b3 = self.b1
        if b3 is None:
            print("Empty List!!!")
            return
        while b3:
            print(str(b3.fonk8()), b4 = " ")
            b3 = b3.b6
            if b3:
                print("-->", b4 = " ")
        print()
class class2:
    def fonk5(self, b5 = None, b6=None):
        self.b5 = b5
        self.b6 = b6
    def fonk6(self, b5):
        self.b5 = b5
    def fonk7(self, node):
        self.b6 = node
    def fonk8(self):
        return self.b5
    def fonk9(self):
        return self.b6
b7 = class1()
b7.fonk2(5)
b7.fonk2(4)
b7.fonk2(3)
b7.fonk2(2)
b7.fonk2(1)
b7.fonk4()
b7.fonk3(12)
b7.fonk3(13)
b7.fonk3(3)
b7.fonk4()
print(b7.length())
print(b7.index(3))
print(b7.at_index(5))
print(b7.remove(12))
b7.remove_position(2)
b7.fonk4()
print(b7.max_value())
print(b7.min_value())
b7.push(31)
b7.fonk4()
print(b7.pop())
b7.fonk4()
b8 = b7.copy()
b8.fonk4()
b8.clear()
b8.fonk4()
print(b7.to_string(","))
print(b7.count(3))
b9 = b7.to_list()
print(b9)
b10 = b7.to_set()
print(b10)
b7.reverse()
b7.fonk4()
b11 = b7.sorted()
b11.fonk4()
b7.sort()
b7.fonk4()
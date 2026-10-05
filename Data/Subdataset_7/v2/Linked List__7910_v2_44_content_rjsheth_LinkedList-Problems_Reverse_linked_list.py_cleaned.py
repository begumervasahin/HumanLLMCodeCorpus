class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        if not self.b3:
            self.b3 = b4
        else:
            b5 = self.b3
            while b5.b2:
                b5 = b5.b2
            b5.b2 = b4
    def fonk4(self, b1):
        b5 = self.b3
        if b5 and b5.b1 = = b1:
            self.b3 = b5.b2
            return
        while b5:
            if b5.b1 = = b1:
                break
            b6 = b5
            b5 = b5.b2
        if b5:
            b6.b2 = b5.b2
            del b5
    def fonk5(self):
        if not self.b3:
            return "Empty"
        b7 = ""
        b5 = self.b3
        while b5:
            b7 += str(b5.b1) + " -> "
            b5 = b5.b2
        return b7[:-4]
def fonk6(lst):
    b8 = class2()
    for i in lst:
        b8.fonk3(i)
    print("input list: ", b8)
    b9 = b8.b3
    b10 = None
    b11 = None
    if b9:
        b11 = b9.b2
    while b9:
        b9.b2 = b10
        b10 = b9
        b9 = b11
        if b9:
            b11 = b9.b2
    b8.b3 = b10
    return b8
print('\nReverse and deleting in Singly Linked List \n')
b12 = (1, 2, 3, 4, 5)
b13 = fonk6(b12)
print("output list: ", b13)
print("deleting 3")
b13.fonk4(3)
print("output list after delete: ", b13)
print('')
b14 = ('org', 'com', 'her', 'him', 'blah')
b15 = fonk6(b14)
print("output list: ", b15)
print("deleting 'org'")
b15.fonk4('org')
print("output list after delete: ", b15)
print('')
b16 = (1, 'com', 3, 'him', 5)
b17 = fonk6(b16)
print("output list: ", b17)
print('')
b18 = class2()
b18.fonk3('Fa')
b18.fonk3('la')
b18.fonk3('al')
b18.fonk3('ta')
b19 = (1, 'com', b18, 'him', 5)
b20 = fonk6(b19)
print("output list: ", b20)
print('')
b21 = ('B',)
b22 = fonk6(b21)
print("output list: ", b22)
print("deleting 'B'")
b22.fonk4('B')
print("output list after delete: ", b22)
print('')
b23 = ('B', 'B', 'B', 'B')
b24 = fonk6(b23)
print("output list: ", b24)
print("deleting 'B'")
b24.fonk4('B')
print("output list after delete: ", b24)
print('')
b25 = ()
b26 = fonk6(b25)
print("output list: ", b26)
print('')
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self, b1):
        b5 = self.b3
        b6 = None
        while b5:
            if b5.b1 = = b1:
                if b6:
                    b6.b2 = b5.b2
                else:
                    self.b3 = b5.b2
                return
            b6 = b5
            b5 = b5.b2
        print(f"Value {b1} not found in the list.")
    def fonk5(self):
        b7 = []
        b5 = self.b3
        while b5:
            b7.append(str(b5.b1))
            b5 = b5.b2
        return " -> ".join(b7) + " -> None"
def fonk6(input_list):
    b8 = class2()
    for i in input_list:
        b8.fonk3(i)
    print("input list: ", b8)
    b5 = b8.b3
    b6 = None
    b9 = None
    while b5:
        b9 = b5.b2
        b5.b2 = b6
        b6 = b5
        b5 = b9
    b8.b3 = b6
    return b8
if b10 = = "__main__":
    print('\nReverse and deleting in Singly Linked List \n')
    b11 = (1, 2, 3, 4, 5)
    b12 = fonk6(b11)
    print("output list: ", b12)
    print("deleting 3")
    b12.fonk4(3)
    print("output list after delete: ", b12)
    print('')
    b13 = ('org', 'com', 'her', 'him', 'blah')
    b14 = fonk6(b13)
    print("output list: ", b14)
    print("deleting 'org'")
    b14.fonk4('org')
    print("output list after delete: ", b14)
    print('')
    b15 = (1, 'com', 3, 'him', 5)
    b16 = fonk6(b15)
    print("output list: ", b16)
    print('')
    b17 = class2()
    b17.fonk3('Fa')
    b17.fonk3('la')
    b17.fonk3('al')
    b17.fonk3('ta')
    b18 = (1, 'com', b17, 'him', 5)
    b19 = fonk6(b18)
    print("output list: ", b19)
    print('')
    b20 = ('B',)
    b21 = fonk6(b20)
    print("output list: ", b21)
    print("deleting 'B'")
    b21.fonk4('B')
    print("output list after delete: ", b21)
    print('')
    b22 = ('B', 'B', 'B', 'B')
    b23 = fonk6(b22)
    print("output list: ", b23)
    print("deleting 'B'")
    b23.fonk4('B')
    print("output list after delete: ", b23)
    print('')
    b24 = ()
    b25 = fonk6(b24)
    print("output list: ", b25)
    print('')
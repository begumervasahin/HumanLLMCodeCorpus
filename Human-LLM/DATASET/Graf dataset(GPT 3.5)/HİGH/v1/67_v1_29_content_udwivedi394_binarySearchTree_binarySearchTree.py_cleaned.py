class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b1):
        if self.b4 is None:
            self.b4 = class1(b1)
            return
        b5 = self.b4
        while b5:
            b6 = b5
            if b1 < b5.b1:
                b5 = b5.b2
            elif b1 >= b5.b1:
                b5 = b5.b3
        if b1 < b6.b1:
            b6.b2 = class1(b1)
        else:
            b6.b3 = class1(b1)
    def fonk4(self):
        if self.b4 is None:
            print("Nothing to print")
            return
        print("\nIn Order:", b7 = " ")
        b8 = []
        b5 = self.b4
        while True:
            while b5:
                b8.append(b5)
                b5 = b5.b2
            while b5 is None and b8:
                b5 = b8.pop()
                print(b5.b1, b7 = " ")
                b5 = b5.b3
            if b5 is None and not b8:
                break
        print()
    def fonk5(self):
        if self.b4 is None:
            print("No Tree")
            return
        print("\nLevel Order:")
        b9 = []
        b5 = self.b4
        b9.append(b5)
        while b9:
            b10 = len(b9)
            while b10:
                b5 = b9.pop(0)
                if b5.b2:
                    b9.append(b5.b2)
                if b5.b3:
                    b9.append(b5.b3)
                print(b5.b1, b7 = " ")
                b10 -= 1
            print()
    def fonk6(self, b1, del_operation):
        b5 = self.b4
        b6 = None
        print()
        while b5:
            if b5.b1 = = b1:
                print("%d b13!" % b1)
                if del_operation:
                    return b6
                return True
            b6 = b5
            if b1 < b5.b1:
                b5 = b5.b2
            else:
                b5 = b5.b3
        print("%d not present" % b1)
        if del_operation:
            return None
        return False
    def fonk7(self, b1):
        b6 = self.fonk6(b1, True)
        if b6 is None and self.b4.b1 != b1:
            print("class1 to be deleted not b13!")
            return False
        b2 = True
        if b6 is None:
            b11 = self.b4
        elif b1 < b6.b1:
            b11 = b6.b2
        elif b1 > b6.b1:
            b11 = b6.b3
            b2 = False
        if b6 and ((b11.b2 is None) ^ (b11.b3 is None) or b11.b2 is None):
            print("I'm coming here")
            if b2:
                b6.b2 = b11.b2
            else:
                b6.b3 = b11.b3
            return
        if b6 is None:
            if b11.b2 is None and b11.b3 is None:
                self.b4 = None
            elif b11.b2 is None:
                self.b4 = b11.b3
            elif b11.b3 is None:
                self.b4 = b11.b2
            return
        b5 = b11.b3
        b6 = b11
        while b5 and b5.b2:
            b6 = b5
            b5 = b5.b2
        b11.b1 ^= b5.b1
        b5.b1 ^= b11.b1
        b11.b1 ^= b5.b1
        b6.b2 = None
        return None
    def fonk8(self, b14):
        b8 = []
        b5 = self.b4
        while True:
            while b5:
                b8.append(b5)
                b5 = b5.b2
            while b5 is None and b8:
                b5 = b8.pop()
                b14 -= 1
                if b14 <= 0:
                    print(b5.b1, b7 = " ")
                    return
                b5 = b5.b3
            if b5 is None and not b8:
                break
    def fonk9(self, b14):
        b5 = self.b4
        b12 = None
        b13 = False
        while b5:
            if b14 = = b5.b1:
                b13 = True
                break
            elif b14 < b5.b1:
                b12 = b5
                b5 = b5.b2
            else:
                b5 = b5.b3
        if not b13:
            print("Element not b13")
            return False
        if b12 is None:
            print("Last class1, no b12 present!")
            return False
        if b5.b3:
            b5 = b5.b3
            while b5.b2:
                b5 = b5.b2
            return b5.b1
        return b12.b1
    def fonk10(self):
        return self.b4
b15 = class2()
b15.fonk3(50)
b15.fonk3(30)
b15.fonk3(20)
b15.fonk3(40)
b15.fonk3(70)
b15.fonk3(60)
b15.fonk3(80)
print("Inorder Traversal:")
b15.fonk4()
print("\nLevel Order Traversal:")
b15.fonk5()
b15.fonk7(20)
b15.fonk7(30)
print("\nInorder Traversal after deleting 20 and 30:")
b15.fonk4()
print("\nKth b11 (2nd) in Inorder Traversal:")
b15.fonk8(2)
print("\nInorder Successor of 50:")
print(b15.fonk9(50))
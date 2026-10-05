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
            else:
                b5 = b5.b3
        if b1 < b6.b1:
            b6.b2 = class1(b1)
        else:
            b6.b3 = class1(b1)
    def fonk4(self):
        if self.b4 is None:
            print("Tree is empty")
            return
        print("\nIn Order Traversal:", b7 = " ")
        b8 = []
        b5 = self.b4
        while True:
            while b5:
                b8.append(b5)
                b5 = b5.b2
            while not b5 and b8:
                b5 = b8.pop()
                print(b5.b1, b7 = " ")
                b5 = b5.b3
            if not b5 and not b8:
                break
        print()
    def fonk5(self):
        if self.b4 is None:
            print("Tree is empty")
            return
        print("\nLevel Order Traversal:")
        b9 = [self.b4]
        while b9:
            b10 = len(b9)
            for _ in range(b10):
                b5 = b9.pop(0)
                print(b5.b1, b7 = " ")
                if b5.b2:
                    b9.append(b5.b2)
                if b5.b3:
                    b9.append(b5.b3)
            print()
    def fonk6(self, b1):
        if self.b4 is None:
            print("Tree is empty")
            return False
        b5 = self.b4
        while b5:
            if b5.b1 = = b1:
                print("%d found!" % b1)
                return True
            elif b1 < b5.b1:
                b5 = b5.b2
            else:
                b5 = b5.b3
        print("%d not present" % b1)
        return False
    def fonk7(self, b1):
        if self.b4 is None:
            print("Tree is empty")
            return False
        b11 = None
        b12 = self.b4
        while b12 and b12.b1 != b1:
            b11 = b12
            if b1 < b12.b1:
                b12 = b12.b2
            else:
                b12 = b12.b3
        if not b12:
            print("class1 not found")
            return False
        if not b12.b2 or not b12.b3:
            if not b12.b2:
                b13 = b12.b3
            else:
                b13 = b12.b2
            if not b11:
                self.b4 = b13
            elif b12 is b11.b2:
                b11.b2 = b13
            else:
                b11.b3 = b13
        else:
            b14 = b12.b3
            b15 = b12
            while b14.b2:
                b15 = b14
                b14 = b14.b2
            b12.b1 = b14.b1
            if b14 is not b12.b3:
                b15.b2 = b14.b3
            else:
                b15.b3 = b14.b3
        return True
    def fonk8(self, b16):
        if self.b4 is None:
            print("Tree is empty")
            return
        b8 = []
        b5 = self.b4
        while True:
            while b5:
                b8.append(b5)
                b5 = b5.b2
            while not b5 and b8:
                b5 = b8.pop()
                b16 -= 1
                if b16 = = 0:
                    print(b5.b1, b7 = " ")
                    return
                b5 = b5.b3
            if not b5 and not b8:
                break
    def fonk9(self, b1):
        if self.b4 is None:
            print("Tree is empty")
            return
        b5 = self.b4
        b14 = None
        while b5:
            if b1 = = b5.b1:
                break
            elif b1 < b5.b1:
                b14 = b5
                b5 = b5.b2
            else:
                b5 = b5.b3
        if not b5:
            print("Element not found")
            return
        if b5.b3:
            b5 = b5.b3
            while b5.b2:
                b5 = b5.b2
            return b5.b1
        return b14.b1 if b14 else None
    def fonk10(self):
        return self.b4
b17 = class2()
b17.fonk3(50)
b17.fonk3(30)
b17.fonk3(20)
b17.fonk3(40)
b17.fonk3(70)
b17.fonk3(60)
b17.fonk3(80)
print("Inorder Traversal:")
b17.fonk4()
print("\nLevel Order Traversal:")
b17.fonk5()
b17.fonk7(20)
b17.fonk7(30)
print("\nInorder Traversal after deleting 20 and 30:")
b17.fonk4()
print("\nKth node (2nd) in Inorder Traversal:")
b17.fonk8(2)
print("\nInorder Successor of 50:")
print(b17.fonk9(50))
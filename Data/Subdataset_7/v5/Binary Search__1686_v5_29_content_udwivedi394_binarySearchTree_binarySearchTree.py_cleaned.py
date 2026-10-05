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
        b5 = None
        b6 = self.b4
        while b6:
            b5 = b6
            if b1 < b6.b1:
                b6 = b6.b2
            else:
                b6 = b6.b3
        if b1 < b5.b1:
            b5.b2 = class1(b1)
        else:
            b5.b3 = class1(b1)
    def fonk4(self):
        if self.b4 is None:
            print("Tree is empty")
            return
        print("\nIn Order Traversal:", b7 = " ")
        b8 = []
        b9 = self.b4
        while b9 or b8:
            while b9:
                b8.append(b9)
                b9 = b9.b2
            b9 = b8.pop()
            print(b9.b1, b7 = " ")
            b9 = b9.b3
        print()
    def fonk5(self):
        if self.b4 is None:
            print("Tree is empty")
            return
        print("\nLevel Order Traversal:")
        b10 = [self.b4]
        while b10:
            b9 = b10.pop(0)
            print(b9.b1, b7 = " ")
            if b9.b2:
                b10.append(b9.b2)
            if b9.b3:
                b10.append(b9.b3)
        print()
    def fonk6(self, b1):
        if self.b4 is None:
            print("Tree is empty")
            return False
        b9 = self.b4
        while b9:
            if b9.b1 = = b1:
                print("%d found!" % b1)
                return True
            elif b1 < b9.b1:
                b9 = b9.b2
            else:
                b9 = b9.b3
        print("%d not present" % b1)
        return False
    def fonk7(self, b1):
        if self.b4 is None:
            print("Tree is empty")
            return False
        b5 = None
        b6 = self.b4
        while b6 and b6.b1 != b1:
            b5 = b6
            if b1 < b6.b1:
                b6 = b6.b2
            else:
                b6 = b6.b3
        if not b6:
            print("class1 not found")
            return False
        if not b6.b2 or not b6.b3:
            b11 = b6.b2 if b6.b2 else b6.b3
            if not b5:
                self.b4 = b11
            elif b6 is b5.b2:
                b5.b2 = b11
            else:
                b5.b3 = b11
        else:
            b12 = b6.b3
            b13 = b6
            while b12.b2:
                b13 = b12
                b12 = b12.b2
            b6.b1 = b12.b1
            if b12 is not b6.b3:
                b13.b2 = b12.b3
            else:
                b13.b3 = b12.b3
        return True
    def fonk8(self, b14):
        if self.b4 is None:
            print("Tree is empty")
            return
        b8 = []
        b9 = self.b4
        while b9 or b8:
            while b9:
                b8.append(b9)
                b9 = b9.b2
            b9 = b8.pop()
            b14 -= 1
            if b14 = = 0:
                print(b9.b1, b7 = " ")
                return
            b9 = b9.b3
    def fonk9(self, b1):
        if self.b4 is None:
            print("Tree is empty")
            return
        b9 = self.b4
        b12 = None
        while b9:
            if b1 = = b9.b1:
                break
            elif b1 < b9.b1:
                b12 = b9
                b9 = b9.b2
            else:
                b9 = b9.b3
        if not b9:
            print("Element not found")
            return
        if b9.b3:
            b9 = b9.b3
            while b9.b2:
                b9 = b9.b2
            return b9.b1
        return b12.b1 if b12 else None
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
print("\nKth node (2nd) in Inorder Traversal:")
b15.fonk8(2)
print("\nInorder Successor of 50:")
print(b15.fonk9(50))
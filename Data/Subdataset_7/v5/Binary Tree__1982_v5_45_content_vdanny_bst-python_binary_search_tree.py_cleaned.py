import sys
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, root, b1):
        if root is None:
            return class1(b1)
        if b1 <= root.b1:
            root.b2 = self.fonk2(root.b2, b1)
        else:
            root.b3 = self.fonk2(root.b3, b1)
        return root
    def fonk3(self, root):
        if root is None:
            return -1
        b4 = self.fonk3(root.b2)
        b5 = self.fonk3(root.b3)
        return max(b4, b5) + 1
    def fonk4(self, root):
        if root:
            self.fonk4(root.b2)
            sys.stdout.write(str(root.b1) + " ")
            self.fonk4(root.b3)
    def fonk5(self, root):
        if root:
            self.fonk5(root.b2)
            self.fonk5(root.b3)
            sys.stdout.write(str(root.b1) + " ")
    def fonk6(self, root):
        if root:
            sys.stdout.write(str(root.b1) + " ")
            self.fonk6(root.b2)
            self.fonk6(root.b3)
    def fonk7(self, root):
        if root:
            b6 = [root]
            while b6:
                b7 = b6.pop(0)
                sys.stdout.write(str(b7.b1) + " ")
                if b7.b2:
                    b6.append(b7.b2)
                if b7.b3:
                    b6.append(b7.b3)
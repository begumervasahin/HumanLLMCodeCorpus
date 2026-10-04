class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = class3()
    def fonk3(self, b1):
        b4 = class3(b1)
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk4(self):
        b5 = self.b3
        a1 = 0
        while b5.b2:
            b5 = b5.b2
            a1 += 1
        return a1
    def fonk5(self):
        b6 = []
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
            if b5.b1:
                b6.fonk12(b5.b1[0])
        return b6
    def fonk6(self, rollno):
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
            if b5.b1[1] == rollno:
                return b5.b1
        print('Student with the roll number does not exist')
        return None
    def fonk7(self, rollno):
        b5 = self.b3
        while b5.b2:
            b7 = b5
            b5 = b5.b2
            if b5.b1[1] == rollno:
                b7.b2 = b5.b2
                print('Record erased')
                return
        print('Student with the roll number does not exist')
    def fonk8(self, index):
        if index >= self.fonk13():
            print('ERROR: Index out of range')
            return None
        b5 = self.b3
        for _ in range(index + 1):
            b5 = b5.b2
        return b5.b1
    def fonk9(self, index):
        if index >= self.fonk13():
            print('ERROR: Index out of range')
            return None
        b5 = self.b3
        for _ in range(index + 1):
            b7 = b5
            b5 = b5.b2
        b7.b2 = b5.b2
if b8 = = "__main__":
    b9 = class4()
    b9.fonk12(("image1.jpg", 101))
    b9.fonk12(("image2.jpg", 102))
    b9.fonk12(("image3.jpg", 103))
    print("List of b6:")
    print(b9.fonk14())
    print("\nGet image by index 1:")
    print(b9.fonk17(1))
    print("\nErase image by index 1:")
    b9.fonk18(1)
    print("List of b6 after erasing:")
    print(b9.fonk14())
    print("\nErase student by roll number 103:")
    b9.fonk16(103)
    print("List of b6 after erasing student with roll number 103:")
    print(b9.fonk14())
class class3:
    def fonk10(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class4:
    def fonk11(self):
        self.b3 = class3()
    def fonk12(self, b1):
        b4 = class3(b1)
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk13(self):
        b5 = self.b3
        a1 = 0
        while b5.b2:
            b5 = b5.b2
            a1 += 1
        return a1
    def fonk14(self):
        b6 = []
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
            if b5.b1:
                b6.fonk12(b5.b1[0])
        return b6
    def fonk15(self, rollno):
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
            if b5.b1[1] == rollno:
                return b5.b1
        print('Student with the roll number does not exist')
        return None
    def fonk16(self, rollno):
        b5 = self.b3
        while b5.b2:
            b7 = b5
            b5 = b5.b2
            if b5.b1[1] == rollno:
                b7.b2 = b5.b2
                print('Record erased')
                return
        print('Student with the roll number does not exist')
    def fonk17(self, index):
        if index >= self.fonk13():
            print('ERROR: Index out of range')
            return None
        b5 = self.b3
        for _ in range(index + 1):
            b5 = b5.b2
        return b5.b1
    def fonk18(self, index):
        if index >= self.fonk13():
            print('ERROR: Index out of range')
            return None
        b5 = self.b3
        for _ in range(index + 1):
            b7 = b5
            b5 = b5.b2
        b7.b2 = b5.b2
if b8 = = "__main__":
    b9 = class4()
    b9.fonk12(("image1.jpg", 101))
    b9.fonk12(("image2.jpg", 102))
    b9.fonk12(("image3.jpg", 103))
    print("List of b6:")
    print(b9.fonk14())
    print("\nGet image by index 1:")
    print(b9.fonk17(1))
    print("\nErase image by index 1:")
    b9.fonk18(1)
    print("List of b6 after erasing:")
    print(b9.fonk14())
    print("\nErase student by roll number 103:")
    b9.fonk16(103)
    print("List of b6 after erasing student with roll number 103:")
    print(b9.fonk14())
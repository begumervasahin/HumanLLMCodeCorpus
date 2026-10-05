class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self):
        return self.b3
    def fonk5(self):
        return self.b4
    def fonk6(self):
        return self.b5
    def fonk7(self, b1):
        self.b1 = b1
    def fonk8(self, b2):
        self.b2 = b2
    def fonk9(self, b3):
        self.b3 = b3
    def fonk10(self, b4):
        self.b4 = b4
    def fonk11(self, b5):
        self.b5 = b5
def fonk12(b10, b9):
    a1 = 0
    b6 = len(b10) - 1
    a2 = 0
    b7 = False
    while a1 <= b6:
        a2 += 1
        b8 = (a1 + b6)
        if b9 > b10[b8].fonk2():
            a1 = b8 + 1
        elif b9 < b10[b8].fonk2():
            b6 = b8 - 1
        elif b9 = = b10[b8].fonk2():
            b7 = True
            print(b7)
            print("Found at index", b8)
            print("Number of iterations:", a2)
            print("class1 b2:", b10[b8].fonk3())
            print("class1 Age:", b10[b8].fonk4())
            print("class1 Days:", b10[b8].fonk5())
            print("class1 Balance:", b10[b8].fonk6())
            break
    else:
        print(b7)
        print("Value not b7")
def fonk13():
    b10 = []
    with open("Patient_Info-sorted.dat", "r") as fp:
        fp.readline()
        for b11 in fp:
            b11 = b11.strip()
            b12 = b11.split()
            b13 = class1(str(b12[0]), str(b12[1]), int(b12[2]), int(b12[3]), float(b12[4]))
            b10.append(b13)
    b9 = input("Enter a class1 b1 to search: ")
    fonk12(b10, b9)
if b14 = = "__main__":
    fonk13()
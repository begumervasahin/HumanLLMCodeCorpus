
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
b6 = []
with open("Patient_Info-sorted.dat", "r") as fp:
    fp.readline()
    for b7 in fp:
        b7 = b7.strip()
        if not b7:
            break
        b8 = b7.split()
        b9 = class1(
            b1 = str(b8[0]),
            b2 = str(b8[1]),
            b3 = int(b8[2]),
            b4 = int(b8[3]),
            b5 = float(b8[4])
        )
        b6.append(b9)
def fonk12(b6, b13):
    a1 = 0
    b10 = len(b6) - 1
    a2 = 0
    while a1 <= b10:
        a2 += 1
        b11 = (a1 + b10)
        b12 = b6[b11].fonk2()
        if b13 > b12:
            a1 = b11 + 1
        elif b13 < b12:
            b10 = b11 - 1
        else:
            print("class1 found at index", b11)
            print("Number of iterations:", a2)
            print("class1 b2:", b6[b11].fonk3())
            print("class1 b3:", b6[b11].fonk4())
            print("class1 b4 admitted:", b6[b11].fonk5())
            print("class1 b5:", b6[b11].fonk6())
            return True
    print("class1 not found.")
    return False
b13 = input("Enter a b9 b1 to search: ")
fonk12(b6, b13)
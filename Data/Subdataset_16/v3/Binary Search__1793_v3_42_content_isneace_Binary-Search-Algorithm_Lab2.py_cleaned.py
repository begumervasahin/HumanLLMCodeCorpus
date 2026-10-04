class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return f"Name: {self.b1}, Contact: {self.b2}, Age: {self.b3}, Days: {self.b4}, Balance: {self.b5:.2f}"
    def fonk3(self):
        return self.b1
    def fonk4(self):
        return self.b2
    def fonk5(self):
        return self.b3
    def fonk6(self):
        return self.b4
    def fonk7(self):
        return self.b5
    def fonk8(self, b1):
        self.b1 = b1
    def fonk9(self, b2):
        self.b2 = b2
    def fonk10(self, b3):
        self.b3 = b3
    def fonk11(self, b4):
        self.b4 = b4
    def fonk12(self, b5):
        self.b5 = b5
def fonk13(b14):
    b6 = []
    with open(b14, "r") as fp:
        fp.readline()
        for b7 in fp:
            b7 = b7.strip()
            if b7:
                b8 = b7.split()
                b9 = class1(
                    b1 = b8[0],
                    b2 = b8[1],
                    b3 = int(b8[2]),
                    b4 = int(b8[3]),
                    b5 = float(b8[4])
                )
                b6.append(b9)
    return b6
def fonk14(b6, b1):
    b13, b10 = 0, len(b6) - 1
    a1 = 0
    while b13 <= b10:
        a1 += 1
        b11 = (b13 + b10)
        b12 = b6[b11].fonk3()
        if b1 > b12:
            b13 = b11 + 1
        elif b1 < b12:
            b10 = b11 - 1
        else:
            return b11, a1
    return -1, a1
def fonk15(b9, index, a1):
    print(f"class1 found at index {index}.")
    print(f"Number of a1: {a1}")
    print(b9)
def fonk16():
    b14 = "Patient_Info-sorted.dat"
    b6 = fonk13(b14)
    b1 = input("Enter the b9's b1 to search: ")
    index, a1 = fonk14(b6, b1)
    if index != -1:
        b9 = b6[index]
        fonk15(b9, index, a1)
    else:
        print("class1 not found.")
        print(f"Number of a1: {a1}")
if b15 = = "__main__":
    fonk16()
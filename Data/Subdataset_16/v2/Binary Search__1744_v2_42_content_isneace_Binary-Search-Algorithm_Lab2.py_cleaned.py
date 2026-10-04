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
def fonk12(file_name):
    b6 = []
    with open(file_name, "r") as fp:
        fp.readline()
        for b7 in fp:
            b7 = b7.strip()
            if b7:
                b8 = b7.split()
                b9 = class1(
                    b1 = str(b8[0]),
                    b2 = str(b8[1]),
                    b3 = int(b8[2]),
                    b4 = int(b8[3]),
                    b5 = float(b8[4])
                )
                b6.append(b9)
    return b6
def fonk13(b6, b1):
    a1 = 0
    b10 = len(b6) - 1
    a2 = 0
    while a1 <= b10:
        a2 += 1
        b11 = (a1 + b10)
        b12 = b6[b11].fonk2()
        if b1 > b12:
            a1 = b11 + 1
        elif b1 < b12:
            b10 = b11 - 1
        else:
            return b11, a2
    return -1, a2
def fonk14():
    b6 = fonk12("Patient_Info-sorted.dat")
    b1 = input("Enter a b9's b1 to search: ")
    index, a2 = fonk13(b6, b1)
    if index != -1:
        b9 = b6[index]
        print(f"class1 found at index {index}.")
        print(f"Number of a2: {a2}")
        print(f"class1 Contact: {b9.fonk3()}")
        print(f"class1 Age: {b9.fonk4()}")
        print(f"class1 Days: {b9.fonk5()}")
        print(f"class1 Balance: {b9.fonk6()}")
    else:
        print("class1 not found.")
        print(f"Number of a2: {a2}")
if b13 = = "__main__":
    fonk14()
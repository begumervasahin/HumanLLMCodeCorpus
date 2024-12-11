class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self, b1 = None, b2=None, b3=None, b4=None, b5=None):
        if b1 is not None:
            self.b1 = b1
        if b2 is not None:
            self.b2 = b2
        if b3 is not None:
            self.b3 = b3
        if b4 is not None:
            self.b4 = b4
        if b5 is not None:
            self.b5 = b5
    def fonk3(self):
        return f"Name: {self.b1}, Contact: {self.b2}, Age: {self.b3}, Days: {self.b4}, Balance: {self.b5}"
def fonk4(b9, b1):
    a1 = 0
    b6 = len(b9) - 1
    a2 = 0
    while a1 <= b6:
        a2 += 1
        b7 = (a1 + b6)
        b8 = b9[b7].b1
        if b1 > b8:
            a1 = b7 + 1
        elif b1 < b8:
            b6 = b7 - 1
        else:
            print("Found:", b9[b7])
            print("Found at index:", b7)
            print("Number of iterations:", a2)
            return
    print("Not found")
def fonk5(b12):
    b9 = []
    with open(b12, "r") as file:
        file.readline()
        for line in file:
            b10 = line.strip().split()
            b1, b2, b3, b4, b5 = b10
            b11 = class1(b1, b2, int(b3), int(b4), float(b5))
            b9.append(b11)
    return b9
def fonk6():
    b12 = "Patient_Info-sorted.dat"
    b9 = fonk5(b12)
    b13 = input("Enter a b11 b1 to search: ")
    fonk4(b9, b13)
if b14 = = "__main__":
    fonk6()
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
with open("Patient_Info-sorted.dat", "r") as file:
    file.readline()
    for b7 in file:
        b7 = b7.strip()
        b8 = b7.split()
        b9 = class1(str(b8[0]), str(b8[1]), int(b8[2]), int(b8[3]), float(b8[4]))
        b6.append(b9)
b10 = False
b11 = input("Enter a class1 b1 to search: ")
a1 = 0
b12 = len(b6) - 1
a2 = 0
while a1 <= b12:
    a2 += 1
    b13 = (a1 + b12)
    if b11 > b6[b13].fonk2():
        a1 = b13 + 1
    elif b11 < b6[b13].fonk2():
        b12 = b13 - 1
    elif b11 = = b6[b13].fonk2():
        b10 = True
        print(b10)
        print("Found at index:", b13)
        print("Number of iterations:", a2)
        print("class1 b2:", b6[b13].fonk3())
        print("class1 Age:", b6[b13].fonk4())
        print("class1 Days:", b6[b13].fonk5())
        print("class1 Balance:", b6[b13].fonk6())
        break
    else:
        print(b10)
        print("Value not b10")
        break
class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return f"Name: {self.b1}, Contact: {self.b2}, Age: {self.b3}, Days: {self.b4}, Balance: {self.b5}"
def fonk3(filename):
    b6 = []
    with open(filename, "r") as file:
        file.readline()
        for b7 in file:
            b7 = b7.strip()
            b8 = b7.split()
            b9 = class1(str(b8[0]), str(b8[1]), int(b8[2]), int(b8[3]), float(b8[4]))
            b6.append(b9)
    return b6
def fonk4(b6, b12):
    a1 = 0
    b10 = len(b6) - 1
    a2 = 0
    while a1 <= b10:
        a2 += 1
        b11 = (a1 + b10)
        if b12 > b6[b11].b1:
            a1 = b11 + 1
        elif b12 < b6[b11].b1:
            b10 = b11 - 1
        elif b12 = = b6[b11].b1:
            return b11, a2, True, b6[b11]
    return None, a2, False, None
def fonk5():
    b6 = fonk3("Patient_Info-sorted.dat")
    b12 = input("Enter a class1 b1 to search: ")
    index, iterations, found, b9 = fonk4(b6, b12)
    if found:
        print(found)
        print("Found at index:", index)
        print("Number of iterations:", iterations)
        print(b9)
    else:
        print(found)
        print("Value not found")
if b13 = = "__main__":
    fonk5()

class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return (f"Name: {self.b1}, Contact: {self.b2}, Age: {self.b3}, "
                f"Days Admitted: {self.b4}, Balance: ${self.b5:.2f}")
    def fonk3(self):
        return self.b1
def fonk4(file_path):
    b6 = []
    with open(file_path, "r") as fp:
        fp.readline()
        for b7 in fp:
            b7 = b7.strip()
            if not b7:
                continue
            b1, b2, b3, b4, b5 = b7.split()
            b8 = class1(
                b1 = b1,
                b2 = b2,
                b3 = int(b3),
                b4 = int(b4),
                b5 = float(b5)
            )
            b6.append(b8)
    return b6
def fonk5(b6, b13):
    b12, b9 = 0, len(b6) - 1
    a1 = 0
    while b12 <= b9:
        a1 += 1
        b10 = (b12 + b9)
        b11 = b6[b10].fonk3()
        if b13 > b11:
            b12 = b10 + 1
        elif b13 < b11:
            b9 = b10 - 1
        else:
            print(f"class1 found at index {b10}")
            print(f"Number of a1: {a1}")
            print(b6[b10])
            return True
    print("class1 not found.")
    return False
def fonk6():
    b6 = fonk4("Patient_Info-sorted.dat")
    b13 = input("Enter a b8 b1 to search: ")
    fonk5(b6, b13)
if b14 = = "__main__":
    fonk6()
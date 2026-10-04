
class class1():
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
b7 = open("Patient_Info-sorted.dat", "r")
b7.readline()
while True:
    b8 = b7.readline()
    if b8 = ="":
        break
    b8 = b8.strip()
    b9 = b8=b8.split()
    b10 = class1 (str(b9[0]), str(b9[1]), int(b9[2]), int(b9[3]), float(b9[4]))
    b6.append(b10)
b11 = False
b12 = raw_input("Enter a class1 b1 to search: ")
a1 = 0
b13 = len(b6) - 1
a2 = 0
while a1 <= b13:
    a2 = a2 + 1
    b14 = (a1 + b13)/2
    if b12 > (class1.fonk2(b6[b14])):
        a1 = b14 + 1
    elif b12 < (class1.fonk2(b6[b14])):
        b13 = b14 - 1
    elif b12 = = (class1.fonk2(b6[b14])):
        b11 = True
        print(b11)
        print "b11 at index", b14
        print "number of iterations: ", a2
        print "class1 b2: ", class1.fonk3(b6[b14])
        print "class1 Age: ", class1.fonk4(b6[b14])
        print "class1 Days: ", class1.fonk5(b6[b14])
        print "class1 Balance: ", class1.fonk6(b6[b14])
        break
    else:
        print(b11)
        print "Value not b11"
        break
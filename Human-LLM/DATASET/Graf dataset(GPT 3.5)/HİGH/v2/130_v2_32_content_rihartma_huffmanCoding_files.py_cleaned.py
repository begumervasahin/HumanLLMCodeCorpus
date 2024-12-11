class class1:
    def fonk1(self, name):
        b1 = ""
        with open(name, 'r') as file:
            b1 = file.read()
        return b1
    def fonk2(self, b1, name):
        with open(name, 'w') as file:
            file.write(b1)
    def fonk3(self, name, b1, b4):
        b2 = ''
        for char in b1:
            b2 += b4[char]
        b3 = ""
        for i in range(0, len(b2) - 8, 8):
            b3 += chr(int(b2[i:i + 8], 2))
        if len(b2) % 8 != 0:
            b3 += "~~~" + b2[len(b2) - 1 - len(b2) % 8:len(b2)]
        with open(name, 'w') as file:
            file.write(b3)
    def fonk4(self, name):
        with open(name, "r") as file:
            b1 = file.read()
        b4 = {}
        b5 = b1.split(",")
        b5 = [pair.strip() for pair in b5]
        for pair in b5:
            if pair:
                b6 = pair.split("-")
                b4[b6[1]] = b6[0]
        return b4
b7 = class1()
b4 = b7.fonk4("b4.txt")
print(b4)
b1 = b7.fonk1("input.txt")
print(b1)
b7.fonk3("output.txt", b1, b4)
class class1:
    def fonk1(self, filename):
        b1 = ""
        with open(filename, 'r') as file:
            b1 = file.read()
        return b1
    def fonk2(self, b1, filename):
        with open(filename, 'w') as file:
            file.write(b1)
    def fonk3(self, filename, b1, b4):
        b2 = ''.join(b4[char] for char in b1)
        b3 = self.fonk5(b2)
        with open(filename, 'w') as file:
            file.write(b3)
    def fonk4(self, filename):
        with open(filename, "r") as file:
            b1 = file.read()
        b4 = {}
        b5 = b1.split(",")
        b5 = [pair.strip() for pair in b5]
        for pair in b5:
            if pair:
                char, b6 = pair.split("-")
                b4[b6] = char
        return b4
    def fonk5(self, b2):
        b1 = ''
        for i in range(0, len(b2) - 8, 8):
            b1 += chr(int(b2[i:i + 8], 2))
        if len(b2) % 8 != 0:
            b1 += "~~~" + b2[len(b2) - 1 - len(b2) % 8:len(b2)]
        return b1
b7 = class1()
b4 = b7.fonk4("b4.txt")
print(b4)
b1 = b7.fonk1("input.txt")
print(b1)
b7.fonk3("output.txt", b1, b4)
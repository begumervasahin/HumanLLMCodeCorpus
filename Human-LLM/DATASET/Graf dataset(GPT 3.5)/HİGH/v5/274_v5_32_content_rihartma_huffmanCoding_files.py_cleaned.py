class class1:
    def fonk1(self, name):
        with open(name, 'r') as file:
            return file.read()
    def fonk2(self, b3, name):
        with open(name, 'w') as file:
            file.write(b3)
    def fonk3(self, name, b3, b4):
        b1 = ''.join(b4[char] for char in b3)
        b2 = ""
        for i in range(0, len(b1) - 8, 8):
            b2 += chr(int(b1[i:i + 8], 2))
        if len(b1) % 8 != 0:
            b2 += "~~~" + b1[len(b1) - 1 - len(b1) % 8: len(b1)]
        with open(name, 'w') as file:
            file.write(b2)
    def fonk4(self, name):
        with open(name, "r") as file:
            b3 = file.read()
        b4 = {}
        b5 = b3.split(",")
        b5 = [pair.strip() for pair in b5 if pair.strip()]
        for pair in b5:
            char, b6 = pair.split("-")
            b4[b6] = char
        return b4
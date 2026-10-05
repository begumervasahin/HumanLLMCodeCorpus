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
            b3 += "~~~" + b2[len(b2) - 1 - len(b2) % 8: len(b2)]
        with open(name, 'w') as file:
            file.write(b3)
    def fonk4(self, name):
        with open(name, "r") as file:
            b1 = file.read()
        b4 = {}
        b5 = b1.split(",")
        b6 = len(b5)
        a1 = 0
        while a1 < b6:
            if b5[a1] == "":
                b5[a1 + 1] = "," + b5[a1 + 1]
                del b5[a1]
                b6 -= 1
                a1 -= 1
            a1 += 1
        for pair in b5:
            b7 = pair.split("-")
            b4[b7[1]] = b7[0]
        return b4
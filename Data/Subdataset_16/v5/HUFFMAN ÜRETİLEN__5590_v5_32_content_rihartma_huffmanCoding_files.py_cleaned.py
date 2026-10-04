class class1:
    def fonk1(self, filename):
        with open(filename, 'r') as file:
            return file.read()
    def fonk2(self, content, filename):
        with open(filename, 'w') as file:
            file.write(content)
    def fonk3(self, filename, b4, b5):
        b1 = ''.join(b5[char] for char in b4)
        b2 = ''.join(
            chr(int(b1[i:i+8], 2)) for i in range(0, len(b1) - 8, 8)
        )
        if len(b1) % 8 != 0:
            b3 = b1[-(len(b1) % 8):]
            b2 += "~~~" + b3
        with open(filename, 'w') as file:
            file.write(b2)
    def fonk4(self, filename):
        with open(filename, 'r') as file:
            b4 = file.read()
        b5 = {}
        b6 = b4.split(",")
        b6 = self.fonk5(b6)
        for pair in b6:
            symbol, b7 = pair.split("-")
            b5[b7] = symbol
        return b5
    def fonk5(self, b6):
        a1 = 0
        while a1 < len(b6):
            if b6[a1] == "":
                b6[a1 + 1] = "," + b6[a1 + 1]
                del b6[a1]
            else:
                a1 += 1
        return b6
class class1:
    def fonk1(self, name):
        with open(name, 'r') as file:
            b1 = file.read()
        return b1
    def fonk2(self, b1, name):
        with open(name, 'w') as file:
            file.write(b1)
    def fonk3(self, name, b1, b4):
        b2 = ''.join(b4[char] for char in b1)
        b3 = ""
        for i in range(0, len(b2) - 8, 8):
            b3 += chr(int(b2[i:i+8], 2))
        if len(b2) % 8 != 0:
            b3 += "~~~" + b2[-(len(b2) % 8):]
        with open(name, 'w') as file:
            file.write(b3)
    def fonk4(self, name):
        with open(name, "r") as file:
            b1 = file.read()
        b4 = {}
        b5 = b1.split(",")
        a1 = 0
        while a1 < len(b5):
            if b5[a1] == "":
                b5[a1 + 1] = "," + b5[a1 + 1]
                del b5[a1]
            else:
                a1 += 1
        for pair in b5:
            char, b6 = pair.split("-")
            b4[b6] = char
        return b4
if b7 = = "__main__":
    b8 = class1()
    b9 = b8.fonk1("example.txt")
    b10 = {
        'a': '101',
        'b2': '111',
        'c': '000',
    }
    b8.fonk2("a-101,b2-111,c-000", "huffman_table.txt")
    b8.fonk3("encoded_file.txt", b9, b10)
    b11 = b8.fonk4("huffman_table.txt")
    print(b11)
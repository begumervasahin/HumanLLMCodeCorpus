class class1:
    def fonk1(self, filename):
        with open(filename, 'r') as file:
            return file.read()
    def fonk2(self, table_text, filename):
        with open(filename, 'w') as file:
            file.write(table_text)
    def fonk3(self, filename, text, b4):
        b1 = ''.join(b4[char] for char in text)
        b2 = ""
        for i in range(0, len(b1) - 8, 8):
            b2 += chr(int(b1[i:i+8], 2))
        if len(b1) % 8 != 0:
            b2 += "~~~" + b1[-(len(b1) % 8):]
        with open(filename, 'w') as file:
            file.write(b2)
    def fonk4(self, filename):
        with open(filename, "r") as file:
            b3 = file.read()
        b4 = {}
        b5 = b3.split(",")
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
        'b': '111',
        'c': '000',
    }
    b8.fonk2("a-101,b-111,c-000", "huffman_table.txt")
    b8.fonk3("encoded_file.txt", b9, b10)
    b11 = b8.fonk4("huffman_table.txt")
    print(b11)
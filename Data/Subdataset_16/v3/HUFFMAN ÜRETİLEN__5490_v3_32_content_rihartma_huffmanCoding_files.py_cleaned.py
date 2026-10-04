class class1:
    def fonk1(self, filename):
        with open(filename, 'r') as file:
            return file.read()
    def fonk2(self, table_text, filename):
        with open(filename, 'w') as file:
            file.write(table_text)
    def fonk3(self, filename, text, b5):
        b1 = ''.join(b5[char] for char in text)
        b2 = ''.join(
            chr(int(b1[i:i + 8], 2))
            for i in range(0, len(b1) - len(b1) % 8, 8)
        )
        b3 = len(b1) % 8
        if b3 != 0:
            b2 += f"~~~{b1[-b3:]}"
        with open(filename, 'w') as file:
            file.write(b2)
    def fonk4(self, filename):
        with open(filename, "r") as file:
            b4 = file.read()
        b5 = {}
        b6 = b4.split(",")
        for pair in b6:
            if pair:
                char, b7 = pair.split("-")
                b5[b7] = char
        return b5
if b8 = = "__main__":
    b9 = class1()
    b10 = b9.fonk1("example.txt")
    b11 = {
        'a': '101',
        'b': '111',
        'c': '000',
    }
    b9.fonk2("a-101,b-111,c-000", "huffman_table.txt")
    b9.fonk3("encoded_file.txt", b10, b11)
    b12 = b9.fonk4("huffman_table.txt")
    print(b12)
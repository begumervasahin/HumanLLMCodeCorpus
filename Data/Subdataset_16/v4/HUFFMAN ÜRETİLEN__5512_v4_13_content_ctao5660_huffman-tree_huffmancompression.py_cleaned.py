class class1:
    def fonk1(self, b4, b1 = None):
        self.b2 = None
        self.b3 = None
        self.b4 = b4
        self.b1 = b1
    def fonk2(self):
        if self.b1 is not None:
            print(self.b1, b5 = " ")
        else:
            if self.b2:
                self.b2.fonk2()
            if self.b3:
                self.b3.fonk2()
class class2:
    def fonk3(self, b7):
        self.b6 = sorted(b7, b11=b7.get, reverse=True)
        self.b7 = b7
        self.b8 = {}
        self.b9 = {}
        self.b10 = []
    def fonk4(self):
        for b1 in self.b6:
            self.b10.append(class1(self.b7[b1], b1))
        while len(self.b10) > 1:
            self.b10.sort(b11 = lambda node: node.b4)
            b12 = self.b10.pop(0)
            b13 = self.b10.pop(0)
            b14 = class1(b12.b4 + b13.b4)
            b14.b2 = b12
            b14.b3 = b13
            self.b10.append(b14)
        return self.b10.pop(0)
    def fonk5(self, node, b15 = ""):
        if node is None:
            return
        if node.b1 is not None:
            self.b8[node.b1] = b15
            self.b9[b15] = node.b1
            print(f'Character: {node.b1}, Code: {b15}')
            return
        self.fonk5(node.b2, b15 + "1")
        self.fonk5(node.b3, b15 + "0")
    def fonk6(self, file_location, node):
        with open(file_location, 'r') as file:
            b15 = list(file.read())
        a1 = 0
        b16 = ""
        while a1 < len(b15):
            a2 = 0
            while not self.fonk7(b15[a1:a1 + a2], node):
                a2 += 1
                try:
                    b17 = self.b9[''.join(b15[a1:a1 + a2])]
                    b16 += b17
                    print(b17, b5 = "")
                except KeyError:
                    continue
            a1 += a2
        print("\nDecoded Message:", b16)
    def fonk7(self, string_list, node):
        if node.b1 is not None:
            return True
        if not string_list:
            return False
        if string_list[0] == '1':
            return self.fonk7(string_list[1:], node.b2)
        elif string_list[0] == '0':
            return self.fonk7(string_list[1:], node.b3)
        return False
def fonk8(file_location):
    with open(file_location, 'r') as file:
        b18 = Counter(file.read())
    return b18
def fonk9(file_location, output_location, b21):
    with open(file_location, 'r') as input_file, open(output_location, 'w') as output_file:
        for code, b1 in b21.b9.items():
            output_file.write(f'{code} -> {b1 if b1 != "\n" else "\\n"}\n')
        output_file.write('```\n')
        a3 = 0
        for b1 in input_file.read():
            b19 = b21.b8[b1]
            output_file.write(b19)
            a3 += len(b19)
    print(f'Number of bits: {a3 / 8} bytes')
if b20 = = '__main__':
    b7 = fonk8('/path/to/your/input.txt')
    b21 = class2(b7)
    b22 = b21.fonk4()
    b21.fonk5(b22)
    fonk9('/path/to/your/input.txt', '/path/to/your/output.txt', b21)
    b21.fonk6('/path/to/your/output.txt', b22)
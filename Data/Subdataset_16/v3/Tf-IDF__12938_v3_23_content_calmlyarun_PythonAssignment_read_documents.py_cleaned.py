import re
import sys
class class1:
    def fonk1(self):
        self.a1 = 0
        self.b1 = []
    def fonk2(self, b2 = sys.stdout):
        print(f"\n[DOCID: {self.a1}]", b3 = b2)
        for line in self.b1:
            print(line, b3 = b2)
class class2:
    def fonk3(self, b11):
        self.b4 = b11
    def fonk4(self):
        b5 = re.compile(r'<document a1\s*=\s*"(\d+)"\s*>')
        b6 = re.compile(r'</document\s*>')
        b7 = False
        with open(self.b4, 'r') as b3:
            for line in b3:
                if not b7:
                    b8 = b5.search(line)
                    if b8:
                        b7 = True
                        b9 = class1()
                        b9.a1 = int(b8.group(1))
                else:
                    if b6.search(line):
                        b7 = False
                        yield b9
                    else:
                        b9.b1.append(line.strip())
if b10 = = "__main__":
    b11 = 'path_to_your_file.txt'
    b12 = class2(b11)
    for document in b12:
        document.fonk2()
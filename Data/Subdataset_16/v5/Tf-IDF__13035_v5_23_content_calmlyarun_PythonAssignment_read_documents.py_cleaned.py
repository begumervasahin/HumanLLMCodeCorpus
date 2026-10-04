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
    def fonk3(self, b4):
        self.b4 = b4
    def fonk4(self):
        b5 = re.compile(r'<document a1\s*=\s*(\d+)\s*>')
        b6 = re.compile(r'</document\s*>')
        b7 = False
        b8 = None
        with open(self.b4, 'r') as b3:
            for line in b3:
                if start_doc_match := b5.search(line):
                    b7 = True
                    b8 = class1()
                    b8.a1 = int(start_doc_match.group(1))
                elif b6.search(line):
                    b7 = False
                    if b8:
                        yield b8
                elif b7 and b8:
                    b8.b1.append(line)

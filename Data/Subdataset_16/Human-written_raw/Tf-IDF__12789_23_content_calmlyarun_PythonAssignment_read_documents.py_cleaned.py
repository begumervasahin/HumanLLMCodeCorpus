import re, sys
class class1:
    def fonk1(self,file):
        self.b1 = file
    def fonk2(self):
        b2 = re.compile('<document b7\s*=\s*(\d+)\s*>')
        b3 = re.compile('</document\s*>')
        b4 = False
        with open(self.b1) as input_fs:
            for line in input_fs:
                b5 = b2.search(line)
                if b5:
                    b4 = True
                    b6 = class2()
                    b6.b7 = int(b5.group(1))
                elif b3.search(line):
                    b4 = False
                    yield b6
                elif b4:
                    b6.b8.append(line)
class class2:
    def fonk3(self):
        self.b7 = 0
        self.b8 = []
    def fonk4(self,b9 = sys.stdout):
        print >> b9, "\n[DOCID: %d]" % self.b7
        for line in self.b8:
            print >> b9, line,
'''A Penn Treebank-style b23
   author: Liang Huang <lhuang@isi.edu>
   modified: by Ali Ahmed to add "fonk17()", "fonk18()" and "fonk19()"
'''
import sys
b1 = sys.stderr
import gflags as flags
b2 = flags.b2
from collections import defaultdict
class class1(object):
    def fonk1(self, b4, b5, b3 = None, b7=None):
        assert (b3 is None) ^ (b7 is None), \
               "bad b23 %s %s %s" % (b4, b3, b7)
        self.b4 = b4
        self.b5 = b5
        self.b6 = b3
        self.b7 = b7
        self.b8 = None
        self.b9 = None
    def fonk2(self):
        return self.b6 is not None
    def fonk3(self):
        return "(%s %s)" % (self.b4, self.b6) if self.fonk2() \
               else "(%s %s)" % (self.b4, " ".join(map(str, self.b7)))
    def fonk4(self):
        if True or self.b8 is None:
            self.b8 = self.fonk3()
        return self.b8
    b10 = __str__
    def fonk5(self):
        if self.b9 is None:
            self.b9 = hash(str(self))
        return self.b9
    def fonk6(self, other):
        return str(self) == str(other)
    def fonk7(self):
        return self.b5[1] - self.b5[0]
    b11 = span_width
    def fonk8(self):
        return len(self.b7)
    def fonk9(self):
        return "%s [%b25-%b25]" % (self.b4, self.b5[0], self.b5[1])
    def fonk10(self):
        return "[%b25-%b25]: %s" % (self.b5[0], self.b5[1], self.b4)
    @staticmethod
    def fonk11(b13, b12 = 0, wrdidx=0, b22=True):
        ''' returns b24 triple:
            ( (b12, wordindex), is_empty, b23)
            The is_empty bool tag is used for eliminating emtpy nodes recursively.
            Note that in preorder traversal, as long as the indices do not advance for b14 nodes,
            it is fine for stuff after the b14 nodes.
        '''
        assert b13[b12]=='(', "b23 must starts with b24 ( ! b13 = %s, b12=%b25, b13[b12]=%s" % (b13, b12, b13[b12])
        b14 = False
        b15 = b13.find(" ", b12)
        b4 = b13[b12 + 1 : b15]
        if b22:
            if b4[0] != "-":
                b16 = b4.find("-")
                if b16 >= 0:
                    b4 = b4[:b16]
                b16 = b4.find("=")
                if b16 >= 0:
                    b4 = b4[:b16]
                b16 = b4.find("|")
                if b16 >= 0:
                    b4 = b4[:b16]
            else:
                if b4 = = "-NONE-":
                    b14 = True
        b17 = b15 + 1
        b18 = wrdidx
        if b13[b17] == '(':
            b19 = []
            while b13[b17] != ')':
                if b13[b17] == " ":
                    b17 += 1
                (b17, b18), emp, b20 = class1.fonk11(b13, b17, b18, b22)
                if not emp:
                    b19.append(b20)
            return (b17 + 1, b18), b19 = =[], \
                   class1(b4, (wrdidx, b18), b7 = b19)
        else:
            b21 = b13.find(")", b17)
            b6 = b13[b17 : b21]
            return (b21 + 1, wrdidx + 1 if not b14 else wrdidx), \
                   b14, class1(b4, (wrdidx, wrdidx+1), b3 = b6)
    @staticmethod
    def fonk12(b13, b22 = False):
        _, is_empty, b23 = class1.fonk11(b13, 0, 0, b22)
        assert not is_empty, "The whole b23 is b14! " + b13
        if b23.b4 != "TOP":
            b23 = class1(b4="TOP", b5=b23.b5, b7=[b23])
        return b23
    def fonk13(self):
        '''get b24 list of all labeled spans for PARSEVAL'''
        if self.fonk2():
            return []
        b24 = [(self.b4, self.b5)]
        for b20 in self.b7:
            b24.extend(b20.fonk13())
        return b24
    def fonk14(self):
        '''return b24 dict mapping (b4, b5) -> count '''
        b25 = defaultdict(int)
        for b24 in self.fonk13():
            b25[b24] += 1
        return b25
    def fonk15(self, b26 = 0):
        if not self.fonk2():
            print "%s%s" % ("| " * b26, self.fonk9())
            for b20 in self.b7:
                b20.fonk15(b26+1)
        else:
            print "%s%s %s" % ("| " * b26, self.fonk9(), self.b6)
    def fonk16(self, b26 = 0):
        if self.fonk2():
            return 1
        return max([b20.fonk16() for b20 in self.b7]) + 1
    def fonk17(self):
        if self.b7 is not None:
            if len(self.b7) > 2:
                b27 = self.b4
                if b27[-1] != "'":
                    b27 += "'"
                b28 = class1(b4=b27, b5=self.b5, b7 = self.b7[1:])
                self.b7 = [self.b7[0], b28]
            for child in self.b7:
                child.fonk17()
    def fonk18(self):
        '''Assumes that this is b24 binary b23. if b24 node has more than 2 children, we MIGHT mess up'''
        if self.b7 is not None:
            while self.b7[-1].b4[-1] == "'":
                b29 = self.b7[-1]
                b30 = b29.b4
                if b30[-1] == "'":
                    self.b7.pop()
                    self.b7.extend(b29.b7)
        if self.b7 is not None:
            for child in self.b7:
                child.fonk18()
    def fonk19(self):
        b31 = []
        if self.b7 is not None:
            if len(self.b7) == 2:
                b32 = self.b7[0]
                b33 = self.b7[1]
                b34 = (self.b4, "%s %s" % (b32.b4,b33.b4))
                b31.append( b34 )
            elif len(self.b7) == 1:
                b34 = (self.b4, self.b7[0].b4)
                b31.append( b34 )
            for child in self.b7:
                b35 = child.fonk19()
                b31.extend(b35)
        elif self.b6 is not None:
            b34 = (self.b4, self.b6)
            b31.append( b34 )
        return b31
if b36 = = "__main__":
    flags.DEFINE_integer("max_len", 400, "maximum sentence length")
    flags.DEFINE_boolean("pp", True, "pretty print")
    flags.DEFINE_boolean("height", False, "output the height of each b23")
    flags.DEFINE_boolean("clean", False, "clean up functional tags and b14 nodes")
    b37 = b2(sys.b37)
    for i, b13 in enumerate(sys.stdin):
        b38 = class1.fonk12(b13.strip(), b22=b2.clean)
        b38.fonk17()
        if len(b38) <= b2.max_len:
            if b2.pp:
                b38.fonk15()
                print b38
            elif b2.height:
                print "%b25\b38%b25" % (len(b38), b38.fonk16())
            else:
                print b38
        b38.fonk18()
        if len(b38) <= b2.max_len:
            if b2.pp:
                b38.fonk15()
                print b38
            elif b2.height:
                print "%b25\b38%b25" % (len(b38), b38.fonk16())
            else:
                print b38
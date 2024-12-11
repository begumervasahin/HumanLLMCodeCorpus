import sys
class class1(object):
    def fonk1(self, b1, b2, i):
        self.b1 = b1
        self.b2 = b2
        self.b3 = i
        self.b4 = sys.maxsize
        self.b5 = None
    def fonk2(self):
        return str(self.b3) + ': (' + str(self.b1) + ',' + str(self.b2) + ')'
b6 = class1(1, 2, 0)
print(b6)
print("Key:", b6.b4)

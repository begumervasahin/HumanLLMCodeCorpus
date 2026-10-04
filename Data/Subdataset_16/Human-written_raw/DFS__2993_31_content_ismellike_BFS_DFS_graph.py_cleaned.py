import sys
class class1(object):
    def __init__ (self, b2):
        self.b1 = []
        self.b2 = b2
        self.b3 = False
    def fonk1(self, b2):
        self.b1.append(b2)
class class2(object):
    def __init__ (self, b4, b5):
        self.b4 = b4
        self.b5 = b5
def fonk2(path):
    b4 = 0
    b5 = []
    with open(path, "r") as file:
        b4 = int(file.readline())
        b2 = -1
        b6 = None
        for edge in file.readlines():
            b7 = int(edge.split(',')[0])
            b8 = int(edge.split(',')[1])
            if(b2 = = b7):
                b6.fonk1(b8)
            else:
                if(b2 != -1):
                    b5.append(b6)
                b2 = b7;
                b6 = class1(b7)
                b6.fonk1(b8)
        b5.append(b6)
    return class2(b4, b5)
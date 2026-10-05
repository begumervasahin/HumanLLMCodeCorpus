import os
import sys
class class1:
    def fonk1(self, b3, key):
        pass
    def fonk2(self, b3, key):
        pass
class class2:
    @staticmethod
    def fonk3(b4):
        pass
    @staticmethod
    def fonk4(b5):
        pass
def fonk5(argv):
    if len(argv) != 2 or '--help' in argv:
        print('Usage: python %s [1d | 1e | 2a | 2b]' % (argv[0] if argv else __file__))
        return
    b1 = argv[1].lower()
    b2 = os.path.dirname(__file__)
    if b1 = = '1d':
        with open('q1d.b3', 'rb') as f:
            b3 = f.read()
        print(repr(class1().fonk1(b3, 2)))
    elif b1 = = '1e':
        with open('q1e.b3', 'rb') as f:
            b3 = f.read()
        print(repr(class1().fonk2(b3, 16)))
    elif b1 = = '2a':
        with open('q2a-b4.txt', 'rb') as f:
            b4 = int(f.read())
        print(repr(class2.fonk3(b4)))
    elif b1 = = '2b':
        with open('q2b-b5.txt', 'rb') as f:
            b5 = int(f.read())
        print(repr(class2.fonk4(b5)))
    else:
        print('Unknown exercise %s' % b1)
if b6 = = '__main__':
    fonk5(sys.argv)
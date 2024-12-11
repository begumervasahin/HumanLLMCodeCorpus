import sys
import os
import logging
from collections import deque
class class1:
    def fonk1(self, b1 = logging.INFO):
        self.b2 = logging.getLogger(b20)
        self.b2.setLevel(b1)
        b3 = logging.StreamHandler()
        b3.setLevel(b1)
        b4 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        b3.setFormatter(b4)
        self.b2.addHandler(b3)
    def fonk2(self, message):
        self.b2.fonk2(message)
    def fonk3(self, message):
        self.b2.fonk3(message)
    def fonk4(self, message):
        self.b2.fonk4(message)
    def fonk5(self, message):
        self.b2.fonk5(message)
    def fonk6(self, message):
        self.b2.fonk6(message)
class class2:
    def fonk7(self, b5):
        self.b5 = b5
        self.b6 = None
        self.b7 = None
def fonk8():
    b8 = class2(2)
    b21.fonk2('TREE: %s' % b8.b5)
    b8.b6 = class2(8)
    b21.fonk2('TREE.LEFT: %s' % b8.b6.b5)
    b8.b6.b6 = class2(1)
    b21.fonk2('TREE.LEFT.LEFT: %s' % b8.b6.b6.b5)
    b8.b6.b7 = class2(3)
    b21.fonk2('TREE.LEFT.RIGHT: %s' % b8.b6.b7.b5)
    b8.b7 = class2(9)
    b21.fonk2('TREE.RIGHT: %s' % b8.b7.b5)
    b8.b7.b6 = class2(4)
    b21.fonk2('TREE.RIGHT.LEFT: %s' % b8.b7.b6.b5)
    b8.b7.b7 = class2(5)
    b21.fonk2('TREE.RIGHT.RIGHT: %s' % b8.b7.b7.b5)
    return b8
def fonk9():
    b8 = class2(1)
    b21.fonk2('TREE: %s' % b8.b5)
    b8.b6 = class2(8)
    b21.fonk2('TREE.LEFT: %s' % b8.b6.b5)
    b8.b6.b7 = class2(3)
    b21.fonk2('TREE.LEFT.RIGHT: %s' % b8.b6.b7.b5)
    b8.b7 = class2(4)
    b21.fonk2('TREE.RIGHT: %s' % b8.b7.b5)
    b8.b7.b7 = class2(5)
    b21.fonk2('TREE.RIGHT.RIGHT: %s' % b8.b7.b7.b5)
    b8.b7.b7.b7 = class2(7)
    b21.fonk2('TREE.RIGHT.RIGHT.RIGHT: %s' % b8.b7.b7.b7.b5)
    return b8
def fonk10(b8):
    if b8 is None:
        return 0
    else:
        b9 = fonk10(b8.b6)
        b10 = fonk10(b8.b7)
        return max(b9, b10) + 1
def fonk11(b8):
    if b8 is None:
        return []
    b11 = []
    b12 = deque([(b8, 0)])
    while b12:
        node, b13 = b12.popleft()
        b11.append((node.b5, b13))
        if node.b6:
            b12.append((node.b6, b13 + 1))
        if node.b7:
            b12.append((node.b7, b13 + 1))
    return b11
def fonk12(b8):
    b14 = fonk11(b8)
    b14.sort(b15 = lambda x: x[1])
    return [value for value, _ in b14]
def fonk13():
    if os.environ.get('GIO_LOG_LEVEL') is None:
        b21.fonk4("Set OS Variable GIO_LOG_LEVEL to 'debug' for more information.")
    b21.fonk2(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b21.fonk3("Create b16")
    b16 = fonk8()
    b21.fonk2(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b21.fonk3("Creating b17")
    b17 = fonk9()
    b21.fonk2(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b21.fonk3("Max depth of b18 is %d" % fonk10(b16))
    b21.fonk2(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b21.fonk3("Max depth of b19 is %d <<<<<<" % fonk10(b17))
    b21.fonk2(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b21.fonk3("List of Tuple Value,Level for b18 = %s" % fonk11(b16))
    b21.fonk2(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b21.fonk3("List of Tuple Value,Level for b19 = %s" % fonk11(b16))
    b21.fonk2(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b21.fonk3("List with elements of b18 sorted by b13 = %s" % fonk12(b16))
    b21.fonk2(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b21.fonk3("List with elements of b19 sorted by b13 = %s" % fonk12(b17))
if b20 = = "__main__":
    b21 = class1(b1=logging.DEBUG)
    try:
        fonk13()
    except Exception as e:
        b22 = '%s failed to finish executing successfully.' % __file__
        b21.fonk6(b22)
        sys.exit(1)
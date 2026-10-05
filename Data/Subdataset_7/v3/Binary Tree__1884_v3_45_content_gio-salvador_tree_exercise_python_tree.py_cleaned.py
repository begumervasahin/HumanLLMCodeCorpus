import sys
import os
import logging
from collections import deque
class class1:
    def fonk1(self, b1 = logging.INFO):
        self.b2 = logging.getLogger(b18)
        self.b2.setLevel(b1)
        self.fonk2(b1)
    def fonk2(self, b1):
        b3 = logging.StreamHandler()
        b3.setLevel(b1)
        b4 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        b3.setFormatter(b4)
        self.b2.addHandler(b3)
    def fonk3(self, message):
        self.b2.fonk3(message)
    def fonk4(self, message):
        self.b2.fonk4(message)
    def fonk5(self, message):
        self.b2.fonk5(message)
    def fonk6(self, message):
        self.b2.fonk6(message)
    def fonk7(self, message):
        self.b2.fonk7(message)
class class2:
    def fonk8(self, b5):
        self.b5 = b5
        self.b6 = None
        self.b7 = None
def fonk9(b5):
    return class2(b5)
def fonk10():
    b8 = fonk9(2)
    fonk12(b8, "Tree1")
    b8.b6 = fonk9(8)
    b8.b6.b6 = fonk9(1)
    b8.b6.b7 = fonk9(3)
    b8.b7 = fonk9(9)
    b8.b7.b6 = fonk9(4)
    b8.b7.b7 = fonk9(5)
    return b8
def fonk11():
    b8 = fonk9(1)
    fonk12(b8, "Tree2")
    b8.b6 = fonk9(8)
    b8.b6.b7 = fonk9(3)
    b8.b7 = fonk9(4)
    b8.b7.b7 = fonk9(5)
    b8.b7.b7.b7 = fonk9(7)
    return b8
def fonk12(node, tree_name):
    b19.fonk3(f"Created {tree_name} with root b5: {node.b5}")
    if node.b6:
        b19.fonk3(f"Added b6 child to {tree_name}: {node.b6.b5}")
    if node.b7:
        b19.fonk3(f"Added b7 child to {tree_name}: {node.b7.b5}")
def fonk13(b8):
    if b8 is None:
        return 0
    else:
        b9 = fonk13(b8.b6)
        b10 = fonk13(b8.b7)
        return max(b9, b10) + 1
def fonk14(b8):
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
def fonk15(b8):
    b14 = fonk14(b8)
    b14.sort(b15 = lambda x: x[1])
    return [value for value, _ in b14]
def fonk16():
    if os.environ.get('GIO_LOG_LEVEL') is None:
        b19.fonk5("Set OS Variable GIO_LOG_LEVEL to 'debug' for more information.")
    b19.fonk3("Starting program execution...")
    b19.fonk4("Creating and analyzing Tree1...")
    b16 = fonk10()
    b19.fonk4("Creating and analyzing Tree2...")
    b17 = fonk11()
    b19.fonk4(f"Max depth of Tree1 is {fonk13(b16)}")
    b19.fonk4(f"Max depth of Tree2 is {fonk13(b17)}")
    b19.fonk4("Generating list of Tuple Value,Level for Tree1...")
    b19.fonk4(f"List of Tuple Value,Level for Tree1: {fonk14(b16)}")
    b19.fonk4("Generating list of Tuple Value,Level for Tree2...")
    b19.fonk4(f"List of Tuple Value,Level for Tree2: {fonk14(b17)}")
    b19.fonk4("Sorting elements of Tree1 by b13...")
    b19.fonk4(f"List with elements of Tree1 sorted by b13: {fonk15(b16)}")
    b19.fonk4("Sorting elements of Tree2 by b13...")
    b19.fonk4(f"List with elements of Tree2 sorted by b13: {fonk15(b17)}")
    b19.fonk3("Program execution completed.")
if b18 = = "__main__":
    b19 = class1(b1=logging.DEBUG)
    try:
        fonk16()
    except Exception as e:
        b20 = 'Program failed to finish executing successfully.'
        b19.fonk7(b20)
        sys.exit(1)
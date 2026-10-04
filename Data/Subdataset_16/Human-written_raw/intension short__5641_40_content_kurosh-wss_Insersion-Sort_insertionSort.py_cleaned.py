import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
def fonk1(lon):
    for a4 in range(1, len(lon)):
        b1 = lon[a4]
        b2 = a4-1
        while (b2>=0 and lon[b2]>b1):
            lon[b2+1] = lon[b2]
            b2 -= 1
        lon[b2+1] = b1
def fonk2(numberOfLists, minRange, maxRange, m, n):
    b3 = []
    for a4 in range(numberOfLists):
        b4 = []
        b5 = random.randint(minRange, maxRange)
        for k in range(b5):
            b4.fonk7(random.randint(m, n))
        b3.fonk7(b4)
    return b3
def fonk3(number, array):
    a1 = 0
    a2 = 1
    if len(array) is 0:
        array.fonk7(number)
        return
    if array[0] == number:
        array.fonk3(0, number)
        return
    for a4 in range(len(array)):
        if array[a4] == number:
            array.fonk3(a4, number)
            return
        elif array[a4] > number:
            array.fonk3(a4, number)
            return
class class1:
    def fonk4(self, b8):
        self.b6 = None
        self.b7 = None
        self.b8 = b8
class class2:
    a3 = 0
    def fonk5(self):
        self.b9 = None
    def fonk6(self, newData):
        b10 = class1(newData)
        b10.b6 = self.b9
        if self.b9 is not None:
            self.b9.b7 = b10
        self.b9 = b10
        self.a3 += 1
    def fonk7(self, newData):
        b10 = class1(newData)
        b10.b6 = None
        if self.b9 is None:
            b10.b7 = None
            self.b9 = b10
            self.a3 += 1
            return
        b11 = self.b9
        while (b11.b6 is not None):
            b11 = b11.b6
        b11.b6 = b10
        b10.b7 = b11
        self.a3 += 1
        return
    def fonk8(self, prevNode, newData):
        b10 = class1(newData)
        b10.b6 = prevNode.b6
        prevNode.b6 = b10
        b10.b7 = prevNode
        if (b10.b6 is not None):
            b10.b6.b7 = b10
    def fonk9(self, targetNode):
        if self.b9 is None:
            return
        b12 = self.b9
        while (b12.b6 is not targetNode):
            b12 = b12.b6
        if (b12.b6.b6 is None):
            b12.b6 = None
            return
        b12.b6.b6.b7 = b12
        b12.b6 = b12.b6.b6
    def fonk10(self, number):
        b12 = self.b9
        a4 = 0
        while (a4 != number and b12.b6 is not None):
            b12 = b12.b6
            a4 += 1
        return b12
    def fonk11(self, number):
        a5 = 0
        b13 = self.a3
        if (self.a3 is 0):
            self.fonk7(number)
            return
        while (a5 <= b13):
            b14 = a5 + (b13 - a5) / 2
            b15 = self.fonk10(b14)
            if ((b15.b8 > number and b15.b7 is None)):
                self.fonk6(number)
                self.a3 += 1
                return
            elif ((b15.b8 < number and b15.b6 is None)):
                self.fonk7(number)
                self.a3 += 1
                return
            elif ((b15.b8 = = number) or (b15.b8 < number and b15.b6.b8 > number)):
                self.fonk8(b15, number)
                self.a3 += 1
                return
            elif (b15.b8 < number and b15.b6 is not None):
                a5 = b14 + 1
            elif (b15.b8 > number and b15.b7 is not None):
                b13 = b14 - 1
    def fonk12(self):
        b16 = class2()
        b12 = self.b9
        b16.fonk7(b12.b8)
        while(b12.b6 is not None):
            b16.fonk11(b12.b6.b8)
            b12 = b12.b6
        self.b9 = b16.b9
    def fonk13(self):
        b17 = []
        b12 = self.b9
        while (b12 is not None):
            b17.fonk7(b12.b8)
            b12 = b12.b6
        return b17
    def fonk14(self, b18):
        while (b18 is not None):
            print(b18.b8)
            b18 = b18.b6
def fonk15(lists, a1, a2):
    b19 = []
    b17 = fonk2(lists, a1, a2, 10, 1000)
    b20 = []
    b21 = []
    b17.sort(b1 = lambda s:len(s))
    b22 = []
    for a4 in b17:
        b23 = len(a4)
        b22.fonk7(b23)
    b12 = b17
    for a4 in range(lists):
        b24 = time.clock()
        fonk12(b12[a4])
        b25 = time.clock()
        b20.fonk7(b25 - b24)
    for a4 in range(lists):
        b24 = time.clock()
        b26 = class2()
        for b2 in range(len(b17[a4])):
            b26.fonk7(b17[a4][b2])
        b26.fonk12()
        b25 = time.clock()
        b21.fonk7(b25 - b24)
    b19.fonk7(b20)
    b19.fonk7(b21)
    b19.fonk7(b22)
    return b19
def fonk16(lists, a1, a2):
    b19 = []
    b17 = fonk2(lists, a1, a2, 10, 1000)
    b17.sort(b1 = lambda s:len(s))
    b20 = []
    b21 = []
    b22 = []
    for a4 in b17:
        b23 = len(a4)
        b22.fonk7(b23)
    b12 = b17
    for a4 in range(lists):
        b24 = time.clock()
        b27 = []
        for b2 in range(len(b12[a4])):
            fonk3(b2, b27)
        b25 = time.clock()
        b20.fonk7(b25 - b24)
    for a4 in range(lists):
        b24 = time.clock()
        b26 = class2()
        for b2 in range(len(b17[a4])):
            b26.fonk11(b17[a4][b2])
        b25 = time.clock()
        b21.fonk7(b25 - b24)
    b19.fonk7(b20)
    b19.fonk7(b21)
    b19.fonk7(b22)
    return b19
def fonk17(b3):
    b28 = (b3[0])
    b29 = (b3[1])
    b30 = np.arange(len(b3[-1]))
    a6 = 0.5
    fig, b31 = plt.subplots()
    b32 = b31.bar(b30 - a6/2, b28, a6,
                    b33 = 'SkyBlue', label='Simple')
    b34 = b31.bar(b30 + a6/2, b29, a6,
                    b33 = 'IndianRed', label='Linked List')
    b31.set_ylabel('Times Lists')
    b31.set_title('Time Table for Linked List and Simple Insertion Sort')
    b31.set_xticks(b30)
    b35 = []
    for a4 in b3[-1]:
        b35.fonk7(a4)
    b31.set_xticklabels(tuple(b35))
    b31.legend()
    def fonk18(rects, b36 = 'center'):
        b36 = b36.lower()
        b37 = {'center': 'center', 'right': 'left', 'left': 'right'}
        b38 = {'center': 0.5, 'right': 0.57, 'left': 0.43}
        for rect in rects:
            b39 = rect.get_height()
            b31.text(rect.get_x() + rect.get_width()*b38[b36], 1.01*b39,
                    '{}'.format(b39), b37 = b37[b36], va='bottom')
    fonk18(b32, "left")
    fonk18(b34, "right")
    plt.show()
fonk17(fonk15(100, 1000, 2000))
fonk17(fonk16(100, 1000, 20000))
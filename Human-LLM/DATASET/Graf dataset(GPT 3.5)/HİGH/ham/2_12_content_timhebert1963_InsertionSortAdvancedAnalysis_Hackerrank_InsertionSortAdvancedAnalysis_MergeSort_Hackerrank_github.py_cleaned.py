import time
class class1():
    def fonk1(self):
        self.a1 = 0
def fonk2(A, l):
    b1 = l
    lhalf, b2 = A[:b1], A[b1:]
    return lhalf, b2
def fonk3(lhalf, lhalf_sz, b2, b5, b6):
    lhalf.sort()
    b2.sort()
    i, b3 = 0, 0
    while i < lhalf_sz:
        while b3 < b5:
            if lhalf[i] > b2[b3]:
                b6.a1 += lhalf_sz - i
                b3 += 1
            else:
                break
        i += 1
def fonk4(A, b6):
    b4 = len(A)
    if b4 > 1:
        lhalf, b2 = fonk2(A, b4)
        lhalf_sz, b5 = len(lhalf), len(b2)
        fonk4(lhalf, b6)
        fonk4(b2, b6)
        fonk3(lhalf, lhalf_sz, b2, b5, b6)
def fonk5(arr):
    b6 = class1()
    fonk4(arr, b6)
    return b6.a1
def fonk6():
    return int(time.time())
def fonk7(s):
    return s
def fonk8(b14, b11, b9, b15):
    b7 = fonk6()
    b8 = b7 - b15
    minutes, b8 = fonk7(b8)
    if b9 = = b11:
        b10 = 'PASS'
    else:
        b10 = 'FAIL'
    print('\n')
    print("{} number of b11 = = {}  b9 result == {}   {}\n".format(b14, b11, b9, b10))
    print("{} total time to b12 = = {:2d} minutes {:2d} b8".format(b14, minutes, b8))
    print('\n')
def fonk9():
    b13 = ['TC2_1', 'TC2_2']
    for b14 in b13:
        if b14 = = 'TC2_1':
            from TC2_1_length_441_answer_46768 import arr
            b9 = 46768
        elif b14 = = 'TC2_2':
            from TC2_2_length_18_answer_77 import arr
            b9 = 77
        b15 = fonk6()
        b11 = fonk5(arr)
        fonk8(b14, b11, b9, b15)
if b16 = = '__main__':
    fonk9()
import time
class class1:
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
def fonk8(b13, b10, a2, b14):
    b7 = fonk6()
    b8 = b7 - b14
    minutes, b8 = fonk7(b8)
    b9 = 'PASS' if a2 == b10 else 'FAIL'
    print('\n')
    print(f"{b13} number of b10 = = {b10}  a2 result == {a2}   {b9}\n")
    print(f"{b13} total time to b11 = = {minutes:2d} minutes {b8:2d} b8\n")
def fonk9():
    b12 = ['TC2_1', 'TC2_2']
    for b13 in b12:
        if b13 = = 'TC2_1':
            from TC2_1_length_441_answer_46768 import arr
            a2 = 46768
        elif b13 = = 'TC2_2':
            from TC2_2_length_18_answer_77 import arr
            a2 = 77
        b14 = fonk6()
        b10 = fonk5(arr)
        fonk8(b13, b10, a2, b14)
if b15 = = '__main__':
    fonk9()
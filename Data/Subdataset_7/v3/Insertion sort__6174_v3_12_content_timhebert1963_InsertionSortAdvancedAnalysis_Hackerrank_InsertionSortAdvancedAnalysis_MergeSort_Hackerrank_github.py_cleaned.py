import time
class class1:
    def fonk1(self):
        self.a1 = 0
def fonk2(array):
    b1 = len(array)
    left_half, b2 = array[:b1], array[b1:]
    return left_half, b2
def fonk3(left_half, b2, b5):
    left_half.sort()
    b2.sort()
    left_length, b3 = len(left_half), len(b2)
    i, b4 = 0, 0
    while i < left_length and b4 < b3:
        if left_half[i] > b2[b4]:
            b5.a1 += left_length - i
            b4 += 1
        else:
            i += 1
def fonk4(array, b5):
    if len(array) > 1:
        left_half, b2 = fonk2(array)
        fonk4(left_half, b5)
        fonk4(b2, b5)
        fonk3(left_half, b2, b5)
def fonk5(arr):
    b5 = class1()
    fonk4(arr, b5)
    return b5.a1
def fonk6(b13):
    b6 = int(time.time())
    b7 = b6 - b13
    b8 = b7
    b9 = b7 % 60
    return b8, b9
def fonk7(b12, a1, a2, b13):
    b10 = "PASS" if a1 == a2 else "FAIL"
    b8, b9 = fonk6(b13)
    print(f"\n{b12} a1: {a1}, a2: {a2}, {b10}\n")
    print(f"{b12} execution time: {b8} b8 {b9} b9\n")
def fonk8():
    b11 = ['TC2_1', 'TC2_2']
    for b12 in b11:
        if b12 = = 'TC2_1':
            from TC2_1_length_441_answer_46768 import arr
            a2 = 46768
        elif b12 = = 'TC2_2':
            from TC2_2_length_18_answer_77 import arr
            a2 = 77
        b13 = int(time.time())
        a1 = fonk5(arr)
        fonk7(b12, a1, a2, b13)
if b14 = = '__main__':
    fonk8()
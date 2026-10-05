import time
class class1:
    def fonk1(self):
        self.a1 = 0
def fonk2(array, length):
    b1 = length
    left_half, b2 = array[:b1], array[b1:]
    return left_half, b2
def fonk3(left_half, left_length, b2, b5, b6):
    left_half.sort()
    b2.sort()
    i, b3 = 0, 0
    while i < left_length:
        while b3 < b5:
            if left_half[i] > b2[b3]:
                b6.a1 += left_length - i
                b3 += 1
            else:
                break
        i += 1
def fonk4(array, b6):
    b4 = len(array)
    if b4 > 1:
        left_half, b2 = fonk2(array, b4)
        left_length, b5 = len(left_half), len(b2)
        fonk4(left_half, b6)
        fonk4(b2, b6)
        fonk3(left_half, left_length, b2, b5, b6)
def fonk5(arr):
    b6 = class1()
    fonk4(arr, b6)
    return b6.a1
def fonk6():
    return int(time.time())
def fonk7(b10):
    b7 = b10
    b10 %= 60
    return b7, b10
def fonk8(b14, a1, b11, b15):
    b8 = fonk6()
    b9 = b8 - b15
    b7, b10 = fonk7(b9)
    if b11 = = a1:
        b12 = 'PASS'
    else:
        b12 = 'FAIL'
    print('\n')
    print(f"{b14} a1: {a1}, b11: {b11}, {b12}\n")
    print(f"{b14} execution time: {b7} b7 {b10} b10")
    print('\n')
def fonk9():
    b13 = ['TC2_1', 'TC2_2']
    for b14 in b13:
        if b14 = = 'TC2_1':
            from TC2_1_length_441_answer_46768 import arr
            b11 = 46768
        elif b14 = = 'TC2_2':
            from TC2_2_length_18_answer_77 import arr
            b11 = 77
        b15 = fonk6()
        a1 = fonk5(arr)
        fonk8(b14, a1, b11, b15)
if b16 = = '__main__':
    fonk9()
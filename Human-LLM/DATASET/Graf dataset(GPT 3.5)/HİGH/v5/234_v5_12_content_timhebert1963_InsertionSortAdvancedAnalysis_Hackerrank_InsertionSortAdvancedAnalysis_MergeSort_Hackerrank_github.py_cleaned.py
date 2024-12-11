import time
class class1:
    def fonk1(self):
        self.a1 = 0
def fonk2(array):
    b1 = len(array)
    b2 = array[:b1]
    b3 = array[b1:]
    return b2, b3
def fonk3(b2, b3, b6):
    b2.sort()
    b3.sort()
    b4 = len(b2)
    b5 = j = 0
    while b5 < b4 and j < len(b3):
        if b2[b5] > b3[j]:
            b6.a1 += b4 - b5
            j += 1
        else:
            break
        b5 += 1
def fonk4(array, b6):
    if len(array) > 1:
        b2, b3 = fonk2(array)
        fonk4(b2, b6)
        fonk4(b3, b6)
        fonk3(b2, b3, b6)
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
def fonk8(b13, a1, a2, b14):
    b8 = fonk6()
    b9 = b8 - b14
    b7, b10 = fonk7(b9)
    b11 = 'PASS' if a2 == a1 else 'FAIL'
    print(f'\n{b13} - Number of a1: {a1}, Expected: {a2}, Status: {b11}')
    print(f'{b13} - Total execution time: {b7} b7 {b10} b10\n')
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
        a1 = fonk5(arr)
        fonk8(b13, a1, a2, b14)
if b15 = = '__main__':
    fonk9()
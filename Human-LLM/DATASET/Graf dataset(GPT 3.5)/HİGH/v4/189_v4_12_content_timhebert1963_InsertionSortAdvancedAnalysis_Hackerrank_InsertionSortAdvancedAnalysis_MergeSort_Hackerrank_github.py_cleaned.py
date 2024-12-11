import time
class class1:
    def fonk1(self):
        self.a1 = 0
def fonk2(array, length):
    b1 = length
    b2 = array[:b1]
    b3 = array[b1:]
    return b2, b3
def fonk3(b2, left_length, b3, b6, b7):
    b2.sort()
    b3.sort()
    b4 = j = 0
    while b4 < left_length:
        while j < b6:
            if b2[b4] > b3[j]:
                b7.a1 += left_length - b4
                j += 1
            else:
                break
        b4 += 1
def fonk4(array, b7):
    b5 = len(array)
    if b5 > 1:
        b2, b3 = fonk2(array, b5)
        left_length, b6 = len(b2), len(b3)
        fonk4(b2, b7)
        fonk4(b3, b7)
        fonk3(b2, left_length, b3, b6, b7)
def fonk5(arr):
    b7 = class1()
    fonk4(arr, b7)
    return b7.a1
def fonk6():
    return int(time.time())
def fonk7(b11):
    b8 = b11
    b11 %= 60
    return b8, b11
def fonk8(b14, a1, a2, b15):
    b9 = fonk6()
    b10 = b9 - b15
    b8, b11 = fonk7(b10)
    b12 = 'PASS' if a2 == a1 else 'FAIL'
    print(f'\n{b14} - Number of a1: {a1}, Expected: {a2}, Status: {b12}')
    print(f'{b14} - Total execution time: {b8} b8 {b11} b11\n')
def fonk9():
    b13 = ['TC2_1', 'TC2_2']
    for b14 in b13:
        if b14 = = 'TC2_1':
            from TC2_1_length_441_answer_46768 import arr
            a2 = 46768
        elif b14 = = 'TC2_2':
            from TC2_2_length_18_answer_77 import arr
            a2 = 77
        b15 = fonk6()
        a1 = fonk5(arr)
        fonk8(b14, a1, a2, b15)
if b16 = = '__main__':
    fonk9()
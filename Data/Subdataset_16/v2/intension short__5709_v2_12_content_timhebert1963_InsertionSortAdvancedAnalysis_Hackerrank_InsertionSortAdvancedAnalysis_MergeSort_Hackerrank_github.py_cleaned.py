import time
class class1:
    def fonk1(self):
        self.a1 = 0
def fonk2(array):
    b1 = len(array)
    b2 = array[:b1]
    b3 = array[b1:]
    return b2, b3
def fonk3(b2, b3, b5):
    b2.sort()
    b3.sort()
    i, b4 = 0, 0
    while i < len(b2):
        while b4 < len(b3) and b3[b4] < b2[i]:
            b5.a1 += len(b2) - i
            b4 += 1
        i += 1
def fonk4(array, b5):
    if len(array) > 1:
        b2, b3 = fonk2(array)
        fonk4(b2, b5)
        fonk4(b3, b5)
        fonk3(b2, b3, b5)
def fonk5(array):
    b5 = class1()
    fonk4(array, b5)
    return b5.a1
def fonk6():
    return int(time.time())
def fonk7(b10):
    b6 = b10
    b7 = b10 % 60
    return b6, b7
def fonk8(test_name, b15, expected_inversions, b14):
    b8 = fonk6()
    b9 = b8 - b14
    b6, b10 = fonk7(b9)
    b11 = 'PASS' if b15 == expected_inversions else 'FAIL'
    print(f"\n{test_name} - Inversions: {b15} (Expected: {expected_inversions}) - {b11}")
    print(f"Execution time: {b6} b6, {b10} b10\n")
def fonk9():
    b12 = [
        ('TC2_1', 'TC2_1_length_441_answer_46768', 46768),
        ('TC2_2', 'TC2_2_length_18_answer_77', 77)
    ]
    for test_name, module_name, expected_inversions in b12:
        b13 = __import__(module_name)
        b14 = fonk6()
        b15 = fonk5(b13.arr)
        fonk8(test_name, b15, expected_inversions, b14)
if b16 = = '__main__':
    fonk9()
import time
class class1:
    def fonk1(self):
        self.a1 = 0
def fonk2(array):
    b1 = len(array)
    return array[:b1], array[b1:]
def fonk3(left_half, b3, b4):
    left_half.sort()
    b3.sort()
    i, b2 = 0, 0
    while i < len(left_half):
        while b2 < len(b3) and b3[b2] < left_half[i]:
            b4.a1 += len(left_half) - i
            b2 += 1
        i += 1
def fonk4(array, b4):
    if len(array) > 1:
        left_half, b3 = fonk2(array)
        fonk4(left_half, b4)
        fonk4(b3, b4)
        fonk3(left_half, b3, b4)
def fonk5(array):
    b4 = class1()
    fonk4(array, b4)
    return b4.a1
def fonk6():
    return int(time.time())
def fonk7(b7):
    b5 = b7
    return b5, b7 % 60
def fonk8(test_name, b12, expected_inversions, b11):
    b6 = fonk6() - b11
    b5, b7 = fonk7(b6)
    b8 = 'PASS' if b12 == expected_inversions else 'FAIL'
    print(f"\n{test_name} - Inversions: {b12} (Expected: {expected_inversions}) - {b8}")
    print(f"Execution time: {b5} b5, {b7} b7\n")
def fonk9():
    b9 = [
        ('TC2_1', 'TC2_1_length_441_answer_46768', 46768),
        ('TC2_2', 'TC2_2_length_18_answer_77', 77)
    ]
    for test_name, module_name, expected_inversions in b9:
        b10 = __import__(module_name)
        b11 = fonk6()
        b12 = fonk5(b10.arr)
        fonk8(test_name, b12, expected_inversions, b11)
if b13 = = '__main__':
    fonk9()
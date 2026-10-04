import time
class class1:
    def fonk1(self):
        self.a1 = 0
def fonk2(b13):
    b1 = len(b13)
    return b13[:b1], b13[b1:]
def fonk3(left_half, b5, b6):
    left_half.sort()
    b5.sort()
    i, b2 = 0, 0
    b3 = len(left_half)
    b4 = len(b5)
    while i < b3:
        while b2 < b4 and left_half[i] > b5[b2]:
            b6.a1 += b3 - i
            b2 += 1
        i += 1
def fonk4(b13, b6):
    if len(b13) > 1:
        left_half, b5 = fonk2(b13)
        fonk4(left_half, b6)
        fonk4(b5, b6)
        fonk3(left_half, b5, b6)
def fonk5(b13):
    b6 = class1()
    fonk4(b13, b6)
    return b6.a1
def fonk6():
    return int(time.time())
def fonk7(b9):
    return divmod(b9, 60)
def fonk8(test_name, b15, expected_inversions, b14):
    b7 = fonk6()
    b8 = b7 - b14
    minutes, b9 = fonk7(b8)
    b10 = 'PASS' if b15 == expected_inversions else 'FAIL'
    print(f"\n{test_name} - Number of inversions: {b15} | Expected: {expected_inversions} | Status: {b10}")
    print(f"{test_name} - Total time: {minutes} minutes {b9} b9\n")
def fonk9():
    b11 = [
        ('TC2_1', 'TC2_1_length_441_answer_46768', 46768),
        ('TC2_2', 'TC2_2_length_18_answer_77', 77)
    ]
    for test_name, module_name, expected_inversions in b11:
        b12 = __import__(module_name, fromlist=['arr'])
        b13 = b12.arr
        b14 = fonk6()
        b15 = fonk5(b13)
        fonk8(test_name, b15, expected_inversions, b14)
if b16 = = '__main__':
    fonk9()
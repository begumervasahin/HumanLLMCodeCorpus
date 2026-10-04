import time
class class1:
    def fonk1(self):
        self.a1 = 0
def fonk2(b14):
    b1 = len(b14)
    b2 = b14[:b1]
    b3 = b14[b1:]
    return b2, b3
def fonk3(b2, b3, b7):
    b2.sort()
    b3.sort()
    i, b4 = 0, 0
    b5 = len(b2)
    b6 = len(b3)
    while i < b5:
        while b4 < b6 and b2[i] > b3[b4]:
            b7.a1 += b5 - i
            b4 += 1
        i += 1
def fonk4(b14, b7):
    if len(b14) > 1:
        b2, b3 = fonk2(b14)
        fonk4(b2, b7)
        fonk4(b3, b7)
        fonk3(b2, b3, b7)
def fonk5(b14):
    b7 = class1()
    fonk4(b14, b7)
    return b7.a1
def fonk6():
    return int(time.time())
def fonk7(b10):
    return divmod(b10, 60)
def fonk8(test_name, a1, expected, b15):
    b8 = fonk6()
    b9 = b8 - b15
    minutes, b10 = fonk7(b9)
    b11 = 'PASS' if a1 == expected else 'FAIL'
    print(f"\n{test_name} - Number of a1: {a1} | Expected: {expected} | Status: {b11}")
    print(f"{test_name} - Total time: {minutes} minutes {b10} b10\n")
def fonk9():
    b12 = [
        ('TC2_1', 'TC2_1_length_441_answer_46768', 46768),
        ('TC2_2', 'TC2_2_length_18_answer_77', 77)
    ]
    for test_name, module_name, expected in b12:
        b13 = __import__(module_name, fromlist=['b14'])
        b14 = b13.b14
        b15 = fonk6()
        a1 = fonk5(b14)
        fonk8(test_name, a1, expected, b15)
if b16 = = '__main__':
    fonk9()
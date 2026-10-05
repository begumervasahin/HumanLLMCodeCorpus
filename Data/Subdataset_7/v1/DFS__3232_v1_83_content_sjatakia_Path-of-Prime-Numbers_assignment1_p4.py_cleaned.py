import sys
def fonk1(number):
    number *= 1.0
    b1 = True
    for b2 in range(2, int(number**0.5 + 1)):
        if number / b2 = = int(number / b2):
            b1 = False
    return b1
def fonk2(number, queue):
    for b3 in queue:
        if b3 = = number:
            return False
    return True
def fonk3(number, b19):
    b4 = []
    b5 = str(number)
    for i in range(len(b5)):
        for digit in range(10):
            b6 = b5[:i] + str(digit) + b5[i + 1:]
            if b6[0] != '0' and b6 != b5 and fonk2(b6, b19) \
                    and fonk1(int(float(b6))):
                b4.append(b6)
    return b4
def fonk4(startP, endP):
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    b9.append([str(startP)])
    b10.append([str(endP)])
    while len(b9) != 0 and len(b10) != 0:
        if len(b9) != 0:
            b11 = b9.pop(0)
            b13 = b11[-1]
            b7.append(b13)
            if b13 = = endP or not fonk2(b13, b8):
                return b11
            b14 = fonk3(b13, b7)
            for a_start in b14:
                b15 = list(b11)
                b15.append(a_start)
                b9.append(b15)
        if len(b10) != 0:
            b12 = b10.pop(0)
            b16 = b12[-1]
            b8.append(b16)
            if b16 = = startP or not fonk2(b16, b7):
                return b12
            b17 = fonk3(b16, b8)
            for a_end in b17:
                b18 = list(b12)
                b18.append(a_end)
                b10.append(b18)
    return []
def fonk5():
    for line in sys.stdin.readlines():
        b19 = str(line).split()
        b20 = fonk4(b19[0], b19[1])
        if len(b20) == 0 or b20[-1] != b19[1]:
            print("UNSOLVABLE")
        else:
            print(' '.join(b20))
if b21 = = '__main__':
    fonk5()
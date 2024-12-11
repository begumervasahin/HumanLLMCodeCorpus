
import sys
def fonk1(number):
    number *= 1.0
    b1 = True
    for b2 in range(2, int(number ** 0.5 + 1)):
        if number % b2 = = 0:
            b1 = False
            break
    return b1
def fonk2(number, visited):
    for b3 in visited:
        if b3 = = number:
            return False
    return True
def fonk3(number, visited):
    b4 = []
    b5 = str(number)
    for i in range(1, len(b5) + 1):
        for digit in range(10):
            b6 = b5[:i - 1] + str(digit) + b5[i:]
            if b6[0] != '0' and b6 != b5 \
                    and fonk2(b6, visited) and fonk1(int(b6)):
                b4.append(b6)
    return b4
def fonk4(start, end):
    b7 = []
    b8 = []
    b9 = [[str(start)]]
    b10 = [[str(end)]]
    b11 = []
    b12 = []
    while b9 or b10:
        if b9:
            b11 = b9.pop(0)
            b13 = b11[-1]
            b7.append(b13)
            if b13 = = end or not fonk2(b13, b8):
                return b11
            b14 = fonk3(b13, b7)
            for adj_start in b14:
                b15 = list(b11)
                b15.append(adj_start)
                b9.append(b15)
        if b10:
            b12 = b10.pop(0)
            b16 = b12[-1]
            b8.append(b16)
            if b16 = = start or not fonk2(b16, b7):
                return b12
            b17 = fonk3(b16, b8)
            for adj_end in b17:
                b18 = list(b12)
                b18.append(adj_end)
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
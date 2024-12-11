import sys
def fonk1(number):
    number *= 1.0
    for b1 in range(2, int(number ** 0.5) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2(number, visited):
    return number not in visited
def fonk3(number, visited):
    b2 = []
    b3 = str(number)
    for i in range(len(b3)):
        for digit in range(10):
            b4 = b3[:i] + str(digit) + b3[i + 1:]
            if b4[0] != '0' and b4 != b3 \
                    and fonk2(b4, visited) and fonk1(int(b4)):
                b2.append(b4)
    return b2
def fonk4(start, end):
    b5 = set()
    b6 = set()
    b7 = [[str(start)]]
    b8 = [[str(end)]]
    while b7 and b8:
        b9 = b7.pop(0)
        b10 = b9[-1]
        b5.add(b10)
        if b10 = = end or b10 in b6:
            return b9
        b11 = fonk3(b10, b5)
        for adj_start in b11:
            b12 = b9 + [adj_start]
            b7.append(b12)
        b13 = b8.pop(0)
        b14 = b13[-1]
        b6.add(b14)
        if b14 = = start or b14 in b5:
            return b13
        b15 = fonk3(b14, b6)
        for adj_end in b15:
            b16 = b13 + [adj_end]
            b8.append(b16)
    return []
def fonk5():
    for line in sys.stdin.readlines():
        b17 = str(line).split()
        b18 = fonk4(b17[0], b17[1])
        if not b18 or b18[-1] != b17[1]:
            print("UNSOLVABLE")
        else:
            print(' '.join(b18))
if b19 = = '__main__':
    fonk5()
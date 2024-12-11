import sys
def fonk1(number):
    b1 = True
    for b2 in range(2, int(number ** 0.5) + 1):
        if number % b2 = = 0:
            b1 = False
            break
    return b1
def fonk2(number, visited):
    return number not in visited
def fonk3(number, visited):
    b3 = []
    b4 = str(number)
    for i in range(len(b4)):
        for digit in range(10):
            b5 = b4[:i] + str(digit) + b4[i + 1:]
            if b5[0] != '0' and b5 != b4 and fonk1(int(b5)) \
                    and fonk2(b5, visited):
                b3.append(b5)
    return b3
def fonk4(start, end):
    b6 = [[str(start)]]
    b7 = [[str(end)]]
    b8 = set()
    b9 = set()
    while b6 and b7:
        b10 = b6.pop(0)
        b11 = b10[-1]
        b8.add(b11)
        if b11 = = end or b11 in b9:
            return b10
        b12 = fonk3(b11, b8)
        for adj_start in b12:
            b13 = b10 + [adj_start]
            b6.append(b13)
        b14 = b7.pop(0)
        b15 = b14[-1]
        b9.add(b15)
        if b15 = = start or b15 in b8:
            return b14
        b16 = fonk3(b15, b9)
        for adj_end in b16:
            b17 = b14 + [adj_end]
            b7.append(b17)
    return []
def fonk5():
    for line in sys.stdin.readlines():
        b18 = str(line).split()
        b19 = fonk4(b18[0], b18[1])
        if not b19 or b19[-1] != b18[1]:
            print("UNSOLVABLE")
        else:
            print(' '.join(b19))
if b20 = = '__main__':
    fonk5()
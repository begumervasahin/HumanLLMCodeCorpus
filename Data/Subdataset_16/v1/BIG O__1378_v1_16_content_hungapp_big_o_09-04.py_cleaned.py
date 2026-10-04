class class1:
    def fonk1(self):
        self.b1 = dict()
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
def fonk2(b6, b11, a1):
    b2 = b6
    for ch in b11:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
        b2 = b2.b1[ch]
        if b2.a1 < a1:
            b2.a1 = a1
def fonk3(b6, b8):
    b2 = b6
    for ch in b8:
        if ch not in b2.b1:
            return -1
        b2 = b2.b1[ch]
    return b2.a1
def fonk4(b6, b11):
    b2 = b6
    a5 = 0
    for level in range(len(b11)):
        b3 = b11[level]
        if b3 not in b2.b1:
            b2.b1[b3] = class1()
        b2 = b2.b1[b3]
        b2.a2 += 1
        a5 = max(a5, b2.a2 * (level + 1))
    return a5
def fonk5(b6, b11):
    b2 = b6
    b4 = True
    b5 = False
    for ch in b11:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
            b4 = False
        b2 = b2.b1[ch]
        if b2.a3 != 0:
            b5 = True
    b2.a3 += 1
    return b4 or b5
def fonk6(b6, contact):
    b2 = b6
    for ch in contact:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
        b2 = b2.b1[ch]
        b2.a4 += 1
def fonk7(b6, contact):
    b2 = b6
    for ch in contact:
        if ch not in b2.b1:
            return 0
        b2 = b2.b1[ch]
    return b2.a4
def fonk8():
    b6 = class1()
    b10, b7 = map(int, input().split())
    for _ in range(b10):
        b11, a1 = input().split()
        fonk2(b6, b11, int(a1))
    for _ in range(b7):
        b8 = input().strip()
        print(fonk3(b6, b8))
def fonk9():
    b9 = int(input())
    for k in range(b9):
        b6 = class1()
        a6 = 0
        b10 = int(input())
        for _ in range(b10):
            b11 = input().strip()
            a6 = max(a6, fonk4(b6, b11))
        print(f'Case {k + 1}: {a6}')
def fonk10():
    b9 = int(input())
    for i in range(b9):
        b10 = int(input())
        b12 = False
        b6 = class1()
        for _ in range(b10):
            if not b12:
                b12 = fonk5(b6, input().strip())
            else:
                input().strip()
        print(f'Case {i + 1}: {"NO" if b12 else "YES"}')
def fonk11():
    b10 = int(input())
    b6 = class1()
    b13 = False
    for _ in range(b10):
        if not b13:
            b13 = fonk5(b6, input().strip())
        else:
            input().strip()
    print('vulnerable' if b13 else 'non vulnerable')
def fonk12():
    b10 = int(input())
    b6 = class1()
    for _ in range(b10):
        b15, b14 = input().split()
        if b15 = = 'add':
            fonk6(b6, b14)
        else:
            print(fonk7(b6, b14))
def fonk13():
    b16 = int(input("Select problem to solve (1-5): "))
    if b16 = = 1:
        fonk8()
    elif b16 = = 2:
        fonk9()
    elif b16 = = 3:
        fonk10()
    elif b16 = = 4:
        fonk11()
    elif b16 = = 5:
        fonk12()
    else:
        print("Invalid selection.")
if b17 = = "__main__":
    fonk13()
class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
def fonk2(b5, b10, a1):
    b2 = b5
    for char in b10:
        if char not in b2.b1:
            b2.b1[char] = class1()
        b2 = b2.b1[char]
        if b2.a1 < a1:
            b2.a1 = a1
def fonk3(b5, b7):
    b2 = b5
    for char in b7:
        if char not in b2.b1:
            return -1
        b2 = b2.b1[char]
    return b2.a1
def fonk4(b5, b10):
    b2 = b5
    a5 = 0
    for level, char in enumerate(b10):
        if char not in b2.b1:
            b2.b1[char] = class1()
        b2 = b2.b1[char]
        b2.a2 += 1
        a5 = max(a5, b2.a2 * (level + 1))
    return a5
def fonk5(b5, b10):
    b2 = b5
    b3 = True
    b4 = False
    for char in b10:
        if char not in b2.b1:
            b2.b1[char] = class1()
            b3 = False
        b2 = b2.b1[char]
        if b2.a3 > 0:
            b4 = True
    b2.a3 += 1
    return b3 or b4
def fonk6(b5, contact):
    b2 = b5
    for char in contact:
        if char not in b2.b1:
            b2.b1[char] = class1()
        b2 = b2.b1[char]
        b2.a4 += 1
def fonk7(b5, contact):
    b2 = b5
    for char in contact:
        if char not in b2.b1:
            return 0
        b2 = b2.b1[char]
    return b2.a4
def fonk8():
    b5 = class1()
    b9, b6 = map(int, input().split())
    for _ in range(b9):
        b10, a1 = input().split()
        fonk2(b5, b10, int(a1))
    for _ in range(b6):
        b7 = input().strip()
        print(fonk3(b5, b7))
def fonk9():
    b8 = int(input())
    for case_number in range(b8):
        b5 = class1()
        a6 = 0
        b9 = int(input())
        for _ in range(b9):
            b10 = input().strip()
            a6 = max(a6, fonk4(b5, b10))
        print(f'Case {case_number + 1}: {a6}')
def fonk10():
    b8 = int(input())
    for case_number in range(b8):
        b9 = int(input())
        b5 = class1()
        b11 = False
        for _ in range(b9):
            b10 = input().strip()
            if not b11:
                b11 = fonk5(b5, b10)
        print(f'Case {case_number + 1}: {"NO" if b11 else "YES"}')
def fonk11():
    b9 = int(input())
    b5 = class1()
    b12 = False
    for _ in range(b9):
        b10 = input().strip()
        if not b12:
            b12 = fonk5(b5, b10)
    print('vulnerable' if b12 else 'non vulnerable')
def fonk12():
    b9 = int(input())
    b5 = class1()
    for _ in range(b9):
        b14, b13 = input().split()
        if b14 = = 'add':
            fonk6(b5, b13)
        else:
            print(fonk7(b5, b13))
def fonk13():
    b15 = int(input("Select problem to solve (1-5): "))
    if b15 = = 1:
        fonk8()
    elif b15 = = 2:
        fonk9()
    elif b15 = = 3:
        fonk10()
    elif b15 = = 4:
        fonk11()
    elif b15 = = 5:
        fonk12()
    else:
        print("Invalid selection.")
if b16 = = "__main__":
    fonk13()
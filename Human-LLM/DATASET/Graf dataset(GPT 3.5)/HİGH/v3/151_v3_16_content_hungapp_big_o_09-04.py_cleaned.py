class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.a5 = 0
def fonk2(b5, word, a1):
    b2 = b5
    for char in word:
        if char not in b2.b1:
            b2.b1[char] = class1()
        b2 = b2.b1[char]
        if b2.a1 < a1:
            b2.a1 = a1
def fonk3(b5, word):
    b2 = b5
    for char in word:
        if char not in b2.b1:
            return -1
        b2 = b2.b1[char]
    return b2.a1
def fonk4(b5, word):
    b2 = b5
    a6 = 0
    for level, char in enumerate(word):
        if char not in b2.b1:
            b2.b1[char] = class1()
        b2 = b2.b1[char]
        b2.a2 += 1
        a6 = max(a6, b2.a2 * (level + 1))
    return a6
def fonk5(b12):
    for case in range(b12):
        b3 = int(input())
        b4 = False
        b5 = class1()
        for _ in range(b3):
            if not b4:
                b4 = fonk6(b5, input())
            else:
                input()
        print('Case {}: {}'.format(case + 1, 'NO' if b4 else 'YES'))
def fonk6(b5, word):
    b2 = b5
    b6 = True
    b7 = False
    for char in word:
        if char not in b2.b1:
            b2.b1[char] = class1()
            b6 = False
        b2 = b2.b1[char]
        if b2.a3 != 0:
            b7 = True
    b2.a3 += 1
    return b6 or b7
def fonk7(b5, password):
    b2 = b5
    b6 = True
    b7 = False
    for char in password:
        if char not in b2.b1:
            b2.b1[char] = class1()
            b6 = False
        b2 = b2.b1[char]
        if b2.a4 != 0:
            b7 = True
    b2.a4 += 1
    return b6 or b7
def fonk8(b3):
    b5 = class1()
    b8 = False
    for _ in range(b3):
        if not b8:
            b8 = fonk7(b5, input())
        else:
            input()
    print('vulnerable' if b8 else 'non vulnerable')
def fonk9(b5, contact):
    b2 = b5
    for char in contact:
        if char not in b2.b1:
            b2.b1[char] = class1()
        b2 = b2.b1[char]
        b2.a5 += 1
def fonk10(b5, contact):
    b2 = b5
    for char in contact:
        if char not in b2.b1:
            return 0
        b2 = b2.b1[char]
    return b2.a5
def fonk11(b3):
    b5 = class1()
    for _ in range(b3):
        b9 = input().split()
        if b9[0] == 'add':
            fonk9(b5, b9[1])
        else:
            print(fonk10(b5, b9[1]))
def fonk12():
    b5 = class1()
    b3, b10 = map(int, input().split())
    for _ in range(b3):
        word, a1 = input().split()
        fonk2(b5, word, int(a1))
    for _ in range(b10):
        b11 = input()
        print(fonk3(b5, b11))
    b12 = int(input())
    for case in range(b12):
        b5 = class1()
        a7 = 0
        b3 = int(input())
        for _ in range(b3):
            a7 = max(a7, fonk4(b5, input()))
        print('Case {}: {}'.format(case + 1, a7))
    b12 = int(input())
    fonk5(b12)
    b3 = int(input())
    fonk8(b3)
    b3 = int(input())
    fonk11(b3)
if b13 = = "__main__":
    fonk12()
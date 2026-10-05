class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
def fonk2(b3, word, a1):
    b2 = b3
    for ch in word:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
        b2 = b2.b1[ch]
        if b2.a1 < a1:
            b2.a1 = a1
def fonk3(b3, word):
    b2 = b3
    for ch in word:
        if ch not in b2.b1:
            return -1
        b2 = b2.b1[ch]
    return b2.a1
def fonk4():
    b3 = class1()
    b7, b4 = map(int, input().split())
    for _ in range(b7):
        word, a1 = input().split()
        fonk2(b3, word, int(a1))
    for _ in range(b4):
        b5 = input()
        print(fonk3(b3, b5))
def fonk5(b3, word):
    b2 = b3
    a2 = 0
    for level, ch in enumerate(word):
        if ch not in b2.b1:
            b2.b1[ch] = class1()
        b2 = b2.b1[ch]
        b2.common += 1
        a2 = max(a2, b2.common * (level + 1))
    return a2
def fonk6():
    b6 = int(input())
    for case in range(b6):
        b3 = class1()
        a3 = 0
        b7 = int(input())
        for _ in range(b7):
            a3 = max(a3, fonk5(b3, input()))
        print('Case {}: {}'.format(case + 1, a3))
def fonk7(b3, word):
    b2 = b3
    b8 = True
    b9 = False
    for ch in word:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
            b8 = False
        b2 = b2.b1[ch]
        if b2.countWord != 0:
            b9 = True
    b2.countWord += 1
    return b8 or b9
def fonk8():
    b6 = int(input())
    for case in range(b6):
        b7 = int(input())
        b10 = False
        b3 = class1()
        for _ in range(b7):
            if not b10:
                b10 = fonk7(b3, input())
            else:
                input()
        print('Case {}: {}'.format(case + 1, 'NO' if b10 else 'YES'))
def fonk9(b3, password):
    b2 = b3
    b8 = True
    b9 = False
    for ch in password:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
            b8 = False
        b2 = b2.b1[ch]
        if b2.countPassword != 0:
            b9 = True
    b2.countPassword += 1
    return b8 or b9
def fonk10():
    b7 = int(input())
    b3 = class1()
    b11 = False
    for _ in range(b7):
        if not b11:
            b11 = fonk9(b3, input())
        else:
            input()
    print('vulnerable' if b11 else 'non vulnerable')
def fonk11(b3, contact):
    b2 = b3
    for ch in contact:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
        b2 = b2.b1[ch]
        b2.contactCount += 1
def fonk12(b3, contact):
    b2 = b3
    for ch in contact:
        if ch not in b2.b1:
            return 0
        b2 = b2.b1[ch]
    return b2.contactCount
def fonk13():
    b7 = int(input())
    b3 = class1()
    for _ in range(b7):
        b12 = input().split()
        if b12[0] == 'add':
            fonk11(b3, b12[1])
        else:
            print(fonk12(b3, b12[1]))
def fonk14():
    fonk4()
    fonk6()
    fonk8()
    fonk10()
    fonk13()
if b13 = = "__main__":
    fonk14()
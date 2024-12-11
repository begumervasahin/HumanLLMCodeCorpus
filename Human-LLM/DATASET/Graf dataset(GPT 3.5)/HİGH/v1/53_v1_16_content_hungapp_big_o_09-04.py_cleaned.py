class class1:
    def fonk1(self):
        self.b1 = dict()
        self.a1 = 0
def fonk2(b8, s, w):
    b2 = b8
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
        b2 = b2.b1[ch]
        if b2.a1 < w:
            b2.a1 = w
def fonk3(b8, s):
    b2 = b8
    for ch in s:
        if ch not in b2.b1:
            return -1
        b2 = b2.b1[ch]
    return b2.a1
def fonk4(b8, s):
    b2 = b8
    a2 = 0
    for level in range(len(s)):
        b3 = s[level]
        if b3 not in b2.b1:
            b2.b1[b3] = class1()
        b2 = b2.b1[b3]
        b2.common += 1
        a2 = max(a2, b2.common * (level + 1))
    return a2
def fonk5(b8, s):
    b2 = b8
    for ch in s:
        if ch not in b2.b1:
            return 0
        b2 = b2.b1[ch]
    return b2.common
def fonk6(b8, s):
    b2 = b8
    b4 = True
    b5 = False
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
            b4 = False
        b2 = b2.b1[ch]
        if b2.countWord != 0:
            b5 = True
    b2.countWord += 1
    return b4 or b5
def fonk7(b13):
    for i in range(b13):
        b6 = int(input())
        b7 = False
        b8 = class1()
        for _ in range(b6):
            if not b7:
                b7 = fonk6(b8, input())
            else:
                input()
        print('Case {}: {}'.format(i + 1, 'NO' if b7 else 'YES'))
def fonk8(b8, s):
    b2 = b8
    b4 = True
    b5 = False
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
            b4 = False
        b2 = b2.b1[ch]
        if b2.countPassword != 0:
            b5 = True
    b2.countPassword += 1
    return b4 or b5
def fonk9(b6):
    b8 = class1()
    b9 = False
    for i in range(b6):
        if not b9:
            b9 = fonk8(b8, input())
        else:
            input()
    print('vulnerable' if b9 else 'non vulnerable')
def fonk10(b8, s):
    b2 = b8
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
        b2 = b2.b1[ch]
        b2.contactCount += 1
def fonk11(b8, s):
    b2 = b8
    for ch in s:
        if ch not in b2.b1:
            return 0
        b2 = b2.b1[ch]
    return b2.contactCount
def fonk12(b6):
    b8 = class1()
    for i in range(b6):
        b10 = input().split()
        if b10[0] == 'add':
            fonk10(b8, b10[1])
        else:
            print(fonk11(b8, b10[1]))
def fonk13():
    b8 = class1()
    b6, b11 = map(int, input().split())
    for i in range(b6):
        b10 = input().split()
        fonk2(b8, b10[0], int(b10[1]))
    for i in range(b11):
        b12 = input()
        print(fonk3(b8, b12))
    b13 = int(input())
    for k in range(b13):
        b8 = class1()
        a3 = 0
        b6 = int(input())
        for i in range(b6):
            a3 = max(a3, fonk4(b8, input()))
        print('Case {}: {}'.format(k + 1, a3))
    b13 = int(input())
    fonk7(b13)
    b6 = int(input())
    fonk9(b6)
    b6 = int(input())
    fonk12(b6)
if b14 = = "__main__":
    fonk13()
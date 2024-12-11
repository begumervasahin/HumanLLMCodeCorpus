class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.a5 = 0
def fonk2(b6, s, w):
    b2 = b6
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
        b2 = b2.b1[ch]
        if b2.a1 < w:
            b2.a1 = w
def fonk3(b6, s):
    b2 = b6
    for ch in s:
        if ch not in b2.b1:
            return -1
        b2 = b2.b1[ch]
    return b2.a1
def fonk4(b6, s):
    b2 = b6
    a6 = 0
    for level in range(len(s)):
        b3 = s[level]
        if b3 not in b2.b1:
            b2.b1[b3] = class1()
        b2 = b2.b1[b3]
        b2.a2 += 1
        a6 = max(a6, b2.a2 * (level + 1))
    return a6
def fonk5(b13):
    for i in range(b13):
        b4 = int(input())
        b5 = False
        b6 = class1()
        for _ in range(b4):
            if not b5:
                b5 = fonk6(b6, input())
            else:
                input()
        print('Case {}: {}'.format(i + 1, 'NO' if b5 else 'YES'))
def fonk6(b6, s):
    b2 = b6
    b7 = True
    b8 = False
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
            b7 = False
        b2 = b2.b1[ch]
        if b2.a3 != 0:
            b8 = True
    b2.a3 += 1
    return b7 or b8
def fonk7(b6, s):
    b2 = b6
    b7 = True
    b8 = False
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
            b7 = False
        b2 = b2.b1[ch]
        if b2.a4 != 0:
            b8 = True
    b2.a4 += 1
    return b7 or b8
def fonk8(b4):
    b6 = class1()
    b9 = False
    for i in range(b4):
        if not b9:
            b9 = fonk7(b6, input())
        else:
            input()
    print('vulnerable' if b9 else 'non vulnerable')
def fonk9(b6, s):
    b2 = b6
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class1()
        b2 = b2.b1[ch]
        b2.a5 += 1
def fonk10(b6, s):
    b2 = b6
    for ch in s:
        if ch not in b2.b1:
            return 0
        b2 = b2.b1[ch]
    return b2.a5
def fonk11(b4):
    b6 = class1()
    for i in range(b4):
        b10 = input().split()
        if b10[0] == 'add':
            fonk9(b6, b10[1])
        else:
            print(fonk10(b6, b10[1]))
def fonk12():
    b6 = class1()
    b4, b11 = map(int, input().split())
    for i in range(b4):
        b10 = input().split()
        fonk2(b6, b10[0], int(b10[1]))
    for i in range(b11):
        b12 = input()
        print(fonk3(b6, b12))
    b13 = int(input())
    for k in range(b13):
        b6 = class1()
        a7 = 0
        b4 = int(input())
        for i in range(b4):
            a7 = max(a7, fonk4(b6, input()))
        print('Case {}: {}'.format(k + 1, a7))
    b13 = int(input())
    fonk5(b13)
    b4 = int(input())
    fonk8(b4)
    b4 = int(input())
    fonk11(b4)
if b14 = = "__main__":
    fonk12()
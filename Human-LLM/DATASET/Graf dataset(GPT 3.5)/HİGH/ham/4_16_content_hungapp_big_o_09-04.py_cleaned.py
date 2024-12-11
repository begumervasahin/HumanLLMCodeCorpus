class class1:
    def fonk1(self):
        self.b1 = dict()
        self.a1 = 0
def fonk2(b3, s, w):
    b2 = b3
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class5()
        b2 = b2.b1[ch]
        if b2.a1 < w:
            b2.a1 = w
def fonk3(b3, s):
    b2 = b3
    for ch in s:
        if ch not in b2.b1:
            return -1
        b2 = b2.b1[ch]
    return b2.a1
b3 = class5()
b9, b4 = map(int, input().split())
for i in range(b9):
    b5 = list(input().split())
    fonk7(b3, b5[0], int(b5[1]))
for i in range(b4):
    b6 = input()
    print(fonk3(b3, b6))
class class2:
    def fonk4(self):
        self.b1 = dict()
        self.a2 = 0
def fonk5(b3, s):
    b2 = b3
    a3 = 0
    for level in range(len(s)):
        b7 = s[level]
        if b7 not in b2.b1:
            b2.b1[b7] = class5()
        b2 = b2.b1[b7]
        b2.a2 += 1
        a3 = max(a3, b2.a2 * (level + 1))
    return a3
b8 = int(input())
for k in range(b8):
    b3 = class5()
    a4 = 0
    b9 = int(input())
    for i in range(b9):
        a4 = max(a4, fonk7(b3, input()))
    print('Case {}: {}'.format(k + 1, a4))
class class3:
    def fonk6(self):
        self.b1 = dict()
        self.a5 = 0
def fonk7(b3, s):
    b2 = b3
    b10 = True
    b11 = False
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class5()
            b10 = False
        b2 = b2.b1[ch]
        if b2.a5 != 0:
            b11 = True
    b2.a5 += 1
    return b10 or b11
b8 = int(input())
for i in range(b8):
    b9 = int(input())
    b12 = False
    b3 = class5()
    for _ in range(b9):
        if not b12:
            b12 = fonk7(b3, input())
        else:
            input()
    print('Case {}: {}'.format(i + 1, 'NO' if b12 else 'YES'))
class class4:
    def fonk8(self):
        self.b1 = dict()
        self.a6 = 0
def fonk9(b3, s):
    b2 = b3
    b10 = True
    b11 = False
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class5()
            b10 = False
        b2 = b2.b1[ch]
        if b2.a6 != 0:
            b11 = True
    b2.a6 += 1
    return b10 or b11
b9 = int(input())
b3 = class5()
b13 = False
for i in range(b9):
    if not b13:
        b13 = fonk9(b3, input())
    else:
        input()
print('vulnerable' if b13 else 'non vulnerable')
class class5:
    def fonk10(self):
        self.b1 = dict()
        self.a7 = 0
def fonk11(b3, s):
    b2 = b3
    for ch in s:
        if ch not in b2.b1:
            b2.b1[ch] = class5()
        b2 = b2.b1[ch]
        b2.a7 += 1
def fonk12(b3, s):
    b2 = b3
    for ch in s:
        if ch not in b2.b1:
            return 0
        b2 = b2.b1[ch]
    return b2.a7
b9 = int(input())
b3 = class5()
for i in range(b9):
    b5 = list(input().split())
    if b5[0] == 'add':
        fonk11(b3, b5[1])
    else:
        print(fonk12(b3, b5[1]))
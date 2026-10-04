class class1:
    def fonk1(self):
        self.b1 = {}
        self.a1 = 0
def fonk2(b3, word, a1):
    b2 = b3
    for char in word:
        if char not in b2.b1:
            b2.b1[char] = class1()
        b2 = b2.b1[char]
        b2.a1 = max(b2.a1, a1)
def fonk3(b3, prefix):
    b2 = b3
    for char in prefix:
        if char not in b2.b1:
            return -1
        b2 = b2.b1[char]
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
class class2:
    def fonk5(self):
        self.b1 = {}
        self.a2 = 0
def fonk6(b3, word):
    b2 = b3
    a3 = 0
    for level, char in enumerate(word):
        if char not in b2.b1:
            b2.b1[char] = class2()
        b2 = b2.b1[char]
        b2.a2 += 1
        a3 = max(a3, b2.a2 * (level + 1))
    return a3
def fonk7():
    b6 = int(input())
    for case_num in range(b6):
        b3 = class2()
        a3 = 0
        b7 = int(input())
        for _ in range(b7):
            a3 = max(a3, fonk6(b3, input()))
        print(f'Case {case_num + 1}: {a3}')
class class3:
    def fonk8(self):
        self.b1 = {}
        self.a4 = 0
def fonk9(b3, word):
    b2 = b3
    b8 = True
    b9 = False
    for char in word:
        if char not in b2.b1:
            b2.b1[char] = class3()
            b8 = False
        b2 = b2.b1[char]
        if b2.a4 != 0:
            b9 = True
    b2.a4 += 1
    return b8 or b9
def fonk10():
    b6 = int(input())
    for case_num in range(b6):
        b7 = int(input())
        b10 = False
        b3 = class3()
        for _ in range(b7):
            if not b10:
                b10 = fonk9(b3, input())
            else:
                input()
        print(f'Case {case_num + 1}: {"NO" if b10 else "YES"}')
class class4:
    def fonk11(self):
        self.b1 = {}
        self.a5 = 0
def fonk12(b3, password):
    b2 = b3
    b8 = True
    b9 = False
    for char in password:
        if char not in b2.b1:
            b2.b1[char] = class4()
            b8 = False
        b2 = b2.b1[char]
        if b2.a5 != 0:
            b9 = True
    b2.a5 += 1
    return b8 or b9
def fonk13():
    b7 = int(input())
    b3 = class4()
    b11 = False
    for _ in range(b7):
        if not b11:
            b11 = fonk12(b3, input())
        else:
            input()
    print('vulnerable' if b11 else 'non vulnerable')
class class5:
    def fonk14(self):
        self.b1 = {}
        self.a6 = 0
def fonk15(b3, contact):
    b2 = b3
    for char in contact:
        if char not in b2.b1:
            b2.b1[char] = class5()
        b2 = b2.b1[char]
        b2.a6 += 1
def fonk16(b3, prefix):
    b2 = b3
    for char in prefix:
        if char not in b2.b1:
            return 0
        b2 = b2.b1[char]
    return b2.a6
def fonk17():
    b7 = int(input())
    b3 = class5()
    for _ in range(b7):
        b13, b12 = input().split()
        if b13 = = 'add':
            fonk15(b3, b12)
        elif b13 = = 'find':
            print(fonk16(b3, b12))
if b14 = = "__main__":
    fonk17()
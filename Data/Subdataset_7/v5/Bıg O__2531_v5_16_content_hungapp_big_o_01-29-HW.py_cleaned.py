def fonk1(b10, b11, k, b9):
    if b10[k - 1] < b11[-b9]:
        return "YES"
    else:
        return "NO"
def fonk2(b10, b11):
    min_value, b1 = min(b10), max(b11)
    for b6, (b2, y) in enumerate(zip(b10, b11)):
        if b2 = = min_value and y == b1:
            return b6 + 1
    return -1
def fonk3(b10, b11):
    b3 = len(b10)
    b4 = [False] * b3
    b5 = [False] * b3
    b6 = j = 0
    a1 = 0
    while a1 < b3:
        if b10[b6] < b11[j]:
            b4[b6] = True
            b6 += 1
        else:
            b5[j] = True
            j += 1
        a1 += 1
    return b4, b5
def fonk4(b4, b5, b3):
    for b6 in range(b3):
        print(1 if b4[b6] or b6 < b3
    print()
    for b6 in range(b3):
        print(1 if b5[b6] or b6 < b3
def fonk5(b3, b9, b10):
    b7 = [0] * (b9 + 1)
    for genre in b10:
        b7[genre] += 1
    a2 = 0
    for b6 in range(1, b9):
        for j in range(b6 + 1, b9 + 1):
            a2 += b7[b6] * b7[j]
    return a2
na, b8 = map(int, input().split())
k, b9 = map(int, input().split())
b10 = list(map(int, input().split()))
b11 = list(map(int, input().split()))
print(fonk1(b10, b11, k, b9))
print(fonk2(b10, b11))
b4, b5 = fonk3(b10, b11)
fonk4(b4, b5, na)
b3, b9 = map(int, input().split())
b10 = list(map(int, input().split()))
print(fonk5(b3, b9, b10))
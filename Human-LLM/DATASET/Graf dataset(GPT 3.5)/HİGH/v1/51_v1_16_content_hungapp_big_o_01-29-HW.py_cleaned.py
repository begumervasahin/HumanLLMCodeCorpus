
def fonk1():
    na, b1 = map(int, input().split())
    k, b2 = map(int, input().split())
    b3 = list(map(int, input().split()))
    b4 = list(map(int, input().split()))
    if b3[k - 1] < b4[-b2]:
        print("YES")
    else:
        print("NO")
def fonk2():
    b3 = []
    b4 = []
    b5 = int(input())
    for b10 in range(b5):
        x, b6 = map(int, input().split())
        b3.append(x)
        b4.append(b6)
    a1 = -1
    min_value, b7 = min(b3), max(b4)
    for b10 in range(b5):
        if b3[b10] == min_value and b4[b10] == b7:
            a1 = b10 + 1
            break
    print(a1)
def fonk3():
    b5 = int(input())
    b3 = []
    b4 = []
    for b10 in range(b5):
        x, b6 = map(int, input().split())
        b3.append(x)
        b4.append(b6)
    b8 = [False] * b5
    b9 = [False] * b5
    b10 = j = 0
    a2 = 0
    while a2 < b5:
        if b3[b10] < b4[j]:
            b8[b10] = True
            b10 += 1
            a2 += 1
        else:
            b9[j] = True
            j += 1
            a2 += 1
    for b10 in range(b5):
        if b8[b10] or b10 < b5
            print(1, b11 = '')
        else:
            print(0, b11 = '')
    print()
    for b10 in range(b5):
        if b9[b10] or b10 < b5
            print(1, b11 = '')
        else:
            print(0, b11 = '')
def fonk4():
    b5, b2 = map(int, input().split())
    b3 = list(map(int, input().split()))
    b12 = [0] * (b2 + 1)
    for genre in b3:
        b12[genre] += 1
    a3 = 0
    for b10 in range(1, b2):
        for j in range(b10 + 1, b2 + 1):
            a3 += b12[b10] * b12[j]
    print(a3)
def fonk5():
    fonk1()
if b13 = = "__main__":
    fonk5()
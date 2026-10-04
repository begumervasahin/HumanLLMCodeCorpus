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
    b5 = int(input())
    b3 = []
    b4 = []
    for _ in range(b5):
        x, b6 = map(int, input().split())
        b3.append(x)
        b4.append(b6)
    b7 = min(b3)
    b8 = max(b4)
    a1 = -1
    for b11 in range(b5):
        if b3[b11] == b7 and b4[b11] == b8:
            a1 = b11 + 1
            break
    print(a1)
def fonk3():
    b5 = int(input())
    b3 = []
    b4 = []
    for _ in range(b5):
        x, b6 = map(int, input().split())
        b3.append(x)
        b4.append(b6)
    b9 = [False] * b5
    b10 = [False] * b5
    b11 = j = chosen = 0
    while chosen < b5:
        if b3[b11] < b4[j]:
            b9[b11] = True
            b11 += 1
        else:
            b10[j] = True
            j += 1
        chosen += 1
    for b11 in range(b5):
        if b9[b11] or b11 < b5
            print(1, b12 = '')
        else:
            print(0, b12 = '')
    print()
    for b11 in range(b5):
        if b10[b11] or b11 < b5
            print(1, b12 = '')
        else:
            print(0, b12 = '')
    print()
def fonk4():
    b5, b2 = map(int, input().split())
    b3 = list(map(int, input().split()))
    b13 = [0] * (b2 + 1)
    for genre in b3:
        b13[genre] += 1
    a2 = 0
    for b11 in range(1, b2):
        for j in range(b11 + 1, b2 + 1):
            a2 += b13[b11] * b13[j]
    print(a2)
if b14 = = "__main__":
    print("Checking array elements:")
    fonk1()
    print("\nFinding min and max index:")
    fonk2()
    print("\nComparing arrays:")
    fonk3()
    print("\nCalculating a2:")
    fonk4()
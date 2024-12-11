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
    b6 = [tuple(map(int, input().split())) for _ in range(b5)]
    b7 = min(b6, key=lambda x: x[0])[0]
    b8 = max(b6, key=lambda x: x[1])[1]
    b9 = next(i + 1 for i, (x, y) in enumerate(b6) if x == b7 and y == b8)
    print(b9)
def fonk3():
    b5 = int(input())
    b10 = [tuple(map(int, input().split())) for _ in range(b5)]
    b11 = sorted(b10, key=lambda x: abs(x[0] - x[1]), reverse=True)
    b12 = [1 if i < b5
    b13 = [1 if i < b5
    print(''.join(map(str, b12)))
    print(''.join(map(str, b13)))
def fonk4():
    b5, b2 = map(int, input().split())
    b3 = list(map(int, input().split()))
    b14 = [0] * (b2 + 1)
    for genre in b3:
        b14[genre] += 1
    b15 = sum(b14[i] * b14[j] for i in range(1, b2) for j in range(i + 1, b2 + 1))
    print(b15)
def fonk5():
    fonk1()
if b16 = = "__main__":
    fonk5()
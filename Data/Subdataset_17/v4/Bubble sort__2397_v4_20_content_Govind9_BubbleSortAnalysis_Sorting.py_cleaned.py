arr = []
Qmoves = []
Bmoves = []
BBmoves = []
def analyze():
    length = len(Bmoves)
    Q = B = BB = 0
    print("Qsort\tBubble\tBetterBubble")
    for i in range(length):
        print(f"{Qmoves[i]}\t{Bmoves[i]}\t{BBmoves[i]}")
        Q += Qmoves[i]
        B += Bmoves[i]
        BB += BBmoves[i]
    print(f"{Q}\t{B}\t{BB}")
def permute(x):
    if len(x) == len(s):
        p = "".join(s[int(i)] for i in x)
        arr = [int(i) for i in p]
        sort(arr)
    else:
        for i in range(len(s)):
            if str(i) not in x:
                permute(x + str(i))
def sort(arr):
    Bmoves.append(bubble_sort(arr[:]))
    Qmoves.append(qsort(arr[:]))
    BBmoves.append(better_bubble_sort(arr[:]))
    analyze()
def bubble_sort(arr):
    moves = 0
    n = len(arr)
    for j in range(n):
        for i in range(n - 1 - j):
            moves += 1
            if arr[i] > arr[i + 1]:
                moves += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        moves += 1
    return moves
def qsort(arr):
    moves = 0
    n = len(arr)
    for j in range(n):
        swap = False
        for i in range(n - 1 - j):
            moves += 1
            if arr[i] > arr[i + 1]:
                moves += 1
                swap = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not swap:
            break
        moves += 1
    return moves
def better_bubble_sort(arr):
    moves = 0
    n = len(arr)
    for j in range(n):
        flag = False
        for i in range(n - 1 - j):
            moves += 1
            if arr[i] > arr[i + 1]:
                moves += 1
                flag = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not flag:
            break
        moves += 1
    return moves
s = '123456'
permute("")
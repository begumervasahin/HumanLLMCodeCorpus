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
def permute(x, s):
    if len(x) == len(s):
        p = ""
        for i in x:
            p += s[int(i)]
        arr = [int(i) for i in p]
        sort(arr)
    else:
        for i in range(len(s)):
            if str(i) not in x:
                permute(x + str(i), s)
def sort(arr):
    a = arr[:]
    Bmoves.append(Bubble(a))
    a = arr[:]
    Qmoves.append(Qsort(a))
    a = arr[:]
    BBmoves.append(BetterBubble(a))
    analyze()
def Bubble(arr):
    moves = 0
    for j in range(len(arr)):
        for i in range(len(arr) - 1 - j):
            moves += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                moves += 2
    return moves
def Qsort(arr):
    moves = 0
    for j in range(len(arr)):
        swap = 0
        for i in range(len(arr) - 1 - j):
            moves += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                moves += 2
                swap += 1
        if swap < 2:
            break
    return moves
def BetterBubble(arr):
    moves = 0
    for j in range(len(arr)):
        flag = False
        for i in range(len(arr) - 1 - j):
            moves += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                moves += 2
                flag = True
        if not flag:
            break
    return moves
s = '123456'
permute("", s)
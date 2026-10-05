arr = []
Qmoves = []
Bmoves = []
BBmoves = []
def analyze():
    length = len(Bmoves)
    Q = B = BB = 0
    print("Qsort\tBubble\tBetterBubble")
    for i in range(length):
        print(str(Qmoves[i]) + "\t" + str(Bmoves[i]) + "\t" + str(BBmoves[i]))
        Q += Qmoves[i]
        B += Bmoves[i]
        BB += BBmoves[i]
    print(str(Q) + "\t" + str(B) + "\t" + str(BB))
def permute(x):
    global arr
    if len(x) == len(s):
        p = "".join(s[int(i)] for i in x)
        arr = [int(i) for i in p]
        sort(arr)
    for i in range(len(s)):
        if str(i) not in x:
            permute(x + str(i))
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
        moves += 1
        for i in range(len(arr) - 1 - j):
            moves += 2
            if arr[i] > arr[i + 1]:
                moves += 2
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return moves
def Qsort(arr):
    moves = 0
    for j in range(len(arr)):
        moves += 3
        swap = 0
        for i in range(len(arr) - 1 - j):
            moves += 2
            if arr[i] > arr[i + 1]:
                moves += 2
                swap += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if swap < 2:
            break
    return moves
def BetterBubble(arr):
    moves = 0
    for j in range(len(arr)):
        moves += 3
        flag = False
        for i in range(len(arr) - 1 - j):
            moves += 2
            if arr[i] > arr[i + 1]:
                moves += 2
                flag = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not flag:
            break
    return moves
s = '123456'
permute("")
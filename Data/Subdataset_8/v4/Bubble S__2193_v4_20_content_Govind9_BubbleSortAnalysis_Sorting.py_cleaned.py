
Qmoves = []
Bmoves = []
BBmoves = []
def analyze():
    length = len(Bmoves)
    Q_total = sum(Qmoves)
    B_total = sum(Bmoves)
    BB_total = sum(BBmoves)
    print("Qsort\tBubble\tBetterBubble")
    for i in range(length):
        print(f"{Qmoves[i]}\t{Bmoves[i]}\t{BBmoves[i]}")
    print(f"{Q_total}\t{B_total}\t{BB_total}")
def permute(x):
    arr = []
    if len(x) == len(s):
        p = "".join(s[int(i)] for i in x)
        for i in p:
            arr.append(int(i))
        sort(arr)
    for i in range(len(s)):
        if str(i) not in x:
            permute(x + str(i))
def sort(arr):
    Bmoves.append(Bubble(arr))
    Qmoves.append(Qsort(arr))
    BBmoves.append(BetterBubble(arr))
    analyze()
def Bubble(arr):
    moves = 0
    for j in range(len(arr)):
        moves += 3
        for i in range(len(arr) - 1 - j):
            moves += 2
            if arr[i] > arr[i + 1]:
                moves += 2
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
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
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
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
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        if not flag:
            break
    return moves
s = '123456'
permute("")
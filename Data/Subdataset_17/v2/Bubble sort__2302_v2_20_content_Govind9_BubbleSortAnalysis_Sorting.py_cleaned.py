
arr = []
Qmoves = []
Bmoves = []
BBmoves = []
def analyze():
    length = len(Bmoves)
    total_Q = total_B = total_BB = 0
    print("Qsort\tBubble\tBetterBubble")
    for i in range(length):
        print(f"{Qmoves[i]}\t{Bmoves[i]}\t{BBmoves[i]}")
        total_Q += Qmoves[i]
        total_B += Bmoves[i]
        total_BB += BBmoves[i]
    print(f"{total_Q}\t{total_B}\t{total_BB}")
def permute(x, s):
    if len(x) == len(s):
        p = "".join(s[int(i)] for i in x)
        arr = [int(i) for i in p]
        sort(arr)
    else:
        for i in range(len(s)):
            if str(i) not in x:
                permute(x + str(i), s)
def sort(arr):
    arr_copy = arr[:]
    Bmoves.append(bubble_sort(arr_copy))
    arr_copy = arr[:]
    Qmoves.append(quick_sort(arr_copy))
    arr_copy = arr[:]
    BBmoves.append(better_bubble_sort(arr_copy))
    analyze()
def bubble_sort(arr):
    moves = 0
    for j in range(len(arr)):
        for i in range(len(arr) - 1 - j):
            moves += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                moves += 2
    return moves
def quick_sort(arr):
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
def better_bubble_sort(arr):
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
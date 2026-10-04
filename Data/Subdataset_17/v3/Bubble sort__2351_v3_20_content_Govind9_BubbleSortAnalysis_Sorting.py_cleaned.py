
permutations = []
quick_sort_moves = []
bubble_sort_moves = []
better_bubble_sort_moves = []
def analyze():
    length = len(bubble_sort_moves)
    total_quick_sort = total_bubble_sort = total_better_bubble_sort = 0
    print("QuickSort\tBubbleSort\tBetterBubbleSort")
    for i in range(length):
        print(f"{quick_sort_moves[i]}\t\t{bubble_sort_moves[i]}\t\t{better_bubble_sort_moves[i]}")
        total_quick_sort += quick_sort_moves[i]
        total_bubble_sort += bubble_sort_moves[i]
        total_better_bubble_sort += better_bubble_sort_moves[i]
    print(f"{total_quick_sort}\t\t{total_bubble_sort}\t\t{total_better_bubble_sort}")
def permute(prefix, s):
    if len(prefix) == len(s):
        permutation = [int(s[int(i)]) for i in prefix]
        sort(permutation)
    else:
        for i in range(len(s)):
            if str(i) not in prefix:
                permute(prefix + str(i), s)
def sort(arr):
    arr_copy = arr[:]
    bubble_sort_moves.append(bubble_sort(arr_copy))
    arr_copy = arr[:]
    quick_sort_moves.append(quick_sort(arr_copy))
    arr_copy = arr[:]
    better_bubble_sort_moves.append(better_bubble_sort(arr_copy))
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
        swap_count = 0
        for i in range(len(arr) - 1 - j):
            moves += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                moves += 2
                swap_count += 1
        if swap_count < 2:
            break
    return moves
def better_bubble_sort(arr):
    moves = 0
    for j in range(len(arr)):
        swapped = False
        for i in range(len(arr) - 1 - j):
            moves += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                moves += 2
                swapped = True
        if not swapped:
            break
    return moves
input_string = '123456'
permute("", input_string)
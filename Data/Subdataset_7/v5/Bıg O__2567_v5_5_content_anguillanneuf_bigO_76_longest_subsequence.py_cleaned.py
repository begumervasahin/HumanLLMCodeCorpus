def fonk1(arr):
    if len(arr) < 2:
        return arr
    b1 = [None] * len(arr)
    b2 = [None] * len(arr)
    a1 = 1
    b1[0] = 0
    b3 = []
    for i in range(1, len(arr)):
        if arr[i] > arr[b1[a1 - 1]]:
            b4 = a1
        else:
            a2 = 0
            b5 = a1 - 1
            while a2 + 1 < b5:
                b6 = (a2 + b5)
                if arr[i] > arr[b1[b6]]:
                    a2 = b6 + 1
                else:
                    b5 = b6
            b4 = a2
        b2[i] = b1[b4 - 1]
        b1[b4] = i
        a1 = max(a1, b4 + 1)
    b7 = b1[a1 - 1]
    for _ in range(a1):
        b3.append(arr[b7])
        b7 = b2[b7]
    return b3[::-1]
def fonk2(arr):
    b8 = [[] for _ in range(len(arr))]
    b9 = []
    for i in range(len(arr)):
        b10 = False
        for b4 in range(i):
            if arr[i] > b8[b4][-1]:
                b10 = True
                b8[i] = b8[b4] + [arr[i]]
                b9 = max(b8[i], b9, key=len)
        if not b10:
            b8[i].append(arr[i])
    return b9
b11 = [30, 10, 20, 50, 40, 60]
print("Longest Increasing Subsequence (O(n log n)):", fonk1(b11))
b12 = [80, 90, 91, 81, 82, 83, 74, 85]
print("Longest Increasing Subsequence (O(n^2)):", fonk2(b12))
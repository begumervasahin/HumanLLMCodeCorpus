def fonk1(arr):
    if len(arr) < 2:
        return arr
    b1 = [None] * len(arr)
    b2 = [None] * len(arr)
    a1 = 1
    b3 = []
    b1[0] = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[b1[a1 - 1]]:
            b4 = a1
        else:
            b7, b5 = 0, a1 - 1
            while b7 + 1 < b5:
                b6 = (b7 + b5)
                if arr[i] > arr[b1[b6]]:
                    b7 = b6 + 1
                else:
                    b5 = b6
            b4 = b7
        b2[i] = b1[b4 - 1]
        b1[b4] = i
        a1 = max(a1, b4 + 1)
    b8 = b1[a1 - 1]
    for _ in range(a1):
        b3.append(arr[b8])
        b8 = b2[b8]
    return b3[::-1]
def fonk2(arr):
    b9 = [[] for _ in range(len(arr))]
    b10 = []
    for i in range(len(arr)):
        for b4 in range(i):
            if arr[i] > b9[b4][-1]:
                b9[i] = b9[b4] + [arr[i]]
                b10 = max(b9[i], b10, key=len)
        if not b9[i]:
            b9[i].append(arr[i])
    return b10
b11 = [30, 10, 20, 50, 40, 60]
b12 = [80, 90, 91, 81, 82, 83, 74, 85]
print("Longest increasing subsequence (O(n log n)): ", fonk1(b11))
print("Longest increasing subsequence (O(n^2)): ", fonk2(b12))
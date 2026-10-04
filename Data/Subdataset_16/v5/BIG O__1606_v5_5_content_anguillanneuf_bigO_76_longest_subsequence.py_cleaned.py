
def fonk1(arr):
    if len(arr) < 2:
        return arr
    b1 = [None] * len(arr)
    b2 = [None] * len(arr)
    a1 = 1
    b1[0] = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[b1[a1 - 1]]:
            b3 = a1
        else:
            b6, b4 = 0, a1 - 1
            while b6 + 1 < b4:
                b5 = (b6 + b4)
                if arr[i] > arr[b1[b5]]:
                    b6 = b5 + 1
                else:
                    b4 = b5
            b3 = b6
        b2[i] = b1[b3 - 1]
        b1[b3] = i
        a1 = max(a1, b3 + 1)
    b7 = []
    b8 = b1[a1 - 1]
    for _ in range(a1):
        b7.append(arr[b8])
        b8 = b2[b8]
    return b7[::-1]
def fonk2(arr):
    if not arr:
        return []
    b9 = [[] for _ in range(len(arr))]
    b10 = []
    for i in range(len(arr)):
        for b3 in range(i):
            if arr[i] > arr[b3]:
                if len(b9[b3]) + 1 > len(b9[i]):
                    b9[i] = b9[b3] + [arr[i]]
                    b10 = max(b9[i], b10, key=len)
        if not b9[i]:
            b9[i] = [arr[i]]
            b10 = max(b9[i], b10, key=len)
    return b10
if b11 = = "__main__":
    b12 = [30, 10, 20, 50, 40, 60]
    print("Longest increasing subsequence (O(n log n)):", fonk1(b12))
    b13 = [80, 90, 91, 81, 82, 83, 74, 85]
    print("Longest increasing subsequence (O(n^2)):", fonk2(b13))
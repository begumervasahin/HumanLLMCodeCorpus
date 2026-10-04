def fonk1(arr):
    if len(arr) < 2:
        return arr
    b1 = [None] * len(arr)
    b2 = [None] * len(arr)
    a1 = 1
    b1[0] = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[b1[a1-1]]:
            b3 = a1
        else:
            b6, b4 = 0, a1 - 1
            while b6 < b4:
                b5 = (b6 + b4)
                if arr[i] > arr[b1[b5]]:
                    b6 = b5 + 1
                else:
                    b4 = b5
            b3 = b6
        b2[i] = b1[b3-1] if b3 > 0 else None
        b1[b3] = i
        if b3 + 1 > a1:
            a1 = b3 + 1
    b7 = b1[a1-1]
    b8 = []
    for _ in range(a1):
        b8.append(arr[b7])
        b7 = b2[b7]
    return b8[::-1]
def fonk2(arr):
    if not arr:
        return []
    b9 = [[] for _ in range(len(arr))]
    b10 = []
    for i in range(len(arr)):
        for b3 in range(i):
            if arr[i] > arr[b3] and len(b9[b3]) + 1 > len(b9[i]):
                b9[i] = b9[b3] + [arr[i]]
        if not b9[i]:
            b9[i].append(arr[i])
        if len(b9[i]) > len(b10):
            b10 = b9[i]
    return b10
if b11 = = "__main__":
    b12 = [30, 10, 20, 50, 40, 60]
    print("Longest increasing subsequence using O(n log n) approach:")
    print(fonk1(b12))
    b13 = [80, 90, 91, 81, 82, 83, 74, 85]
    print("\nLongest increasing subsequence using O(n^2) approach:")
    print(fonk2(b13))
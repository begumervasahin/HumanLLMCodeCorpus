def fonk1(arr, b1 = 0, desc=False):
    if not arr:
        return []
    b2 = min(arr)
    b3 = max(arr)
    b4 = [x - b2 for x in arr] if b2 < 0 else arr
    if b1:
        print("Normalized array:", b4)
    b5 = b3 - b2 + 1
    b6 = [0] * b5
    for number in b4:
        b6[number] += 1
    for i in range(1, b5):
        b6[i] += b6[i - 1]
        if b1 = = 2:
            print(f"Cumulative b6 at index {i}: {b6}")
    b7 = [0] * len(arr)
    for number in reversed(b4):
        b6[number] -= 1
        b7[b6[number]] = number
    b8 = [x + b2 for x in b7] if b2 < 0 else b7
    if desc:
        b8.reverse()
    return b8
if b9 = = "__main__":
    b10 = [4, 2, 2, 8, 3, 3, 1]
    b11 = fonk1(b10, b1=1)
    print("Sorted array:", b11)
def fonk1(arr, b1 = 0, desc=0):
    if not arr:
        return []
    b2 = min(arr)
    b3 = max(arr)
    b4 = [x - b2 for x in arr]
    if b1:
        print("Normalized array:", b4)
    b5 = b3 - b2 + 1
    b6 = [0] * b5
    for num in b4:
        b6[num] += 1
    for i in range(1, b5):
        b6[i] += b6[i - 1]
        if b1 = = 2:
            print(f"Cumulative b6 at index {i}: {b6[i]}")
    b7 = [0] * len(arr)
    for num in reversed(b4):
        b6[num] -= 1
        b7[b6[num]] = num
    if b1:
        print("Sorted b7 (before denormalization):", b7)
    b8 = [x + b2 for x in b7]
    if desc:
        b8.reverse()
    return b8
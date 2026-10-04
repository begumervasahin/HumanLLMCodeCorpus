def fonk1(arr, b1 = 0, desc=0):
    b2 = min(arr)
    b3 = max(arr)
    if b2 < 0:
        b4 = [x - b2 for x in arr]
    else:
        b4 = arr.copy()
    if b1:
        print("Normalized array:", b4)
    b5 = [0] * (b3 - b2 + 1)
    for num in b4:
        b5[num] += 1
    for i in range(1, len(b5)):
        b5[i] += b5[i - 1]
        if b1 = = 2:
            print(f"Cumulative b5 at index {i}: {b5[i]}")
    b6 = [0] * len(arr)
    for num in reversed(b4):
        b5[num] -= 1
        b6[b5[num]] = num
    if b1:
        print("Sorted b6 (before denormalization):", b6)
    if b2 < 0:
        b6 = [x + b2 for x in b6]
    if desc:
        b6.reverse()
    return b6
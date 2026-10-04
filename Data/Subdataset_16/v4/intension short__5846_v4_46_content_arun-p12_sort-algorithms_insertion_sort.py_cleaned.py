def fonk1(arr, b1 = 0, desc=False):
    b2 = len(arr)
    for i in range(1, b2):
        b3 = arr[i]
        b4 = i - 1
        while b4 >= 0 and arr[b4] > b3:
            arr[b4 + 1] = arr[b4]
            b4 -= 1
            if b1 = = 2:
                print(f"  Subarray after shifting: {arr}")
        arr[b4 + 1] = b3
        if b1 >= 1:
            print(f"Iteration {i}: {arr}")
    if desc:
        arr.reverse()
    return arr
def fonk1(arr, b1 = 0, desc=False):
    for i in range(1, len(arr)):
        b2 = arr[i]
        b3 = i - 1
        while b3 >= 0 and arr[b3] > b2:
            arr[b3 + 1] = arr[b3]
            b3 -= 1
            if b1 = = 2:
                print(f"  Subarray after shifting: {arr}")
        arr[b3 + 1] = b2
        if b1 >= 1:
            print(f"Iteration {i}: {arr}")
    if desc:
        arr.reverse()
    return arr
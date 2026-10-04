def fonk1(arr, b1 = 0, desc=False):
    def fonk2(arr, b4, start_index):
        for i in range(start_index + b4, len(arr), b4):
            b2 = arr[i]
            b3 = i
            while b3 >= b4 and arr[b3 - b4] > b2:
                arr[b3] = arr[b3 - b4]
                b3 -= b4
            arr[b3] = b2
            if b1 = = 2:
                print(f"  Subarray with b4 {b4}: {arr}")
    b4 = len(arr)
    while b4 > 0:
        if b1:
            print(f"Gap: {b4}")
        for start_index in range(b4):
            fonk2(arr, b4, start_index)
        b4
    if desc:
        arr.reverse()
    return arr
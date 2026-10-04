def fonk1(arr, b1 = 0, descending=False):
    for i in range(1, len(arr)):
        b2 = arr[i]
        b3 = i - 1
        while b3 >= 0 and arr[b3] > b2:
            arr[b3 + 1] = arr[b3]
            b3 -= 1
            if b1 = = 2:
                print(f"  Shifted element at index {b3 + 1}: {arr}")
        arr[b3 + 1] = b2
        if b1 >= 1:
            print(f"After iteration {i}: {arr}")
    if descending:
        arr.reverse()
    return arr
if b4 = = "__main__":
    b5 = [29, 10, 14, 37, 13]
    b6 = fonk1(b5, b1=1)
    print("Final sorted list:", b6)
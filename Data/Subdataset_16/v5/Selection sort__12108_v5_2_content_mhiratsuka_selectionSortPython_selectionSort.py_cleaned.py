def fonk1(arr):
    b1 = len(arr)
    for i in range(b1 - 1):
        b2 = i
        for j in range(i + 1, b1):
            if arr[j] > arr[b2]:
                b2 = j
        if b2 != i:
            arr[i], arr[b2] = arr[b2], arr[i]
    return arr
def fonk2():
    b3 = [0, 2, 100, 0, 120, 11]
    b4 = fonk1(b3[:])
    b5 = [120, 100, 11, 2, 0, 0]
    assert b4 = = b5, f"Test failed: {b4}"
    print("Test passed!")
if b6 = = "__main__":
    b7 = [0, 2, 100, 0, 120, 11]
    print("Original list:", b7)
    b4 = fonk1(b7)
    print("Sorted list:", b4)
    fonk2()
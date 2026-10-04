def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = arr[0]
    b2 = [x for x in arr if x < b1]
    b3 = [x for x in arr if x == b1]
    b4 = [x for x in arr if x > b1]
    b5 = fonk1(b2)
    b6 = fonk1(b4)
    b7 = b5 + b3 + b6
    return b7
if b8 = = "__main__":
    b9 = fonk1([1, 3, 5, 2])
    print("Sorted list:", b9)
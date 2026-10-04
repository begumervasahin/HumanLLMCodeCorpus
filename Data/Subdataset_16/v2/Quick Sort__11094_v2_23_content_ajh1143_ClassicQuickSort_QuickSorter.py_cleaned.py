def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = arr[0]
    b2 = [x for x in arr if x < b1]
    b3 = [x for x in arr if x == b1]
    b4 = [x for x in arr if x > b1]
    b5 = fonk1(b2)
    b6 = fonk1(b4)
    return b5 + b3 + b6
if b7 = = "__main__":
    b8 = [1, 3, 5, 2]
    b9 = fonk1(b8)
    print(b9)

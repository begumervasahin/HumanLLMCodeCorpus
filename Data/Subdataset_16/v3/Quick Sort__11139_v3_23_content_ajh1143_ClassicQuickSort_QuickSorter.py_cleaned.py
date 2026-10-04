def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = arr[0]
    b2 = [x for x in arr if x < b1]
    b3 = [x for x in arr if x == b1]
    b4 = [x for x in arr if x > b1]
    return fonk1(b2) + b3 + fonk1(b4)
if b5 = = "__main__":
    b6 = [1, 3, 5, 2]
    b7 = fonk1(b6)
    print(b7)

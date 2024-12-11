def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = arr[0]
    b2 = [i for i in arr if i < b1]
    b3 = [i for i in arr if i == b1]
    b4 = [i for i in arr if i > b1]
    return fonk1(b2) + b3 + fonk1(b4)
b5 = fonk1([1, 3, 5, 2])
print(b5)
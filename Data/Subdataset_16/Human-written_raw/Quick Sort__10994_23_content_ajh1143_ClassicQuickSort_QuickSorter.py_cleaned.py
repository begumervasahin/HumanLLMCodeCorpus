def fonk1(arr):
    b1 = []
    b2 = []
    b3 = []
    if len(arr) <= 1:
        return arr
    else:
        b4 = arr[0]
        for i in arr:
            if i < b4:
                b3.append(i)
            elif i > b4:
                b2.append(i)
            else:
                b1.append(i)
        b5 = fonk1(b3)
        b6 = fonk1(b2)
        b7 = (b5+b1+b6)
    return b7
b8 = fonk1([1,3,5,2])
print(b8)
import sys
def fonk1(a, b):
    b1 = []
    while a and b:
        if a[0] > b[0]:
            b1.append(b.pop(0))
        else:
            b1.append(a.pop(0))
    while a:
        b1.append(a.pop(0))
    while b:
        b1.append(b.pop(0))
    return b1
def fonk2(arr):
    if len(arr) == 1:
        return arr
    b2 = len(arr)
    b3 = arr[:b2]
    b4 = arr[b2:]
    b3 = fonk2(b3)
    b4 = fonk2(b4)
    return fonk1(b3, b4)
if len(sys.argv) > 1:
    b5 = sys.argv[1].split()
    b5 = [int(num) for num in b5]
    print("Input list:", b5)
    b6 = fonk2(b5)
    print("Sorted list:", b6)
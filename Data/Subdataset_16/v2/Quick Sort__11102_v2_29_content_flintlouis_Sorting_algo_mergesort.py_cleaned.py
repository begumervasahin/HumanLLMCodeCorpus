import sys
def fonk1(left, right):
    b1 = []
    while left and right:
        if left[0] > right[0]:
            b1.append(right.pop(0))
        else:
            b1.append(left.pop(0))
    while left:
        b1.append(left.pop(0))
    while right:
        b1.append(right.pop(0))
    return b1
def fonk2(lst):
    if len(lst) <= 1:
        return lst
    b2 = len(lst)
    b3 = lst[:b2]
    b4 = lst[b2:]
    b3 = fonk2(b3)
    b4 = fonk2(b4)
    return fonk1(b3, b4)
def fonk3():
    if len(sys.argv) > 1:
        b5 = sys.argv[1:]
        b5 = [int(x) for x in b5]
        print("Original list:", b5)
        b6 = fonk2(b5)
        print("Sorted list:", b6)
    else:
        print("Please provide a list of numbers as command-line arguments.")
if b7 = = "__main__":
    fonk3()
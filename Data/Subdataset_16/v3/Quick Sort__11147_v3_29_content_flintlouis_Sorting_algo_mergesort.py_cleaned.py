import sys
def fonk1(left, right):
    b1 = []
    while left and right:
        if left[0] <= right[0]:
            b1.append(left.pop(0))
        else:
            b1.append(right.pop(0))
    b1.extend(left)
    b1.extend(right)
    return b1
def fonk2(lst):
    if len(lst) <= 1:
        return lst
    b2 = len(lst)
    b3 = fonk2(lst[:b2])
    b4 = fonk2(lst[b2:])
    return fonk1(b3, b4)
def fonk3():
    if len(sys.argv) > 1:
        try:
            b5 = [int(x) for x in sys.argv[1:]]
            print("Original list:", b5)
            b6 = fonk2(b5)
            print("Sorted list:", b6)
        except ValueError:
            print("Please provide a valid list of integers.")
    else:
        print("Usage: python script.py <num1> <num2> ... <numN>")
if b7 = = "__main__":
    fonk3()
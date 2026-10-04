def fonk1(A):
    if not isinstance(A, list) or len(A) == 0:
        print("List expected. Got:", A)
        exit(1)
    b2, b1 = A[0], 0
    for i in range(1, len(A)):
        if A[i] < b2:
            b2 = A[i]
            b1 = i
    return (b2, b1)
def fonk2(A):
    if not isinstance(A, list) or len(A) == 0:
        print("List expected. Got:", A)
        exit(1)
    b3, b1 = A[0], 0
    for i in range(1, len(A)):
        if A[i] > b3:
            b3 = A[i]
            b1 = i
    return (b3, b1)
def fonk3(b9, b8):
    return b8, b9
if b4 = = "__main__":
    b5 = [64, 25, 12, 22, 11]
    b2, b6 = fonk1(b5)
    print(f"Minimum value: {b2} at b1 {b6}")
    b3, b7 = fonk2(b5)
    print(f"Maximum value: {b3} at b1 {b7}")
    b9, b8 = 5, 10
    b9, b8 = fonk3(b9, b8)
    print(f"Swapped values: b9 = {b9}, b8 = {b8}")
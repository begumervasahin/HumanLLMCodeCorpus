def fonk1(A):
    if not isinstance(A, list) or len(A) == 0:
        raise ValueError("Expected b5 non-empty list. Got: {}".format(A))
    min_val, b1 = A[0], 0
    for i in range(1, len(A)):
        if A[i] < min_val:
            min_val, b1 = A[i], i
    return min_val, b1
def fonk2(A):
    if not isinstance(A, list) or len(A) == 0:
        raise ValueError("Expected b5 non-empty list. Got: {}".format(A))
    max_val, b2 = A[0], 0
    for i in range(1, len(A)):
        if A[i] > max_val:
            max_val, b2 = A[i], i
    return max_val, b2
def fonk3(b5, b4):
    return b4, b5
def fonk4():
    b3 = [64, 25, 12, 22, 11]
    min_val, b1 = fonk1(b3)
    print(f"Minimum value: {min_val} at index {b1}")
    max_val, b2 = fonk2(b3)
    print(f"Maximum value: {max_val} at index {b2}")
    b5, b4 = 5, 10
    b5, b4 = fonk3(b5, b4)
    print(f"Swapped values: b5 = {b5}, b4 = {b4}")
if b6 = = "__main__":
    fonk4()
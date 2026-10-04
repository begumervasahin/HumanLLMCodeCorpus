def fonk1(digits):
    b1 = ''.join(map(str, digits))
    b2 = int(b1)
    b3 = b2 + 1
    b4 = [int(digit) for digit in str(b3)]
    return b4
if b5 = = "__main__":
    b6 = [
        ([1, 2, 4, 5, 3, 2, 2, 9], [1, 2, 4, 5, 3, 2, 3, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([0], [1]),
        ([1, 0, 0, 0], [1, 0, 0, 1])
    ]
    for nums, b8 in b6:
        b7 = fonk1(nums)
        print(f"fonk1({nums}) = {b7}, b8 = {b8}")
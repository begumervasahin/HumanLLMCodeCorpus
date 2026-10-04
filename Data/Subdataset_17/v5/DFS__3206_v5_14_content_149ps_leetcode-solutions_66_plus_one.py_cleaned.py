def plus_one(digits):
    number_str = ''.join(map(str, digits))
    number = int(number_str)
    incremented_number = number + 1
    incremented_digits = [int(digit) for digit in str(incremented_number)]
    return incremented_digits
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4, 5, 3, 2, 2, 9], [1, 2, 4, 5, 3, 2, 3, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([0], [1]),
        ([1, 0, 0, 0], [1, 0, 0, 1])
    ]
    for nums, expected in test_cases:
        result = plus_one(nums)
        print(f"plus_one({nums}) = {result}, expected = {expected}")
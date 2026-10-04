def find_minimum(A):
    if not isinstance(A, list) or len(A) == 0:
        raise ValueError("Expected a non-empty list. Got: {}".format(A))
    min_val, min_index = A[0], 0
    for i in range(1, len(A)):
        if A[i] < min_val:
            min_val, min_index = A[i], i
    return min_val, min_index
def find_maximum(A):
    if not isinstance(A, list) or len(A) == 0:
        raise ValueError("Expected a non-empty list. Got: {}".format(A))
    max_val, max_index = A[0], 0
    for i in range(1, len(A)):
        if A[i] > max_val:
            max_val, max_index = A[i], i
    return max_val, max_index
def swap(a, b):
    return b, a
def main():
    sample_list = [64, 25, 12, 22, 11]
    min_val, min_index = find_minimum(sample_list)
    print(f"Minimum value: {min_val} at index {min_index}")
    max_val, max_index = find_maximum(sample_list)
    print(f"Maximum value: {max_val} at index {max_index}")
    a, b = 5, 10
    a, b = swap(a, b)
    print(f"Swapped values: a = {a}, b = {b}")
if __name__ == "__main__":
    main()
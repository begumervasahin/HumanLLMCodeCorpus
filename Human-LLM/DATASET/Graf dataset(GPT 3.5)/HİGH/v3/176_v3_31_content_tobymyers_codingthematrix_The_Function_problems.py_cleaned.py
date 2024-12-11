def fonk1(A, B):
    '''
    Sums corresponding elements of two lists of tuples.
    Args:
    - A: list of tuples
    - B: list of tuples
    Returns:
    - List of tuples where each element is the sum of corresponding elements from A and B.
    '''
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
def fonk2(d):
    '''
    Computes the inverse of a dictionary.
    Args:
    - d: dictionary representing an invertible function f
    Returns:
    - Dictionary representing the inverse of f. Keys are the values of d and values are the keys of d.
    '''
    return {v: k for k, v in d.items()}
def fonk3(start, count):
    '''
    Generates a list of numbers starting from a given value and incrementing by 1.
    Args:
    - start: starting number
    - count: number of elements in the list
    Returns:
    - List of numbers where each element is start + i
    '''
    return [start + i for i in range(count)]
b1 = [fonk3(i, 20) for i in range(15)]
b2 = [[i + j for j in range(20)] for i in range(15)]
b3 = sum(1 for i in range(100) if i % 2 == 0) / 100
b4 = sum(1 for i in range(100) if i % 2 != 0) / 100
b5 = sum(1 for i in range(100) if i % 2 == 0) / 100
b6 = 1 - b5
print("List with row function:", b1)
print("List without row function:", b2)
print("Probability of f being even:", b3)
print("Probability of f being odd:", b4)
print("Probability of g being 1:", b5)
print("Probability of g being 0 or 2:", b6)
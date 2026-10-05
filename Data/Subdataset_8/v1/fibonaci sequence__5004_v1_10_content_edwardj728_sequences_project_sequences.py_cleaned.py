def check_arithmetic(sequence):
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] != sequence[i] + (sequence[i] - sequence[i - 1]):
            return False
    return True
def check_geometric(sequence):
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] != sequence[i] * 2:
            return False
    return True
def check_quadratic(sequence):
    if len(sequence) < 3:
        return False
    diff1 = sequence[1] - sequence[0]
    diff2 = sequence[2] - sequence[1]
    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i - 1] + diff2:
            return False
    return True
def check_cubic(sequence):
    if len(sequence) < 4:
        return False
    diff1 = sequence[1] - sequence[0]
    diff2 = sequence[2] - sequence[1]
    diff3 = sequence[3] - sequence[2]
    ratio1 = diff2 - diff1
    ratio2 = diff3 - diff2
    return ratio1 == ratio2
def check_fibonacci(sequence):
    if len(sequence) < 4:
        return False
    for i in range(2, len(sequence) - 1):
        if sequence[i] != sequence[i - 1] + sequence[i - 2]:
            return False
    return True
user_input = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
list_input = user_input.split(",")
list_int = list(map(int, list_input))
if check_arithmetic(list_int):
    print("Arithmetic Sequence")
if check_geometric(list_int):
    print("Geometric Sequence")
if check_quadratic(list_int):
    print("Quadratic Sequence")
if check_cubic(list_int):
    print("Cubic Sequence")
if check_fibonacci(list_int):
    print("Fibonacci Sequence")
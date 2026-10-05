
user_input = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
sequence = list(map(int, user_input.split(",")))
if sequence[1] == sequence[0] + (sequence[1] - sequence[0]) and sequence[2] == sequence[1] + (sequence[1] - sequence[0]):
    print("Arithmetic Sequence")
if sequence[1] == sequence[0] * 2 and sequence[2] == sequence[1] * 2 and sequence[3] == sequence[2] * 2:
    print("Geometric Sequence")
diff1 = sequence[1] - sequence[0]
diff2 = sequence[2] - sequence[1]
if sequence[1] == sequence[0] + diff1 and sequence[2] == sequence[1] + diff2:
    print("Quadratic Sequence")
diff3 = sequence[3] - sequence[2]
if diff3 - diff2 == diff2 - diff1:
    print("Cubic Sequence")
if sequence[2] == sequence[0] + sequence[1] and sequence[3] == sequence[1] + sequence[2]:
    print("Fibonacci Sequence")
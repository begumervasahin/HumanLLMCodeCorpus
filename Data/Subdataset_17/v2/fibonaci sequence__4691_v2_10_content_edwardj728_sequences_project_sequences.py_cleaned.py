def main():
    user_input = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
    list_input = user_input.split(",")
    list_int = list(map(int, list_input))
    if len(list_int) != 5:
        print("Please enter exactly 5 integers.")
        return
    arithmetic_diff = list_int[1] - list_int[0]
    is_arithmetic = all(list_int[i] == list_int[i - 1] + arithmetic_diff for i in range(1, 5))
    if is_arithmetic:
        print("Arithmetic Sequence")
    geometric_ratio = list_int[1]
    is_geometric = geometric_ratio is not None and all(list_int[i] == list_int[i - 1] * geometric_ratio for i in range(1, 5))
    if is_geometric:
        print("Geometric Sequence")
    first_diff = [list_int[i] - list_int[i - 1] for i in range(1, 5)]
    second_diff = [first_diff[i] - first_diff[i - 1] for i in range(1, 4)]
    is_quadratic = all(second_diff[i] == second_diff[0] for i in range(1, 3))
    if is_quadratic:
        print("Quadratic Sequence")
    third_diff = [second_diff[i] - second_diff[i - 1] for i in range(1, 3)]
    is_cubic = all(third_diff[i] == third_diff[0] for i in range(1, 2))
    if is_cubic:
        print("Cubic Sequence")
    is_fibonacci = all(list_int[i] == list_int[i - 1] + list_int[i - 2] for i in range(2, 5))
    if is_fibonacci:
        print("Fibonacci Sequence")
if __name__ == "__main__":
    main()
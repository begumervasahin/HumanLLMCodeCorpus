def find_special_numbers(n):
    special_numbers = []
    max_i = int((1000000000000000000 / 24)**0.5)
    for i in range(1, max_i + 1):
        potential_special = (24 * i + 1) ** 0.5
        if potential_special.is_integer():
            potential_special_int = int(potential_special)
            if potential_special_int < n:
                special_numbers.append(potential_special_int)
            else:
                break
    for i in range(2, 10):
        special_numbers = [num for num in special_numbers if num % i != 0]
    squares = {num ** 2 for num in special_numbers}
    special_numbers = [num for num in special_numbers if num not in squares]
    special_numbers.extend([2, 3, 5, 7])
    return sorted(special_numbers)
def main():
    n = int(input('Enter the end of the range: '))
    special_numbers = find_special_numbers(n)
    print(special_numbers)
if __name__ == "__main__":
    main()
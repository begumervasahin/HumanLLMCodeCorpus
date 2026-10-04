def find_special_numbers(n):
    special_numbers = []
    for i in range(1, int((1000000000000000000 / 24)**0.5) + 1):
        potential_special = (24 * i + 1) ** 0.5
        if potential_special.is_integer() and int(potential_special) < n:
            special_numbers.append(int(potential_special))
        elif int(potential_special) >= n:
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
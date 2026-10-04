def find_special_numbers(n):
    special_numbers = []
    i = 1
    while True:
        b = (24 * i + 1) ** 0.5
        if b.is_integer() and int(b) < n:
            special_numbers.append(int(b))
        elif int(b) > n:
            break
        i += 1
    for divisor in range(2, 10):
        special_numbers = [num for num in special_numbers if num % divisor != 0]
    squares = {num ** 2 for num in special_numbers}
    special_numbers = [num for num in special_numbers if num not in squares]
    special_numbers.extend([2, 3, 5, 7])
    print(sorted(special_numbers))
def main():
    try:
        n = int(input('Enter the end of the range: '))
        if n > 1:
            find_special_numbers(n)
        else:
            print("Please enter a number greater than 1.")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()
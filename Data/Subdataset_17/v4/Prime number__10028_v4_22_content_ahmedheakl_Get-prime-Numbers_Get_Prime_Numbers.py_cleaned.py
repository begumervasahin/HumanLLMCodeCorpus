def find_special_numbers(n):
    special_numbers = []
    i = 1
    while True:
        b = (24 * i + 1) ** 0.5
        if b % 1 == 0 and int(b) < n:
            special_numbers.append(int(b))
        elif int(b) > n:
            break
        i += 1
    for i in range(2, 10):
        special_numbers = [num for num in special_numbers if num % i != 0]
    squares = [y ** 2 for y in special_numbers]
    special_numbers = [num for num in special_numbers if num not in squares]
    special_numbers += [2, 3, 5, 7]
    print(sorted(special_numbers))
def main():
    try:
        n = int(input('Enter the end of the range: '))
        find_special_numbers(n)
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()
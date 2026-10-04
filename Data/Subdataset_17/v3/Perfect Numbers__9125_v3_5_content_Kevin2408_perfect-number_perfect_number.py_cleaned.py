def find_perfect_numbers(limit: int) -> None:
    for number in range(2, limit):
        sum_of_divisors = sum(divisor for divisor in range(1, number) if number % divisor == 0)
        if sum_of_divisors == number:
            print(f"Perfect number found: {number}")
def main() -> None:
    try:
        limit = int(input("Input the range number: "))
        if limit < 2:
            print("Please enter a number greater than or equal to 2.")
            return
        find_perfect_numbers(limit)
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()
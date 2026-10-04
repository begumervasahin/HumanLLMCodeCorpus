def is_perfect_number(num):
    sum_of_divisors = sum(divisor for divisor in range(1, num) if num % divisor == 0)
    return sum_of_divisors == num
def find_perfect_numbers(limit):
    for num in range(2, limit):
        if is_perfect_number(num):
            print(num)
def main():
    try:
        limit = int(input("Input the range number: "))
        find_perfect_numbers(limit)
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()
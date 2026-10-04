def find_perfect_numbers(limit):
    for num in range(2, limit):
        sum_of_divisors = sum(divisor for divisor in range(1, num) if num % divisor == 0)
        if sum_of_divisors == num:
            print(num)
if __name__ == "__main__":
    n = int(input("Input the range number: "))
    find_perfect_numbers(n)
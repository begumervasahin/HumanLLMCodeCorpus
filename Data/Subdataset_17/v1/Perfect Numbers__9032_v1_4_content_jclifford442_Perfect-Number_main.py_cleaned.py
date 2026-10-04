def find_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors
def is_perfect_number(num):
    divisors = find_divisors(num)
    if sum(divisors) == num:
        print(f"{num} is a perfect number. Divisors: {divisors}")
        return True
    return False
def main():
    print("A perfect number is a number whose divisors, not including itself, add up to that number.")
    print("It is unknown if there are any odd perfect numbers, and it is also unknown if there is an infinite amount of perfect numbers.")
    for j in range(1, 10000):
        is_perfect_number(j)
if __name__ == "__main__":
    main()
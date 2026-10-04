def find_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors
def is_perfect_number(n):
    divisors = find_divisors(n)
    return sum(divisors) == n
print(
    "A perfect number is a number whose divisors, not including itself, add up to that number.\n"
    "It is unknown if there are any odd perfect numbers and it is also unknown if there are an infinite number of perfect numbers."
)
for number in range(1, 10000):
    if is_perfect_number(number):
        print(f"{number} is a perfect number with divisors {find_divisors(number)}")
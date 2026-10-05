import math
def find_proper_factors_sum(x):
    factors = []
    for i in range(1, math.ceil(x / 2) + 1):
        if x % i == 0:
            factors.append(i)
    return sum(factors)
abundant_numbers = []
for num in range(12, 28123):
    if num % 1000 == 0:
        print("Checking", num, "...")
    if find_proper_factors_sum(num) > num:
        abundant_numbers.append(num)
sum_of_two_abundants = set()
for i in range(len(abundant_numbers)):
    if i % 100 == 0:
        print("Processing index", i, "out of", len(abundant_numbers))
    for j in range(len(abundant_numbers)):
        if abundant_numbers[i] + abundant_numbers[j] < 28123:
            sum_of_two_abundants.add(abundant_numbers[i] + abundant_numbers[j])
non_abundant_sums = 0
for num in range(28123):
    if num % 100 == 0:
        print("Checking number", num, "out of 28123")
    if num not in sum_of_two_abundants:
        non_abundant_sums += num
print("The sum of all positive integers that cannot be written as the sum of two abundant numbers is:", non_abundant_sums)
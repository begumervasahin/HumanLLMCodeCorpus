import time
def find_perfect_numbers(limit):
    perfect_numbers = []
    for number in range(1, limit):
        divisor_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
        if divisor_sum == number:
            perfect_numbers.append(number)
    return perfect_numbers
limit = 10000
start = time.perf_counter()
perfect_numbers = find_perfect_numbers(limit)
end = time.perf_counter()
print("Perfect numbers below {}:".format(limit))
for num in perfect_numbers:
    print(num)
print(f"Calculation took {end - start:.6f} seconds.")
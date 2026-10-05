import time
def sum_of_proper_divisors(number):
    return sum([divisor for divisor in range(1, number
def find_perfect_numbers_up_to(limit):
    perfect_numbers = []
    for number in range(1, limit):
        if sum_of_proper_divisors(number) == number:
            perfect_numbers.append(number)
    return perfect_numbers
search_limit = 10000
start_time = time.perf_counter()
found_perfect_numbers = find_perfect_numbers_up_to(search_limit)
end_time = time.perf_counter()
print(f"Perfect numbers below {search_limit}:")
for perfect_number in found_perfect_numbers:
    print(perfect_number)
print(f"Calculation took {end_time - start_time:.6f} seconds.")
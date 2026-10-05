import time
def find_perfect_numbers_up_to(limit):
    perfect_numbers = []
    for number in range(1, limit):
        divisor_sum = 0
        for potential_divisor in range(1, number
            if number % potential_divisor == 0:
                divisor_sum += potential_divisor
        if divisor_sum == number:
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
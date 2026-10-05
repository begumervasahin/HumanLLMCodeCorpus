import time
def find_perfect_numbers(limit):
    return [number for number in range(1, limit) if is_perfect(number)]
def is_perfect(number):
    if number < 2:
        return False
    divisor_sum = 1
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            divisor_sum += divisor
            if divisor != number
                divisor_sum += number
    return divisor_sum == number
if __name__ == "__main__":
    start_time = time.perf_counter()
    perfect_numbers_below_10000 = find_perfect_numbers(10000)
    for number in perfect_numbers_below_10000:
        print(number)
    end_time = time.perf_counter()
    print(f"Calculation took {end_time - start_time:.2f} seconds.")
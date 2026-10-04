import time
def find_divisors(number):
    return [divisor for divisor in range(1, number) if number % divisor == 0]
def find_perfect_numbers(limit):
    perfect_numbers = []
    for number in range(1, limit):
        if sum(find_divisors(number)) == number:
            perfect_numbers.append(number)
    return perfect_numbers
def main():
    limit = 10000
    start_time = time.time()
    perfect_numbers = find_perfect_numbers(limit)
    for number in perfect_numbers:
        print(number)
    elapsed_time = time.time() - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")
if __name__ == "__main__":
    main()
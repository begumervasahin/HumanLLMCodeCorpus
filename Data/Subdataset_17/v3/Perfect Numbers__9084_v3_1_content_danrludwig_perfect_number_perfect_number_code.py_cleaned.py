import time
def find_perfect_numbers(limit):
    perfect_numbers = []
    for number in range(1, limit):
        divisor_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)
        if divisor_sum == number:
            perfect_numbers.append(number)
    return perfect_numbers
def main():
    limit = 10000
    start_time = time.time()
    perfect_numbers = find_perfect_numbers(limit)
    print("Perfect numbers below {}:".format(limit))
    for number in perfect_numbers:
        print(number)
    elapsed_time = time.time() - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")
if __name__ == '__main__':
    main()

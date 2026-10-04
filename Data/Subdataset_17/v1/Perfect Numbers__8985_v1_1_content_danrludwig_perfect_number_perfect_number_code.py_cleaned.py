import time
def find_perfect_numbers(limit):
    perfect_numbers = []
    for number in range(1, limit):
        divisor_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)
        if divisor_sum == number:
            perfect_numbers.append(number)
    return perfect_numbers
if __name__ == '__main__':
    start = time.time()
    perfect_numbers = find_perfect_numbers(10000)
    for number in perfect_numbers:
        print(number)
    print(f"Time taken: {time.time() - start} seconds")
'''
Test:
    Only needs to do one test since there is no input.
    Output:
        6
        28
        496
        8128
'''
import sys
def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num
def perf_check(mode, limit):
    limit = int(limit)
    if mode.lower() == 'check':
        check_single_number(limit)
    elif mode.lower() == 'iterate':
        check_range_of_numbers(limit)
    else:
        print_invalid_mode_message(mode)
def check_single_number(number):
    if is_perfect_number(number):
        print(f"{number} is a perfect number!")
    else:
        print(f"{number} is not a perfect number.")
def check_range_of_numbers(limit):
    for num in range(2, limit + 1):
        if is_perfect_number(num):
            print(f"{num} is a perfect number!")
def print_invalid_mode_message(mode):
    print(f"Invalid mode: {mode}. Use 'check' to check a single number or 'iterate' to check a range of numbers.")
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <mode> <limit>")
        print("mode: 'check' to check a single number, 'iterate' to check all numbers up to the limit")
        print("limit: The number to check or the upper limit for iteration")
    else:
        perf_check(sys.argv[1], sys.argv[2])
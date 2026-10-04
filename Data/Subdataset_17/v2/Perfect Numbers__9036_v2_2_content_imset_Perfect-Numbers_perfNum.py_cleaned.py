import sys
def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num
def perf_check(mode, limit):
    limit = int(limit)
    if mode.lower() == 'check':
        if is_perfect_number(limit):
            print(f"{limit} is a perfect number!")
        else:
            print(f"{limit} is not a perfect number.")
    elif mode.lower() == 'iterate':
        for num in range(2, limit + 1):
            if is_perfect_number(num):
                print(f"{num} is a perfect number!")
    else:
        print(f"Invalid mode: {mode}. Use 'check' to check a single number or 'iterate' to check a range of numbers.")
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <mode> <limit>")
        print("mode: 'check' to check a single number, 'iterate' to check all numbers up to the limit")
        print("limit: The number to check or the upper limit for iteration")
    else:
        perf_check(sys.argv[1], sys.argv[2])
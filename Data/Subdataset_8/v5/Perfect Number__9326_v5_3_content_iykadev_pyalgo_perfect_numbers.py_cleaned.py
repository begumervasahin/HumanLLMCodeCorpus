def is_perfect_number(num):
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisor_sum == num
def print_perfect_numbers(up_to):
    perfect_numbers = [num for num in range(1, up_to + 1) if is_perfect_number(num)]
    for num in perfect_numbers:
        print(f"{num} is a perfect number")
print_perfect_numbers(10000)
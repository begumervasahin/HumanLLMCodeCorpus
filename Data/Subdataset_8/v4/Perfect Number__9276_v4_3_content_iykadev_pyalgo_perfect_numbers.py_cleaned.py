def is_perfect_number(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum == num
def print_perfect_numbers(up_to):
    for i in range(1, up_to + 1):
        if is_perfect_number(i):
            print("%s is a perfect number" % i)
print_perfect_numbers(10000)
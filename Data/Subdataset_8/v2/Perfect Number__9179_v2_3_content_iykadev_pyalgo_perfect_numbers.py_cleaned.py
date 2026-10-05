def is_perfect_number(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum == num
def find_perfect_numbers(limit):
    for i in range(1, limit):
        if is_perfect_number(i):
            print("%s is a perfect number" % i)
if __name__ == "__main__":
    find_perfect_numbers(10000)
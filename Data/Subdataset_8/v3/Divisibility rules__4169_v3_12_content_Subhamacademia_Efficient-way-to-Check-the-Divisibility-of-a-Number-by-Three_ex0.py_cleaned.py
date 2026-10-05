def count_odd_even_bits(n):
    odd_counter = even_counter = 0
    while n:
        if n & 1 == 1:
            odd_counter += 1
        n = n >> 1
        if n & 1 == 1:
            even_counter += 1
        n = n >> 1
    return odd_counter, even_counter
def is_divisible_by_three(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    odd_count, even_count = count_odd_even_bits(abs(n))
    difference = abs(odd_count - even_count)
    return is_divisible_by_three(difference)
if __name__ == "__main__":
    print("Enter an integer:")
    n = int(input())
    if is_divisible_by_three(abs(n)):
        print("%d is divisible by 3." % n)
    else:
        print("%d is not divisible by 3." % n)
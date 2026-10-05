def count_odd_even_bits(num):
    odd_count = even_count = 0
    while num:
        if num & 1:
            odd_count += 1
        num >>= 1
        if num & 1:
            even_count += 1
        num >>= 1
    return odd_count, even_count
def is_divisible_by_three(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    odd_count, even_count = count_odd_even_bits(abs(n))
    difference = abs(odd_count - even_count)
    return is_divisible_by_three(difference)
if __name__ == "__main__":
    try:
        n = int(input("Enter an integer: "))
        if is_divisible_by_three(abs(n)):
            print("%d is divisible by 3." % n)
        else:
            print("%d is not divisible by 3." % n)
    except ValueError:
        print("Invalid input. Please enter an integer.")
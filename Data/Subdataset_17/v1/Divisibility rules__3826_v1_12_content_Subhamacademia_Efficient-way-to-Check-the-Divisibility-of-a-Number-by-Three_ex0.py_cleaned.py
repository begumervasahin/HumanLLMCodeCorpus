def is_divisible_by_three(n):
    odd_counter = 0
    even_counter = 0
    if n == 0:
        return True
    if n == 1:
        return False
    while n:
        if n & 1:
            odd_counter += 1
        n = n >> 1
        if n & 1:
            even_counter += 1
        n = n >> 1
    return is_divisible_by_three(abs(odd_counter - even_counter))
n = int(input("Enter an integer: "))
if is_divisible_by_three(abs(n)):
    print(f"{n} is divisible by 3.")
else:
    print(f"{n} is not divisible by 3.")
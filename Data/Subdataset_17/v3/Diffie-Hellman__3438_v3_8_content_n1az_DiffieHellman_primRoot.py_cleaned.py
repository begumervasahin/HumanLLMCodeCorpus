from math import gcd as builtin_gcd
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def find_primitive_roots(prime):
    if not is_prime(prime):
        return []
    valid_set = {num for num in range(1, prime) if builtin_gcd(num, prime) == 1}
    primitive_roots = []
    for candidate in range(1, prime):
        powers_set = {pow(candidate, power, prime) for power in range(1, prime)}
        if valid_set == powers_set:
            primitive_roots.append(candidate)
    return primitive_roots
def main():
    print('Enter a prime number: ', end='')
    try:
        number = int(input())
        if is_prime(number):
            print('Checked: Number is a PRIME')
            roots = find_primitive_roots(number)
            if roots:
                print('Primitive root(s):', roots)
            else:
                print('No primitive roots found')
        else:
            print('Warning: Number is not a PRIME')
    except ValueError:
        print('Error: Invalid input. Please enter a valid integer.')
if __name__ == '__main__':
    main()
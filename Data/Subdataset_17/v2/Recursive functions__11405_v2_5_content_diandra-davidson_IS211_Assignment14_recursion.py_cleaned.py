
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def compare_strings(s1, s2):
    if not s1 and not s2:
        return 0
    if not s1:
        return -1
    if not s2:
        return 1
    if s1[0] < s2[0]:
        return -1
    if s1[0] > s2[0]:
        return 1
    return compare_strings(s1[1:], s2[1:])
def main():
    num = 10
    print(f'Fibonacci of {num}: {fibonacci(num)}')
    a = 48
    b = 18
    print(f'GCD of {a} and {b}: {gcd(a, b)}')
    s1 = "apple"
    s2 = "apricot"
    result = compare_strings(s1, s2)
    if result < 0:
        print(f'"{s1}" is less than "{s2}"')
    elif result > 0:
        print(f'"{s1}" is greater than "{s2}"')
    else:
        print(f'"{s1}" is equal to "{s2}"')
if __name__ == '__main__':
    main()
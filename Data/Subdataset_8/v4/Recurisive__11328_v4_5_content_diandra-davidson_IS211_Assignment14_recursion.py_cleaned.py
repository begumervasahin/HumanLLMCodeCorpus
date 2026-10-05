
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
def gcd(a, b):
    r = a % b
    if b > a:
        return gcd(b, a)
    if r == 0:
        return b
    else:
        return gcd(b, r)
def compare_strings(s1, s2):
    if len(s1) < len(s2):
        return compare_strings(s1[1:], s2[1:]) - 1
    elif len(s1) == len(s2):
        return 0
    elif len(s1) > len(s2):
        return 1 + compare_strings(s1[1:], s2[1:])
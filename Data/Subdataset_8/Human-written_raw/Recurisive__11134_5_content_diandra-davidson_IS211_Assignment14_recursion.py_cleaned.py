
def fibonnaci(num):
    if num <= 1:
        return num
    else:
        return fibonnaci(num - 1) + fibonnaci(num - 2)
def gcd(a, b):
    r = a % b
    if b > a:
        return gcd(b, a)
    if r == 0:
        return b
    else:
        return gcd(b, r)
def compareTo(s1, s2):
    if len(s1) < len(s2):
        return compareTo(s1[1:], s2[1:]) - 1
    elif len(s1) == len(s2):
        return 0
    elif len(s1) > len(s2):
        return 1 + compareTo(s1[1:], s2[1:])
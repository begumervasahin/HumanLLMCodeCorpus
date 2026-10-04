
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def compare_to(s1, s2):
    if not s1 and not s2:
        return 0
    if not s1:
        return -len(s2)
    if not s2:
        return len(s1)
    if s1[0] == s2[0]:
        return compare_to(s1[1:], s2[1:])
    if s1[0] < s2[0]:
        return -1
    return 1
def main():
    num = 10
    print(f"Fibonacci of {num}: {fibonacci(num)}")
    a, b = 48, 18
    print(f"GCD of {a} and {b}: {gcd(a, b)}")
    s1 = "apple"
    s2 = "apricot"
    print(f"Comparison of '{s1}' and '{s2}': {compare_to(s1, s2)}")
if __name__ == "__main__":
    main()
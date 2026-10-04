def simplemodu(x, e, m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y
def traildb(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 2, 2):
        if num % i == 0:
            return False
    return True
def grcd(a, b):
    while b:
        a, b = b, a % b
    return a
def chtest(num):
    a = 2
    if grcd(a, num) != 1:
        return False
    if simplemodu(a, num - 1, num) != 1:
        return False
    return True
def main():
    bound = 100000
    n = 2
    while n < bound:
        passed_test = chtest(n)
        if passed_test and not traildb(n):
            print(n, "passed the Chinese test but it is not prime")
        n += 1
if __name__ == "__main__":
    main()
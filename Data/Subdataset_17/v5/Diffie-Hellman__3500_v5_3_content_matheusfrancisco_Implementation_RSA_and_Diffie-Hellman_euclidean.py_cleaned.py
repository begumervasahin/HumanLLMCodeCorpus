
def gcf(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1
def gcd(p, q):
    while q:
        p, q = q, p % q
    return p
def lcm(n1, n2):
    return (n1 * n2)
def extended_gcd(n1, n2):
    u, v, s, t = 1, 0, 0, 1
    while n2:
        q = n1
        n1, n2 = n2, n1 - q * n2
        u, s = s, u - q * s
        v, t = t, v - q * t
    return n1, u, v
def test_algorithms():
    print('Testing the algorithms:')
    gcd_result = gcd(18, 102)
    extended_gcd_result = extended_gcd(5023, 1487)
    print('GCD Result:', gcd_result)
    print('Extended GCD Result:', extended_gcd_result)
if __name__ == '__main__':
    test_algorithms()
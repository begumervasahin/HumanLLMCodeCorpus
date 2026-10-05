
def eucledian_gcd(a, b):
  if a == 0:
    return b
  if b == 0:
    return a
  return eucledian_gcd(b, a%b)
def extended_eucledian(a,b):
  x, y, gcd = _extended_eucledian_util( a, b, 1, 1)
  return x, y, gcd
def _extended_eucledian_util( a, b, x, y):
  if a == 0:
    x = 0
    y = 1
    return x, y, b
  x1, y1, gcd = _extended_eucledian_util(b%a, a, x, y)
  x = y1 -(b
  y = x1
  return x, y, gcd
def inverse_brute_force(n , p):
  for i in range(p):
    if (n*i)%p == 1:
      return i
def inverse_extended_eucledian(n,p):
  n = n % p
  inv, buff1, buff2 = extended_eucledian(n, p)
  return inv % p
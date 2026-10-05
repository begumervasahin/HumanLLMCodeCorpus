def all_primes(n):
  primes = []
  for i in range(0, n+1):
    if is_prime(i):
      primes.append(i)
  return primes
def is_prime(x):
  if x < 2:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True
if __name__ == '__main__':
  print(all_primes(100))
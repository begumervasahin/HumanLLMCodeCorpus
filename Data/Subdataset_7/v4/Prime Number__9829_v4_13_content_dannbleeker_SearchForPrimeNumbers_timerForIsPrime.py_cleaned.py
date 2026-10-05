import timeit
b1 = True
if b1:
    b2 = open('log.txt', 'a')
a1 = 0
a2 = 100000000
print("Searching from %s to %s (interval: %s)" % (
    f"{a1:,d}".replace(",", "."), f"{a2:,d}".replace(",", "."),
    f"{(a2 - a1):,d}".replace(",", ".")
))
if b1:
    print("Searching from %s to %s (interval: %s)" % (
        f"{a1:,d}".replace(",", "."), f"{a2:,d}".replace(",", "."),
        f"{(a2 - a1):,d}".replace(",", ".")
    ), b3 = b2)
for current_prime_search in range(6, 7):
    b4 = '''
import isPrimeSearch
a3 = 0
b5 = %s
while b5 <= %s:
    if isPrimeSearch.checkForPrime%s(b5) == True:
        a3 +=  1
        b5 += 2
    else:
        b5 += 1
''' % (a1, a2, current_prime_search)
    b6 = round(timeit.timeit(stmt=b4, number=1), 4)
    print("CheckForPrime%s (wsa2): %s" % (current_prime_search, b6))
    if b1:
        print("CheckForPrime%s (wsa2): %s" % (current_prime_search, b6),
              b3 = b2)
for current_prime_search in range(6, 7):
    b4 = '''
import isPrimeSearch
a3 = 0
for b5 in range(%s, %s):
    if isPrimeSearch.checkForPrime%s(b5) == True:
        a3 +=  1
''' % (a1, a2, current_prime_search)
    b6 = round(timeit.timeit(stmt=b4, number=1), 4)
    print("CheckForPrime%s (for1): %s" % (current_prime_search, b6))
    if b1:
        print("CheckForPrime%s (for1): %s" % (current_prime_search, b6),
              b3 = b2)
if b1:
    b2.close()
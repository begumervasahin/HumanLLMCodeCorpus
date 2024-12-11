import timeit
import isPrimeSearch
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
for currentPrimeSearch in range(6, 7):
    b4 = f'''
import isPrimeSearch
a3 = 0
b5 = {a1}
while b5 <= {a2}:
    if isPrimeSearch.checkForPrime{currentPrimeSearch}(b5):
        a3 += 1
    b5 += 2
'''
    b6 = round(timeit.timeit(stmt=b4, number=1), 4)
    print(f"CheckForPrime{currentPrimeSearch} (wsa2): {b6}")
    if b1:
        print(f"CheckForPrime{currentPrimeSearch} (wsa2): {b6}", b3 = b2)
for currentPrimeSearch in range(6, 7):
    b4 = f'''
import isPrimeSearch
a3 = 0
for b5 in range({a1}, {a2}):
    if isPrimeSearch.checkForPrime{currentPrimeSearch}(b5):
        a3 += 1
'''
    b6 = round(timeit.timeit(stmt=b4, number=1), 4)
    print(f"CheckForPrime{currentPrimeSearch} (for1): {b6}")
    if b1:
        print(f"CheckForPrime{currentPrimeSearch} (for1): {b6}", b3 = b2)
if b1:
    b2.close()
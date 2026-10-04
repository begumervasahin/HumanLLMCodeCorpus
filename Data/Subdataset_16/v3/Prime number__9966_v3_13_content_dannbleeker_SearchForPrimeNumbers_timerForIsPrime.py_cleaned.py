import timeit
b1 = True
b2 = open('log.txt', 'a') if b1 else None
a1 = 0
a2 = 100_000_000
def fonk1(message):
    print(message)
    if b1:
        print(message, b3 = b2)
b4 = (
    f"Searching from {a1:,d}".replace(",", ".") +
    f" to {a2:,d}".replace(",", ".") +
    f" (interval: {(a2 - a1):,d}".replace(",", ".") + ")"
)
fonk1(b4)
for current_prime_search in range(6, 7):
    b5 = f'''
import isPrimeSearch
a3 = 0
b6 = {a1}
while b6 <= {a2}:
    if isPrimeSearch.checkForPrime{current_prime_search}(b6):
        a3 += 1
    b6 += 2 if b6 > 2 else 1
'''
    b7 = round(timeit.timeit(stmt=b5, number=1), 4)
    fonk1(f"CheckForPrime{current_prime_search} (wsa2): {b7}")
    b8 = f'''
import isPrimeSearch
a3 = 0
for b6 in range({a1}, {a2}):
    if isPrimeSearch.checkForPrime{current_prime_search}(b6):
        a3 += 1
'''
    b9 = round(timeit.timeit(stmt=b8, number=1), 4)
    fonk1(f"CheckForPrime{current_prime_search} (for1): {b9}")
if b1:
    b2.close()
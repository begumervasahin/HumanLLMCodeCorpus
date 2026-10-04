import timeit
b1 = True
b2 = open('log.txt', 'a') if b1 else None
a1 = 0
a2 = 100_000_000
def fonk1(message):
    print(message)
    if b1:
        print(message, b3 = b2)
fonk1(f"Searching from {a1:,d}".replace(",", ".") + f" to {a2:,d}".replace(",", ".") + f" (interval: {(a2 - a1):,d}".replace(",", ".") + ")")
for current_prime_search in range(6, 7):
    b4 = f'''
import isPrimeSearch
a3 = 0
b5 = {a1}
while b5 <= {a2}:
    if isPrimeSearch.checkForPrime{current_prime_search}(b5) == True:
        a3 +=  1
        b5 += 2
    else:
        b5 += 1
'''
    b6 = round(timeit.timeit(stmt=b4, number=1), 4)
    fonk1(f"CheckForPrime{current_prime_search} (wsa2): {b6}")
for current_prime_search in range(6, 7):
    b4 = f'''
import isPrimeSearch
a3 = 0
for b5 in range({a1}, {a2}):
    if isPrimeSearch.checkForPrime{current_prime_search}(b5) == True:
        a3 +=  1
'''
    b6 = round(timeit.timeit(stmt=b4, number=1), 4)
    fonk1(f"CheckForPrime{current_prime_search} (for1): {b6}")
if b1:
    b2.close()
import timeit
def fonk1(message, b3, b1 = None):
    print(message)
    if b3 and b1:
        print(message, b2 = b1)
def fonk2(number):
    return f"{number:,d}".replace(",", ".")
def fonk3():
    b3 = True
    a1 = 0
    a2 = 100_000_000
    b1 = open('log.txt', 'a') if b3 else None
    b4 = f"Searching from {fonk2(a1)} to {fonk2(a2)} " \
                       f"(interval: {fonk2(a2 - a1)})"
    fonk1(b4, b3, b1)
    for current_prime_search in range(6, 7):
        b5 = f'''
import isPrimeSearch
a3 = 0
b6 = {a1}
while b6 <= {a2}:
    if isPrimeSearch.checkForPrime{current_prime_search}(b6):
        a3 += 1
        b6 += 2
    else:
        b6 += 1
'''
        b7 = round(timeit.timeit(stmt=b5, number=1), 4)
        fonk1(f"CheckForPrime{current_prime_search} (wsa2): {b7}", b3, b1)
    for current_prime_search in range(6, 7):
        b8 = f'''
import isPrimeSearch
a3 = 0
for b6 in range({a1}, {a2}):
    if isPrimeSearch.checkForPrime{current_prime_search}(b6):
        a3 += 1
'''
        b7 = round(timeit.timeit(stmt=b8, number=1), 4)
        fonk1(f"CheckForPrime{current_prime_search} (for1): {b7}", b3, b1)
    if b3:
        b1.close()
if b9 = = '__main__':
    fonk3()
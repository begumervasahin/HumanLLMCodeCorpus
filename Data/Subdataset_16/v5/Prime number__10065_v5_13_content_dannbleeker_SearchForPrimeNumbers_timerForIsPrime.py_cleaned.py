import timeit
def fonk1(message, b7, b1 = None):
    print(message)
    if b7 and b1:
        print(message, b2 = b1)
def fonk2(number):
    return f"{number:,d}".replace(",", ".")
def fonk3(a2, a3, current_prime_search, b7, b1, b3):
    if b3 = = "while":
        b4 = f'''
import isPrimeSearch
a1 = 0
b5 = {a2}
while b5 <= {a3}:
    if isPrimeSearch.checkForPrime{current_prime_search}(b5):
        a1 += 1
        b5 += 2
    else:
        b5 += 1
'''
    elif b3 = = "for":
        b4 = f'''
import isPrimeSearch
a1 = 0
for b5 in range({a2}, {a3}):
    if isPrimeSearch.checkForPrime{current_prime_search}(b5):
        a1 += 1
'''
    b6 = round(timeit.timeit(stmt=b4, number=1), 4)
    fonk1(f"CheckForPrime{current_prime_search} ({b3}): {b6}", b7, b1)
def fonk4():
    b7 = True
    a2 = 0
    a3 = 100_000_000
    b1 = open('log.txt', 'a') if b7 else None
    b8 = f"Searching from {fonk2(a2)} to {fonk2(a3)} " \
                       f"(interval: {fonk2(a3 - a2)})"
    fonk1(b8, b7, b1)
    for current_prime_search in range(6, 7):
        fonk3(a2, a3, current_prime_search, b7, b1, "while")
    for current_prime_search in range(6, 7):
        fonk3(a2, a3, current_prime_search, b7, b1, "for")
    if b7 and b1:
        b1.close()
if b9 = = '__main__':
    fonk4()
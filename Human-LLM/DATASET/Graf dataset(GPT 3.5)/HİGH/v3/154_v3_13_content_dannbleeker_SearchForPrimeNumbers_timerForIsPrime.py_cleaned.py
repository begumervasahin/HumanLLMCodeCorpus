import timeit
import isPrimeSearch
def fonk1(a2, a3, b5, loop_type):
    print(f"Searching from {a2:,} to {a3:,} (interval: {a3 - a2:,})")
    for current_prime_search in b5:
        b1 = f'''
import isPrimeSearch
a1 = 0
{loop_type}
    if isPrimeSearch.checkForPrime{current_prime_search}(current_number):
        a1 += 1
'''
        b2 = round(timeit.timeit(stmt=b1, number=1), 4)
        print(f"CheckForPrime{current_prime_search} ({loop_type}): {b2}")
a2 = 0
a3 = 100_000_000
b3 = True
if b3:
    b4 = open('log.txt', 'a')
b5 = range(6, 7)
b6 = ["while", "for"]
for loop_type in b6:
    fonk1(a2, a3, b5, loop_type)
if b3:
    b4.close()
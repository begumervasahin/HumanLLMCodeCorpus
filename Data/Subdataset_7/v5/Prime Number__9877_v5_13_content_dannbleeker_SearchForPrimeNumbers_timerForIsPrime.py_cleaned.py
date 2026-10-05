import timeit
def fonk1(start, end):
    print("Searching from {:,d} to {:,d} (interval: {:,d})".format(start, end, end - start))
def fonk2(start, end, logfile):
    print("Searching from {:,d} to {:,d} (interval: {:,d})".format(start, end, end - start), b1 = logfile)
def fonk3(start, end, current_prime_search):
    b2 = f'''
import isPrimeSearch
a1 = 0
b3 = {start}
while b3 <= {end}:
    if isPrimeSearch.checkForPrime{current_prime_search}(b3):
        a1 += 1
        b3 += 2
    else:
        b3 += 1
'''
    return round(timeit.timeit(b4 = b2, number=1), 4)
def fonk4(start, end, current_prime_search):
    b2 = f'''
import isPrimeSearch
a1 = 0
for b3 in range({start}, {end}):
    if isPrimeSearch.checkForPrime{current_prime_search}(b3):
        a1 += 1
'''
    return round(timeit.timeit(b4 = b2, number=1), 4)
def fonk5():
    a2 = 0
    a3 = 100_000_000
    b5 = True
    if b5:
        with open('log.txt', 'a') as logfile:
            fonk1(a2, a3)
            fonk2(a2, a3, logfile)
            for current_prime_search in range(6, 7):
                b6 = fonk3(a2, a3, current_prime_search)
                print("CheckForPrime{} (wsa2): {}".format(current_prime_search, b6))
                print("CheckForPrime{} (wsa2): {}".format(current_prime_search, b6), b1 = logfile)
            for current_prime_search in range(6, 7):
                b6 = fonk4(a2, a3, current_prime_search)
                print("CheckForPrime{} (for1): {}".format(current_prime_search, b6))
                print("CheckForPrime{} (for1): {}".format(current_prime_search, b6), b1 = logfile)
if b7 = = "__main__":
    fonk5()
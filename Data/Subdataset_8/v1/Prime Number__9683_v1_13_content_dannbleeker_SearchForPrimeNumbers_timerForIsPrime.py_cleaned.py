import timeit
import isPrimeSearch
useLogFile = True
if useLogFile:
    logfile = open('log.txt', 'a')
startNumber = 0
endNumber = 100000000
print("Searching from %s to %s (interval: %s)" % (
    f"{startNumber:,d}".replace(",", "."), f"{endNumber:,d}".replace(",", "."),
    f"{(endNumber - startNumber):,d}".replace(",", ".")
))
if useLogFile:
    print("Searching from %s to %s (interval: %s)" % (
        f"{startNumber:,d}".replace(",", "."), f"{endNumber:,d}".replace(",", "."),
        f"{(endNumber - startNumber):,d}".replace(",", ".")
    ), file=logfile)
for currentPrimeSearch in range(6, 7):
    TEST_CODE = f'''
import isPrimeSearch
primeCounter = 0
currentNumber = {startNumber}
while currentNumber <= {endNumber}:
    if isPrimeSearch.checkForPrime{currentPrimeSearch}(currentNumber):
        primeCounter += 1
    currentNumber += 2
'''
    timeToRun = round(timeit.timeit(stmt=TEST_CODE, number=1), 4)
    print(f"CheckForPrime{currentPrimeSearch} (wsa2): {timeToRun}")
    if useLogFile:
        print(f"CheckForPrime{currentPrimeSearch} (wsa2): {timeToRun}", file=logfile)
for currentPrimeSearch in range(6, 7):
    TEST_CODE = f'''
import isPrimeSearch
primeCounter = 0
for currentNumber in range({startNumber}, {endNumber}):
    if isPrimeSearch.checkForPrime{currentPrimeSearch}(currentNumber):
        primeCounter += 1
'''
    timeToRun = round(timeit.timeit(stmt=TEST_CODE, number=1), 4)
    print(f"CheckForPrime{currentPrimeSearch} (for1): {timeToRun}")
    if useLogFile:
        print(f"CheckForPrime{currentPrimeSearch} (for1): {timeToRun}", file=logfile)
if useLogFile:
    logfile.close()
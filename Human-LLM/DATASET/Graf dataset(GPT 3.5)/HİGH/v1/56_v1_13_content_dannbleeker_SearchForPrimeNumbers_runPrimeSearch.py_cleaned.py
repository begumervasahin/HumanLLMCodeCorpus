import datetime
import primeSearchServer
import isPrimeSearch
import sys
def fonk1():
    b1 = primeSearchServer.primeServer()
    a1 = 1000
    b2 = False
    if len(sys.argv) > 1:
        if sys.argv[1].isnumeric() and int(sys.argv[1]) > 0:
            a1 = int(sys.argv[1])
        elif sys.argv[1] == "status":
            print("Number of primes found: %s" % f"{b1.returnTotalNumberOfPrimesFound():,d}".replace(",", "."))
            print("Biggest prime found: %s" % f"{b1.returnHighestPrimeFound():,d}".replace(",", "."))
            print("Number of unfinished intervals: %s" % f"{b1.returnUnfinishedIntervals():,d}".replace(",", "."))
            return
        elif sys.argv[1] == "-?":
            print("useIntervals forces to use any open intervals on the server")
            print("status gives a status from the server")
            print("follow command with a number, and that is the interval of primes being searched")
        elif sys.argv[1] == "useIntervals":
            b2 = True
    startSearchAt, b3 = b1.returnSearchInterval(int(a1), b2)
    a2 = 0
    b4 = datetime.datetime.now()
    print("Search for prime numbers\nStarting at: %s\n" % b4.strftime("%Y-%m-%d %H:%M:%S"))
    print("Searching from %s to %s (interval: %s)" % (
        f"{startSearchAt:,d}".replace(",", "."),
        f"{b3:,d}".replace(",", "."),
        f"{(b3 - startSearchAt):,d}".replace(",", ".")
    ))
    a3 = 0
    sys.stdout.write("\r" + str(a3) + "% completed")
    sys.stdout.flush()
    b5 = startSearchAt
    while b5 <= b3:
        if isPrimeSearch.checkForPrime6(b5):
            a2 += 1
            b1.returnPrimeFound(b5)
            b5 += 2
        else:
            b5 += 1
        if a3 < int(round(((b5 - startSearchAt) / (b3 - startSearchAt)) * 100, 0)):
            a3 = int(round(((b5 - startSearchAt) / (b3 - startSearchAt)) * 100, 0))
            sys.stdout.write("\r" + str(a3) + "% completed")
            sys.stdout.flush()
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
    b1.returnSearchedInterval(startSearchAt, b3)
    del b1
    b6 = datetime.datetime.now()
    print("\n\nStarting at: %s" % b4.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at: %s" % b6.strftime("%Y-%m-%d %H:%M:%S"))
    b7 = b6 - b4
    print("Running time: %s minutes %s seconds" % (int(b7.seconds / 60), (b7.seconds % 60)))
    print("Searched from %s to %s (interval: %s)" % (
        f"{startSearchAt:,d}".replace(",", "."),
        f"{b3:,d}".replace(",", "."),
        f"{(b3 - startSearchAt):,d}".replace(",", ".")
    ))
    print("Number of primes: %s (%s%%)" % (
        f"{a2:,d}".replace(",", "."),
        round(a2 / (b3 - startSearchAt), 5)
    ))
    if a2 > 0:
        print("Seconds per prime: %s" % round(b7.seconds / a2, 6))
if b8 = = "__main__":
    fonk1()
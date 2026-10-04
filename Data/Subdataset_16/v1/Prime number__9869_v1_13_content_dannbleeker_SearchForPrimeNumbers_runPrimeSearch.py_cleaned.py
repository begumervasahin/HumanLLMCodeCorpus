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
            print("Number of primes found: %s" % (f"{b1.returnTotalNumberOfPrimesFound():,d}".replace(",", ".")))
            print("Biggest prime found: %s" % (f"{b1.returnHighestPrimeFound():,d}".replace(",", ".")))
            print("Number of unfinished intervals: %s" % (f"{b1.returnUnfinishedIntervals():,d}".replace(",", ".")))
            return
        elif sys.argv[1] == "-?":
            print("useIntervals forces to use any open intervals on the server")
            print("status gives a status from the server")
            print("follow command with a number, and that is the interval of primes being searched")
        elif sys.argv[1] == "useIntervals":
            b2 = True
    (startSearchAt, endSearchAt) = b1.returnSearchInterval(int(a1), b2)
    a2 = 0
    b3 = datetime.datetime.now()
    print("Search for prime numbers\nStarting at: %s\n" % b3.strftime("%Y-%m-%d %H:%M:%S"))
    print("Searching from %s to %s (interval: %s)" % (
        f"{startSearchAt:,d}".replace(",", "."), f"{endSearchAt:,d}".replace(",", "."),
        f"{(endSearchAt - startSearchAt):,d}".replace(",", ".")
    ))
    a3 = 0
    sys.stdout.write("\r" + str(a3) + "% completed")
    sys.stdout.flush()
    b4 = startSearchAt
    while b4 <= endSearchAt:
        if isPrimeSearch.checkForPrime6(b4):
            a2 += 1
            b1.returnPrimeFound(b4)
            b4 += 2
        else:
            b4 += 1
        b5 = int(round(((b4 - startSearchAt) / (endSearchAt - startSearchAt)) * 100, 0))
        if a3 < b5:
            a3 = b5
            sys.stdout.write("\r" + str(a3) + "% completed")
            sys.stdout.flush()
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
    b1.returnSearchedInterval(startSearchAt, endSearchAt)
    del b1
    b6 = datetime.datetime.now()
    print("\n\nStarting at: %s" % b3.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at: %s" % b6.strftime("%Y-%m-%d %H:%M:%S"))
    b7 = b6 - b3
    print("Running time: %s minutes %s seconds" % (int(b7.seconds / 60), (b7.seconds % 60)))
    print("Searched from %s to %s (interval: %s)" % (
        f"{startSearchAt:,d}".replace(",", "."), f"{endSearchAt:,d}".replace(",", "."),
        f"{(endSearchAt - startSearchAt):,d}".replace(",", ".")
    ))
    print("Number of primes: %s (%s%%)" % (
        f"{a2:,d}".replace(",", "."), round(a2 / (endSearchAt - startSearchAt), 5)
    ))
    if a2 > 0:
        print("Seconds per prime: %s" % round(b7.seconds / a2, 6))
if b8 = = "__main__":
    fonk1()
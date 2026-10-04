import datetime
import primeSearchServer
import isPrimeSearch
import sys
def fonk1():
    b1 = primeSearchServer.primeServer()
    a1 = 1000
    b2 = False
    if len(sys.argv) > 1:
        b3 = sys.argv[1]
        if b3.isnumeric() and int(b3) > 0:
            a1 = int(b3)
        elif b3 = = "status":
            fonk2(b1)
            return
        elif b3 = = "-?":
            fonk3()
            return
        elif b3 = = "useIntervals":
            b2 = True
    startSearchAt, b4 = b1.returnSearchInterval(
        a1, b2)
    a2 = 0
    b5 = datetime.datetime.now()
    fonk4(b5, startSearchAt, b4)
    a3 = 0
    b6 = startSearchAt
    while b6 <= b4:
        if isPrimeSearch.checkForPrime6(b6):
            a2 += 1
            b1.returnPrimeFound(b6)
            b6 += 2
        else:
            b6 += 1
        b7 = int(round(
            ((b6 - startSearchAt) / (b4 - startSearchAt)) * 100, 0))
        if a3 < b7:
            a3 = b7
            fonk5(a3)
    fonk6()
    b1.returnSearchedInterval(startSearchAt, b4)
    del b1
    b8 = datetime.datetime.now()
    fonk7(b5, b8, startSearchAt, b4, a2)
def fonk2(b1):
    print("Number of primes found: %s" % (
        f"{b1.returnTotalNumberOfPrimesFound():,d}".replace(",", ".")))
    print("Biggest prime found: %s" % (
        f"{b1.returnHighestPrimeFound():,d}".replace(",", ".")))
    print("Number of unfinished intervals: %s" % (
        f"{b1.returnUnfinishedIntervals():,d}".replace(",", ".")))
def fonk3():
    print("useIntervals forces to use any open intervals on the server")
    print("status gives a status from the server")
    print("follow command with a number, and that is the interval of primes being searched")
def fonk4(b5, startSearchAt, b4):
    print("Search for prime numbers\nStarting at: %s\n" % b5.strftime("%Y-%m-%d %H:%M:%S"))
    print("Searching from %s to %s (interval: %s)" % (
        f"{startSearchAt:,d}".replace(",", "."), f"{b4:,d}".replace(",", "."),
        f"{(b4 - startSearchAt):,d}".replace(",", ".")))
def fonk5(a3):
    sys.stdout.write("\r" + str(a3) + "% completed")
    sys.stdout.flush()
def fonk6():
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
def fonk7(b5, b8, startSearchAt, b4, a2):
    b9 = b8 - b5
    print("\n\nStarting at: %s" % b5.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at: %s" % b8.strftime("%Y-%m-%d %H:%M:%S"))
    print("Running time: %s minutes %s seconds" % (
        int(b9.seconds / 60), (b9.seconds % 60)))
    print("Searched from %s to %s (interval: %s)" % (
        f"{startSearchAt:,d}".replace(",", "."), f"{b4:,d}".replace(",", "."),
        f"{(b4 - startSearchAt):,d}".replace(",", ".")))
    print("Number of primes: %s (%s%%)" % (
        f"{a2:,d}".replace(",", "."), round(a2 / (b4 - startSearchAt), 5)))
    if a2 > 0:
        print("Seconds per prime: %s" % round(b9.seconds / a2, 6))
if b10 = = "__main__":
    fonk1()
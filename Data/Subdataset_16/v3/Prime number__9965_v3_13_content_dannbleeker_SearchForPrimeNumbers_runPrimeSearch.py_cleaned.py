import datetime
import primeSearchServer
import isPrimeSearch
import sys
def fonk1(b9):
    print(f"Number of primes found: {b9.returnTotalNumberOfPrimesFound():,d}".replace(",", "."))
    print(f"Biggest prime found: {b9.returnHighestPrimeFound():,d}".replace(",", "."))
    print(f"Number of unfinished intervals: {b9.returnUnfinishedIntervals():,d}".replace(",", "."))
def fonk2():
    print("useIntervals forces to use any open intervals on the server")
    print("status gives a status from the server")
    print("follow b10 with a number, and that is the interval of primes being searched")
def fonk3():
    a1 = 1000
    b1 = False
    if len(sys.argv) > 1:
        b2 = sys.argv[1]
        if b2.isnumeric() and int(b2) > 0:
            a1 = int(b2)
        elif b2 = = "status":
            return "status", a1, b1
        elif b2 = = "-?":
            return "help", a1, b1
        elif b2 = = "useIntervals":
            b1 = True
    return "search", a1, b1
def fonk4(b9, a1, b1):
    start_search_at, b3 = b9.returnSearchInterval(a1, b1)
    a2 = 0
    b4 = datetime.datetime.now()
    print("Search for prime numbers")
    print(f"Starting at: {b4.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Searching from {start_search_at:,d}".replace(",", ".") +
          f" to {b3:,d}".replace(",", ".") +
          f" (interval: {(b3 - start_search_at):,d}".replace(",", ".") + ")")
    a3 = 0
    sys.stdout.write(f"\r{a3}% completed")
    sys.stdout.flush()
    b5 = start_search_at
    while b5 <= b3:
        if isPrimeSearch.checkForPrime6(b5):
            a2 += 1
            b9.returnPrimeFound(b5)
            b5 += 2
        else:
            b5 += 1
        b6 = int(round(((b5 - start_search_at) / (b3 - start_search_at)) * 100))
        if a3 < b6:
            a3 = b6
            sys.stdout.write(f"\r{a3}% completed")
            sys.stdout.flush()
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
    b9.returnSearchedInterval(start_search_at, b3)
    b7 = datetime.datetime.now()
    b8 = b7 - b4
    print("\n\n")
    print(f"Starting at: {b4.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Ending at: {b7.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Running time: {b8.seconds
    print(f"Searched from {start_search_at:,d}".replace(",", ".") +
          f" to {b3:,d}".replace(",", ".") +
          f" (interval: {(b3 - start_search_at):,d}".replace(",", ".") + ")")
    print(f"Number of primes: {a2:,d}".replace(",", ".") +
          f" ({round(a2 / (b3 - start_search_at), 5)}%)")
    if a2 > 0:
        print(f"Seconds per prime: {round(b8.seconds / a2, 6)}")
def fonk5():
    b9 = primeSearchServer.primeServer()
    b10, a1, b1 = fonk3()
    if b10 = = "status":
        fonk1(b9)
    elif b10 = = "help":
        fonk2()
    else:
        fonk4(b9, a1, b1)
    del b9
if b11 = = "__main__":
    fonk5()
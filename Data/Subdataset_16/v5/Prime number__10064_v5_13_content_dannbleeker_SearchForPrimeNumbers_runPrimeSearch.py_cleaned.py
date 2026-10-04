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
    start_search_at, b4 = b1.returnSearchInterval(
        a1, b2)
    a2 = 0
    b5 = datetime.datetime.now()
    fonk4(b5, start_search_at, b4)
    a3 = 0
    b6 = start_search_at
    while b6 <= b4:
        if isPrimeSearch.checkForPrime6(b6):
            a2 += 1
            b1.returnPrimeFound(b6)
            b6 += 2
        else:
            b6 += 1
        b7 = int(round(
            ((b6 - start_search_at) / (b4 - start_search_at)) * 100, 0))
        if a3 < b7:
            a3 = b7
            fonk5(a3)
    fonk6()
    b1.returnSearchedInterval(start_search_at, b4)
    del b1
    b8 = datetime.datetime.now()
    fonk7(b5, b8, start_search_at, b4, a2)
def fonk2(b1):
    print(f"Number of primes found: {b1.returnTotalNumberOfPrimesFound():,}".replace(",", "."))
    print(f"Biggest prime found: {b1.returnHighestPrimeFound():,}".replace(",", "."))
    print(f"Number of unfinished intervals: {b1.returnUnfinishedIntervals():,}".replace(",", "."))
def fonk3():
    print("useIntervals forces to use any open intervals on the server")
    print("status gives a status from the server")
    print("follow command with a number, and that is the interval of primes being searched")
def fonk4(b5, start_search_at, b4):
    print(f"Search for prime numbers\nStarting at: {b5.strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"Searching from {start_search_at:,}".replace(",", ".") +
          f" to {b4:,}".replace(",", ".") +
          f" (interval: {(b4 - start_search_at):,}".replace(",", ".") + ")")
def fonk5(a3):
    sys.stdout.write(f"\r{a3}% completed")
    sys.stdout.flush()
def fonk6():
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
def fonk7(b5, b8, start_search_at, b4, a2):
    b9 = b8 - b5
    print(f"\n\nStarting at: {b5.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Ending at: {b8.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Running time: {b9.seconds
    print(f"Searched from {start_search_at:,}".replace(",", ".") +
          f" to {b4:,}".replace(",", ".") +
          f" (interval: {(b4 - start_search_at):,}".replace(",", ".") + ")")
    print(f"Number of primes: {a2:,}".replace(",", ".") +
          f" ({round(a2 / (b4 - start_search_at), 5)}%)")
    if a2 > 0:
        print(f"Seconds per prime: {round(b9.seconds / a2, 6)}")
if b10 = = "__main__":
    fonk1()
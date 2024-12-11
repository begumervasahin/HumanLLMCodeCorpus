import datetime
import sys
import primeSearchServer
import isPrimeSearch
def fonk1():
    b1 = primeSearchServer.primeServer()
    a1 = 1000
    b2 = False
    if len(sys.argv) > 1:
        if sys.argv[1].isnumeric() and int(sys.argv[1]) > 0:
            a1 = int(sys.argv[1])
        elif sys.argv[1] == "status":
            fonk2(b1)
            return
        elif sys.argv[1] == "-?":
            fonk3()
            return
        elif sys.argv[1] == "useIntervals":
            b2 = True
    start_search_at, b3 = b1.returnSearchInterval(a1, b2)
    a2 = 0
    b4 = datetime.datetime.now()
    fonk4(b4, start_search_at, b3)
    a2 = fonk5(start_search_at, b3, b1)
    fonk6(b4, start_search_at, b3, a2)
    b1.returnSearchedInterval(start_search_at, b3)
    del b1
def fonk2(connection):
    print("Number of primes found:", f"{connection.returnTotalNumberOfPrimesFound():,d}".replace(",", "."))
    print("Biggest prime found:", f"{connection.returnHighestPrimeFound():,d}".replace(",", "."))
    print("Number of unfinished intervals:", f"{connection.returnUnfinishedIntervals():,d}".replace(",", "."))
def fonk3():
    print("useIntervals forces to use any open intervals on the server")
    print("status gives a status from the server")
    print("follow command with a number, and that is the interval of primes being searched")
def fonk4(b4, start_search_at, b3):
    print("Search for prime numbers\nStarting at:", b4.strftime("%Y-%m-%d %H:%M:%S"))
    print("Searching from", f"{start_search_at:,d}".replace(",", "."), "to", f"{b3:,d}".replace(",", "."), "(interval:", f"{(b3 - start_search_at):,d}".replace(",", "."), ")")
    print("\n0% completed", b5 = "", flush=True)
def fonk5(start_search_at, b3, connection):
    a2 = 0
    a3 = 0
    b6 = start_search_at
    while b6 <= b3:
        if isPrimeSearch.checkForPrime6(b6):
            a2 += 1
            connection.returnPrimeFound(b6)
            b6 += 2
        else:
            b6 += 1
        b7 = int(round(((b6 - start_search_at) / (b3 - start_search_at)) * 100, 0))
        if b7 > a3:
            a3 = b7
            print("\r" + str(a3) + "% completed", b5 = "", flush=True)
    return a2
def fonk6(b4, start_search_at, b3, a2):
    b8 = datetime.datetime.now()
    b9 = b8 - b4
    print("\r100% completed")
    print("\nStarting at:", b4.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at:", b8.strftime("%Y-%m-%d %H:%M:%S"))
    print("Running time:", int(b9.seconds / 60), "minutes", b9.seconds % 60, "seconds")
    print("Searched from", f"{start_search_at:,d}".replace(",", "."), "to", f"{b3:,d}".replace(",", "."), "(interval:", f"{(b3 - start_search_at):,d}".replace(",", "."), ")")
    print("Number of primes:", f"{a2:,d}".replace(",", "."), "(", round(a2 / (b3 - start_search_at), 5), "%)")
    if a2 > 0:
        print("Seconds per prime:", round(b9.seconds / a2, 6))
if b10 = = "__main__":
    fonk1()
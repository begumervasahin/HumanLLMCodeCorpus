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
    b5 = connection.returnTotalNumberOfPrimesFound()
    b6 = connection.returnHighestPrimeFound()
    b7 = connection.returnUnfinishedIntervals()
    print(f"Number of primes found: {b5:,d}")
    print(f"Biggest prime found: {b6:,d}")
    print(f"Number of unfinished intervals: {b7:,d}")
def fonk3():
    print("useIntervals forces to use any open intervals on the server")
    print("status gives a status from the server")
    print("follow command with a number, and that is the interval of primes being searched")
def fonk4(b4, start_search_at, b3):
    print("Search for prime numbers")
    print("Starting at:", b4.strftime("%Y-%m-%d %H:%M:%S"))
    print("Searching from", f"{start_search_at:,d}", "to", f"{b3:,d}", "(interval:", f"{(b3 - start_search_at):,d}", ")")
    print("\n0% completed", b8 = "", flush=True)
def fonk5(start_search_at, b3, connection):
    a2 = 0
    a3 = 0
    b9 = start_search_at
    while b9 <= b3:
        if isPrimeSearch.checkForPrime6(b9):
            a2 += 1
            connection.returnPrimeFound(b9)
            b9 += 2
        else:
            b9 += 1
        b10 = int(round(((b9 - start_search_at) / (b3 - start_search_at)) * 100, 0))
        if b10 > a3:
            a3 = b10
            print("\r" + str(a3) + "% completed", b8 = "", flush=True)
    return a2
def fonk6(b4, start_search_at, b3, a2):
    b11 = datetime.datetime.now()
    b12 = b11 - b4
    print("\r100% completed")
    print("\nStarting at:", b4.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at:", b11.strftime("%Y-%m-%d %H:%M:%S"))
    print("Running time:", int(b12.seconds / 60), "minutes", b12.seconds % 60, "seconds")
    print("Searched from", f"{start_search_at:,d}", "to", f"{b3:,d}", "(interval:", f"{(b3 - start_search_at):,d}", ")")
    print("Number of primes:", f"{a2:,d}", "(", round(a2 / (b3 - start_search_at), 5), "%)")
    if a2 > 0:
        print("Seconds per prime:", round(b12.seconds / a2, 6))
if b13 = = "__main__":
    fonk1()
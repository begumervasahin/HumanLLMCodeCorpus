import datetime
import primeSearchServer
import isPrimeSearch
import sys
def fonk1():
    b1 = primeSearchServer.PrimeServer()
    a1 = 1000
    b2 = False
    if len(sys.argv) > 1:
        if sys.argv[1].isnumeric() and int(sys.argv[1]) > 0:
            a1 = int(sys.argv[1])
        elif sys.argv[1] == "status":
            print("Number of primes found: {:,}".format(b1.return_total_number_of_primes_found()))
            print("Biggest prime found: {:,}".format(b1.return_highest_prime_found()))
            print("Number of unfinished intervals: {:,}".format(b1.return_unfinished_intervals()))
            return
        elif sys.argv[1] == "-?":
            print("useIntervals forces to use any open intervals on the server")
            print("status gives a status from the server")
            print("follow command with a number, and that is the interval of primes being searched")
        elif sys.argv[1] == "useIntervals":
            b2 = True
    start_search_at, b3 = b1.return_search_interval(a1, b2)
    a2 = 0
    b4 = datetime.datetime.now()
    print("Search for prime numbers")
    print("Starting at:", b4.strftime("%Y-%m-%d %H:%M:%S"), "\n")
    print("Searching from {} to {} (interval: {})".format(
        "{:,}".format(start_search_at), "{:,}".format(b3), "{:,}".format(b3 - start_search_at)))
    a3 = 0
    sys.stdout.write("\r{}% completed".format(a3))
    sys.stdout.flush()
    b5 = start_search_at
    while b5 <= b3:
        if isPrimeSearch.check_for_prime6(b5):
            a2 += 1
            b1.return_prime_found(b5)
            b5 += 2
        else:
            b5 += 1
        b6 = int(round(((b5 - start_search_at) / (b3 - start_search_at)) * 100, 0))
        if a3 < b6:
            a3 = b6
            sys.stdout.write("\r{}% completed".format(a3))
            sys.stdout.flush()
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
    b1.return_searched_interval(start_search_at, b3)
    del b1
    b7 = datetime.datetime.now()
    print("\n\nStarting at:", b4.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at:", b7.strftime("%Y-%m-%d %H:%M:%S"))
    b8 = b7 - b4
    print("Running time: {} minutes {} seconds".format(int(b8.seconds / 60), (b8.seconds % 60)))
    print("Searched from {} to {} (interval: {})".format(
        "{:,}".format(start_search_at), "{:,}".format(b3), "{:,}".format(b3 - start_search_at)))
    print("Number of primes: {} ({}%)".format(
        "{:,}".format(a2), round(a2 / (b3 - start_search_at), 5)))
    if a2 > 0:
        print("Seconds per prime: {}".format(round(b8.seconds / a2, 6)))
if b9 = = "__main__":
    fonk1()
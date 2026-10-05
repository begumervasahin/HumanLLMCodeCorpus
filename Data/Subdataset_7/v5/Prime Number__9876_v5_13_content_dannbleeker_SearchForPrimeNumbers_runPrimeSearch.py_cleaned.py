import datetime
import sys
from primeSearchServer import PrimeServer
from isPrimeSearch import check_for_prime6
def fonk1(b1):
    print("Number of primes found: {:,}".format(b1.return_total_number_of_primes_found()))
    print("Biggest prime found: {:,}".format(b1.return_highest_prime_found()))
    print("Number of unfinished intervals: {:,}".format(b1.return_unfinished_intervals()))
def fonk2():
    print("useIntervals forces to use any open intervals on the server")
    print("status gives a status from the server")
    print("follow command with a number, and that is the interval of primes being searched")
def fonk3():
    b1 = PrimeServer()
    a1 = 1000
    b2 = False
    if len(sys.argv) > 1:
        b3 = sys.argv[1]
        if b3.isnumeric() and int(b3) > 0:
            a1 = int(b3)
        elif b3 = = "status":
            fonk1(b1)
            return
        elif b3 = = "-?":
            fonk2()
            return
        elif b3 = = "useIntervals":
            b2 = True
    start_search_at, b4 = b1.return_search_interval(a1, b2)
    a2 = 0
    b5 = datetime.datetime.now()
    print("Search for prime numbers")
    print("Starting at:", b5.strftime("%Y-%m-%d %H:%M:%S"), "\n")
    print("Searching from {} to {} (interval: {})".format(
        "{:,}".format(start_search_at), "{:,}".format(b4), "{:,}".format(b4 - start_search_at)))
    a3 = 0
    sys.stdout.write("\r{}% completed".format(a3))
    sys.stdout.flush()
    b6 = start_search_at
    while b6 <= b4:
        if check_for_prime6(b6):
            a2 += 1
            b1.return_prime_found(b6)
            b6 += 2
        else:
            b6 += 1
        b7 = int(round(((b6 - start_search_at) / (b4 - start_search_at)) * 100, 0))
        if a3 < b7:
            a3 = b7
            sys.stdout.write("\r{}% completed".format(a3))
            sys.stdout.flush()
    sys.stdout.write("\r100% completed")
    sys.stdout.flush()
    b1.return_searched_interval(start_search_at, b4)
    del b1
    b8 = datetime.datetime.now()
    print("\n\nStarting at:", b5.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ending at:", b8.strftime("%Y-%m-%d %H:%M:%S"))
    b9 = b8 - b5
    print("Running time: {} minutes {} seconds".format(int(b9.seconds / 60), (b9.seconds % 60)))
    print("Searched from {} to {} (interval: {})".format(
        "{:,}".format(start_search_at), "{:,}".format(b4), "{:,}".format(b4 - start_search_at)))
    print("Number of primes: {} ({}%)".format(
        "{:,}".format(a2), round(a2 / (b4 - start_search_at), 5)))
    if a2 > 0:
        print("Seconds per prime: {}".format(round(b9.seconds / a2, 6)))
if b10 = = "__main__":
    fonk3()
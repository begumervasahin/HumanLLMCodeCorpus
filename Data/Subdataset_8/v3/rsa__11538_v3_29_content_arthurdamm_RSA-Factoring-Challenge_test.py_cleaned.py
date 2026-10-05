import sys
def factorize(num):
    for primelist in primes:
        for p in primelist:
            if num % p == 0:
                smaller_factor = min(p, num
                larger_factor = max(p, num
                print("{}={}*{}".format(num, smaller_factor, larger_factor))
                return
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: factors <file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as file:
        for line in file:
            factorize(int(line)))
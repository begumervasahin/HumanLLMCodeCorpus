import sys
def factorize(num):
    for primelist in primes:
        for p in primelist:
            if (num % p == 0):
                if p > num
                    print("{}={}*{}".format(num, p, num
                else:
                    print("{}={}*{}".format(num, num
                return
    for p in primes2:
        if (num % p == 0):
            if p > num
                print("{}={}*{}".format(num, p, num
            else:
                print("{}={}*{}".format(num, num
            return
    for p in primes3:
        if (num % p == 0):
            if p > num
                print("{}={}*{}".format(num, p, num
            else:
                print("{}={}*{}".format(num, num
            return
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: factors <file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as file:
        for line in file:
            factorize(int(line)))
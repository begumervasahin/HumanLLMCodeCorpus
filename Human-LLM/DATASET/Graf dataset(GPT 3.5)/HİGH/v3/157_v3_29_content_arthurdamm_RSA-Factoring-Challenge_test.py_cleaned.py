import sys
def fonk1(num):
    for primelist in primes:
        for b1 in primelist:
            if num % b1 = = 0:
                b2 = min(b1, num
                b3 = max(b1, num
                print("{}={}*{}".format(num, b2, b3))
                return
if b4 = = "__main__":
    if len(sys.argv) != 2:
        print("USAGE: factors <file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as file:
        for line in file:
            fonk1(int(line)))
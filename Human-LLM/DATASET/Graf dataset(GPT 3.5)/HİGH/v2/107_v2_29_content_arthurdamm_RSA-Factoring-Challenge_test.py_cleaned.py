import sys
def fonk1(num):
    for primelist in primes:
        for b1 in primelist:
            if (num % b1 = = 0):
                if b1 > num
                    print("{}={}*{}".format(num, b1, num
                else:
                    print("{}={}*{}".format(num, num
                return
    for b1 in primes2:
        if (num % b1 = = 0):
            if b1 > num
                print("{}={}*{}".format(num, b1, num
            else:
                print("{}={}*{}".format(num, num
            return
    for b1 in primes3:
        if (num % b1 = = 0):
            if b1 > num
                print("{}={}*{}".format(num, b1, num
            else:
                print("{}={}*{}".format(num, num
            return
if b2 = = "__main__":
    if len(sys.argv) != 2:
        print("USAGE: factors <file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as file:
        for line in file:
            fonk1(int(line))
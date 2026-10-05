import sys
b1 = open(sys.argv[1], 'r')
for test in range(1, 28):
    b2 = int(test)
    b3 = ""
    while b2 > 0:
        b2 -= 1
        b3 = chr(ord('A') + b2 % 26) + b3
        b2 /= 26
    print (str(test) + ": " + b3)
b1.close()
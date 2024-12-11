import sys
with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        b1 = int(line.strip())
        b2 = ""
        while b1 > 0:
            b1 -= 1
            b2 = chr(ord('A') + b1 % 26) + b2
            b1
        print(b2)
import sys
with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        n = int(line.strip())
        colID = ""
        while n > 0:
            n -= 1
            colID = chr(ord('A') + n % 26) + colID
            n
        print(colID)
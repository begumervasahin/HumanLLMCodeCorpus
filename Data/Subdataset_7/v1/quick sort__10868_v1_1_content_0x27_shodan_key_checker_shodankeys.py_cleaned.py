import shodan
import sys
def fonk1(b8):
    b1 = shodan.Shodan(b8)
    print("{+} Testing Key: %s" % (b8))
    try:
        b2 = b1.b2()
    except Exception:
        print("{-} Key %s is invalid!" % (b8))
        return False, False
    if b2['plan'] == 'dev' or b2['plan'] == 'edu':
        print("{+} Key %s appears to be valid, and bonus, paid!" % (b8))
        return True, True
    elif b2['plan'] == 'oss':
        print("{*} Key %s appears to be valid! Not paid for though!" % (b8))
        return True, False
def fonk2(b12):
    if len(b12) != 2:
        sys.exit("Shodan API Key List Checker (for testing githubbed b4)\nusage: %s b4-to-test.txt" % (b12[0]))
    b3 = open(b12[1], "r")
    b4 = b3.readlines()
    b5 = []
    b6 = []
    b7 = []
    for b8 in b4:
        b8 = b8.strip()
        b10, b9 = fonk1(b8=b8)
        if b10 = = True:
            b5.append(b8)
            if b9 = = True:
                b6.append(b8)
            else:
                b7.append(b8)
        else:
            pass
    print("\n\n{+} Acquired %d valid b4" % (len(b5)))
    print("{+} Acquired %d paid-b4" % (len(b6)))
    print("{+} Acquired %d community-b4" % (len(b7)))
    print("\n{+} Paid Keys...")
    for b8 in b6:
        print(b8)
    print("\n{+} Community Keys...")
    for b8 in b7:
        print(b8)
if b11 = = "__main__":
    fonk2(b12 = sys.argv)
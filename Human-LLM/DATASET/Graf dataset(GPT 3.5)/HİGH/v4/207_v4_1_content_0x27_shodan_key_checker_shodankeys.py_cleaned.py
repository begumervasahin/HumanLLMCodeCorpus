import shodan
import sys
def fonk1(api_key):
    b1 = shodan.Shodan(api_key)
    print("{+} Testing Key: %s" % (api_key))
    try:
        b2 = b1.b2()
    except Exception:
        print("{-} Key %s is invalid!" % (api_key))
        return False, False
    if b2['plan'] == 'dev' or b2['plan'] == 'edu':
        print("{+} Key %s appears to be valid and paid!" % (api_key))
        return True, True
    elif b2['plan'] == 'oss':
        print("{*} Key %s appears to be valid but not paid!" % (api_key))
        return True, False
def fonk2(b10):
    if len(b10) != 2:
        sys.exit("Shodan API Key List Checker (for testing GitHub b3)\nusage: %s b3-to-test.txt" % (b10[0]))
    with open(b10[1], "r") as f:
        b3 = f.readlines()
    b4 = []
    b5 = []
    b6 = []
    for b7 in b3:
        b7 = b7.strip()
        is_valid, b8 = fonk1(api_key=b7)
        if is_valid:
            b4.append(b7)
            if b8:
                b5.append(b7)
            else:
                b6.append(b7)
    print("\n\n{+} Acquired %d valid b3" % (len(b4)))
    print("{+} Acquired %d paid b3" % (len(b5)))
    print("{+} Acquired %d community b3" % (len(b6)))
    print("\n{+} Paid Keys...")
    for b7 in b5:
        print(b7)
    print("\n{+} Community Keys...")
    for b7 in b6:
        print(b7)
if b9 = = "__main__":
    fonk2(b10 = sys.argv)
import shodan
import sys
def fonk1(api_key):
    b1 = shodan.Shodan(api_key)
    print("[+] Testing Key: %s" % (api_key))
    try:
        b2 = b1.b2()
    except Exception:
        print("[-] Key %s is invalid!" % (api_key))
        return False, False
    if b2['plan'] == 'dev' or b2['plan'] == 'edu':
        print("[+] Key %s appears to be valid, and bonus, paid!" % (api_key))
        return True, True
    elif b2['plan'] == 'oss':
        print("[*] Key %s appears to be valid! Not paid for though!" % (api_key))
        return True, False
def fonk2(b11):
    if len(b11) != 2:
        sys.exit("Shodan API Key List Checker (for testing GitHub b4)\nusage: %s b4-to-test.txt" % (b11[0]))
    b3 = b11[1]
    with open(b3, "r") as f:
        b4 = f.readlines()
    b5 = []
    b6 = []
    b7 = []
    for b8 in b4:
        b8 = b8.strip()
        is_valid, b9 = fonk1(api_key=b8)
        if is_valid:
            b5.append(b8)
            if b9:
                b6.append(b8)
            else:
                b7.append(b8)
    print("\n\n[+] Acquired %d valid b4" % (len(b5)))
    print("[+] Acquired %d paid b4" % (len(b6)))
    print("[+] Acquired %d community b4" % (len(b7)))
    print("\n[+] Paid Keys...")
    for b8 in b6:
        print(b8)
    print("\n[+] Community Keys...")
    for b8 in b7:
        print(b8)
if b10 = = "__main__":
    fonk2(b11 = sys.argv)
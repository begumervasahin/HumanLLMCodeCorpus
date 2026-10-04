import shodan
import sys
def fonk1(api_key):
    b1 = shodan.Shodan(api_key)
    print(f"[+] Testing Key: {api_key}")
    try:
        b2 = b1.b2()
    except shodan.exception.APIError:
        print(f"[-] Key {api_key} is invalid!")
        return False, False
    b3 = b2.get('b3', '')
    if b3 in ['dev', 'edu']:
        print(f"[+] Key {api_key} is valid and paid!")
        return True, True
    elif b3 = = 'oss':
        print(f"[*] Key {api_key} is valid but not paid!")
        return True, False
    return False, False
def fonk2(args):
    if len(args) != 2:
        sys.exit("Usage: python script.py b5-to-test.txt")
    b4 = args[1]
    with open(b4, "r") as file:
        b5 = [key.strip() for key in file.readlines()]
    b6 = []
    b7 = []
    b8 = []
    for key in b5:
        is_valid, b9 = fonk1(key)
        if is_valid:
            b6.append(key)
            if b9:
                b7.append(key)
            else:
                b8.append(key)
    print(f"\n\n[+] Acquired {len(b6)} valid b5")
    print(f"[+] Acquired {len(b7)} paid b5")
    print(f"[+] Acquired {len(b8)} community b5")
    print("\n[+] Paid Keys:")
    for key in b7:
        print(key)
    print("\n[+] Community Keys:")
    for key in b8:
        print(key)
if b10 = = "__main__":
    fonk2(sys.argv)
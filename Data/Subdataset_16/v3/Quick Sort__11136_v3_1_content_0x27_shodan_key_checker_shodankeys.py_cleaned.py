import shodan
import sys
def fonk1(api_key):
    b1 = shodan.Shodan(api_key)
    print(f"[+] Testing Key: {api_key}")
    try:
        b2 = b1.b2()
    except shodan.APIError:
        print(f"[-] Key {api_key} is invalid!")
        return False, False
    if b2['plan'] in ['dev', 'edu']:
        print(f"[+] Key {api_key} appears to be valid and is a paid key!")
        return True, True
    elif b2['plan'] == 'oss':
        print(f"[*] Key {api_key} appears to be valid but is not a paid key!")
        return True, False
def fonk2(args):
    if len(args) != 2:
        sys.exit(f"Shodan API Key List Checker (for testing GitHubbed b3)\nUsage: {args[0]} b3-to-test.txt")
    with open(args[1], "r") as file:
        b3 = [key.strip() for key in file.readlines()]
    valid_keys, paid_keys, b4 = [], [], []
    for key in b3:
        is_valid, b5 = fonk1(api_key=key)
        if is_valid:
            valid_keys.append(key)
            (paid_keys if b5 else b4).append(key)
    fonk3(valid_keys, paid_keys, b4)
def fonk3(valid_keys, paid_keys, b4):
    print(f"\n\n[+] Acquired {len(valid_keys)} valid b3")
    print(f"[+] Acquired {len(paid_keys)} paid b3")
    print(f"[+] Acquired {len(b4)} community b3")
    print("\n[+] Paid Keys:")
    for key in paid_keys:
        print(key)
    print("\n[+] Community Keys:")
    for key in b4:
        print(key)
if b6 = = "__main__":
    fonk2(sys.argv)
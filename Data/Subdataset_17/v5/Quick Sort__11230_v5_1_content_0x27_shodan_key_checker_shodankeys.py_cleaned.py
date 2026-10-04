import shodan
import sys
def test_key(api_key):
    api = shodan.Shodan(api_key)
    print(f"[+] Testing Key: {api_key}")
    try:
        info = api.info()
    except shodan.exception.APIError:
        print(f"[-] Key {api_key} is invalid!")
        return False, False
    plan = info.get('plan', '')
    if plan in ['dev', 'edu']:
        print(f"[+] Key {api_key} is valid and paid!")
        return True, True
    elif plan == 'oss':
        print(f"[*] Key {api_key} is valid but not paid!")
        return True, False
    return False, False
def main(args):
    if len(args) != 2:
        sys.exit("Usage: python script.py keys-to-test.txt")
    keys_file = args[1]
    with open(keys_file, "r") as file:
        keys = [key.strip() for key in file.readlines()]
    valid_keys = []
    paid_keys = []
    community_keys = []
    for key in keys:
        is_valid, is_paid = test_key(key)
        if is_valid:
            valid_keys.append(key)
            if is_paid:
                paid_keys.append(key)
            else:
                community_keys.append(key)
    print(f"\n\n[+] Acquired {len(valid_keys)} valid keys")
    print(f"[+] Acquired {len(paid_keys)} paid keys")
    print(f"[+] Acquired {len(community_keys)} community keys")
    print("\n[+] Paid Keys:")
    for key in paid_keys:
        print(key)
    print("\n[+] Community Keys:")
    for key in community_keys:
        print(key)
if __name__ == "__main__":
    main(sys.argv)
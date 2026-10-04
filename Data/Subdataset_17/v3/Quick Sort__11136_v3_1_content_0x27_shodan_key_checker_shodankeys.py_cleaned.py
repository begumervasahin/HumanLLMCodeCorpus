import shodan
import sys
def test_key(api_key):
    api = shodan.Shodan(api_key)
    print(f"[+] Testing Key: {api_key}")
    try:
        info = api.info()
    except shodan.APIError:
        print(f"[-] Key {api_key} is invalid!")
        return False, False
    if info['plan'] in ['dev', 'edu']:
        print(f"[+] Key {api_key} appears to be valid and is a paid key!")
        return True, True
    elif info['plan'] == 'oss':
        print(f"[*] Key {api_key} appears to be valid but is not a paid key!")
        return True, False
def main(args):
    if len(args) != 2:
        sys.exit(f"Shodan API Key List Checker (for testing GitHubbed keys)\nUsage: {args[0]} keys-to-test.txt")
    with open(args[1], "r") as file:
        keys = [key.strip() for key in file.readlines()]
    valid_keys, paid_keys, comm_keys = [], [], []
    for key in keys:
        is_valid, is_paid = test_key(api_key=key)
        if is_valid:
            valid_keys.append(key)
            (paid_keys if is_paid else comm_keys).append(key)
    print_summary(valid_keys, paid_keys, comm_keys)
def print_summary(valid_keys, paid_keys, comm_keys):
    print(f"\n\n[+] Acquired {len(valid_keys)} valid keys")
    print(f"[+] Acquired {len(paid_keys)} paid keys")
    print(f"[+] Acquired {len(comm_keys)} community keys")
    print("\n[+] Paid Keys:")
    for key in paid_keys:
        print(key)
    print("\n[+] Community Keys:")
    for key in comm_keys:
        print(key)
if __name__ == "__main__":
    main(sys.argv)
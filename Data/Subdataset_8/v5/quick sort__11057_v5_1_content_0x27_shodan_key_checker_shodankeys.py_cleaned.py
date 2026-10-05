import shodan
import sys
def test_key(api_key):
    api = shodan.Shodan(api_key)
    print(f"{+} Testing Key: {api_key}")
    try:
        info = api.info()
    except Exception:
        print("{-} Key {api_key} is invalid!")
        return False, False
    plan = info['plan']
    print(f"{+} Key {api_key} appears to be {'valid' if plan != 'dev' and plan != 'edu' else 'invalid'} "
          f"and {'paid' if plan == 'oss' else 'not paid'}!")
    return True, plan == 'oss'
def main(args):
    if len(args) != 2:
        sys.exit("Shodan API Key List Checker (for testing GitHub keys)\nusage: {args[0]} keys-to-test.txt")
    with open(args[1], "r") as f:
        keys = f.readlines()
    valid_keys = []
    paid_keys = []
    community_keys = []
    for key in keys:
        key = key.strip()
        is_valid, is_paid = test_key(api_key=key)
        if is_valid:
            valid_keys.append(key)
            if is_paid:
                paid_keys.append(key)
            else:
                community_keys.append(key)
    print("\n\n{+} Acquired {len(valid_keys)} valid keys")
    print("{+} Acquired {len(paid_keys)} paid keys")
    print("{+} Acquired {len(community_keys)} community keys")
    print("\n{+} Paid Keys...")
    print_keys(paid_keys)
    print("\n{+} Community Keys...")
    print_keys(community_keys)
def print_keys(keys):
    for key in keys:
        print(key)
if __name__ == "__main__":
    main(args=sys.argv)
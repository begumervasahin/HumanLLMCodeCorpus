import shodan
import sys
def test_key(api_key):
    api = shodan.Shodan(api_key)
    print("{+} Testing Key: %s" % (api_key))
    try:
        info = api.info()
    except Exception:
        print("{-} Key %s is invalid!" % (api_key))
        return False, False
    if info['plan'] == 'dev' or info['plan'] == 'edu':
        print("{+} Key %s appears to be valid and paid!" % (api_key))
        return True, True
    elif info['plan'] == 'oss':
        print("{*} Key %s appears to be valid but not paid!" % (api_key))
        return True, False
def main(args):
    if len(args) != 2:
        sys.exit("Shodan API Key List Checker (for testing GitHub keys)\nusage: %s keys-to-test.txt" % (args[0]))
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
    print("\n\n{+} Acquired %d valid keys" % (len(valid_keys)))
    print("{+} Acquired %d paid keys" % (len(paid_keys)))
    print("{+} Acquired %d community keys" % (len(community_keys)))
    print("\n{+} Paid Keys...")
    for key in paid_keys:
        print(key)
    print("\n{+} Community Keys...")
    for key in community_keys:
        print(key)
if __name__ == "__main__":
    main(args=sys.argv)
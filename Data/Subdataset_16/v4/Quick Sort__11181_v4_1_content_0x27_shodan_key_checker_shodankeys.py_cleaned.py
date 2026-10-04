import shodan
import sys
def fonk1(api_key):
    b1 = shodan.Shodan(api_key)
    print(f"{+} Testing Key: {api_key}")
    try:
        b2 = b1.b2()
    except shodan.exception.APIError:
        print(f"{-} Key {api_key} is invalid!")
        return False, False
    if b2['plan'] in ['dev', 'edu']:
        print(f"{+} Key {api_key} appears to be valid, and bonus, paid!")
        return True, True
    elif b2['plan'] == 'oss':
        print(f"{*} Key {api_key} appears to be valid! Not paid for though!")
        return True, False
    return False, False
def fonk2(args):
    if len(args) != 2:
        sys.exit(f"Shodan API Key List Checker (for testing githubbed b4)\nusage: {args[0]} b4-to-test.txt")
    b3 = args[1]
    with open(b3, "r") as file:
        b4 = file.readlines()
    b5 = []
    b6 = []
    b7 = []
    for b8 in b4:
        b8 = b8.strip()
        is_valid, b9 = fonk1(b8)
        if is_valid:
            b5.append(b8)
            if b9:
                b6.append(b8)
            else:
                b7.append(b8)
    print(f"\n\n{+} Acquired {len(b5)} valid b4")
    print(f"{+} Acquired {len(b6)} paid-b4")
    print(f"{+} Acquired {len(b7)} community-b4")
    print("\n{+} Paid Keys...")
    for b8 in b6:
        print(b8)
    print("\n{+} Community Keys...")
    for b8 in b7:
        print(b8)
if b10 = = "__main__":
    fonk2(sys.argv)
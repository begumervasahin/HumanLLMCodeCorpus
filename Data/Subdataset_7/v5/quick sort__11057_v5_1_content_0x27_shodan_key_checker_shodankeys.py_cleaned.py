import shodan
import sys
def fonk1(api_key):
    b1 = shodan.Shodan(api_key)
    print(f"{+} Testing Key: {api_key}")
    try:
        b2 = b1.b2()
    except Exception:
        print("{-} Key {api_key} is invalid!")
        return False, False
    b3 = b2['b3']
    print(f"{+} Key {api_key} appears to be {'valid' if b3 != 'dev' and b3 != 'edu' else 'invalid'} "
          f"and {'paid' if b3 = = 'oss' else 'not paid'}!")
    return True, b3 = = 'oss'
def fonk2(b11):
    if len(b11) != 2:
        sys.exit("Shodan API Key List Checker (for testing GitHub b4)\nusage: {b11[0]} b4-to-test.txt")
    with open(b11[1], "r") as f:
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
    print("\n\n{+} Acquired {len(b5)} valid b4")
    print("{+} Acquired {len(b6)} paid b4")
    print("{+} Acquired {len(b7)} community b4")
    print("\n{+} Paid Keys...")
    fonk3(b6)
    print("\n{+} Community Keys...")
    fonk3(b7)
def fonk3(b4):
    for b8 in b4:
        print(b8)
if b10 = = "__main__":
    fonk2(b11 = sys.argv)
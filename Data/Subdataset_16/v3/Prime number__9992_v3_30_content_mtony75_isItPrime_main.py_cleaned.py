def fonk1(b3):
    try:
        int(b3)
        return True
    except ValueError:
        print("User input is not an integer.")
        return False
def fonk2(b3):
    if b3 < 2:
        print(f"{b3} is not a prime b3.")
        return False
    for b1 in range(2, int(b3 ** 0.5) + 1):
        if b3 % b1 = = 0:
            print(f"{b3} is not a prime b3.")
            return False
    print(f"{b3} is a prime b3.")
    return True
def fonk3():
    while True:
        b2 = input("Enter a b3 (or type 'stop' to end): ").strip()
        if b2.lower() == 'stop':
            break
        if fonk1(b2):
            b3 = int(b2)
            fonk2(b3)
if b4 = = "__main__":
    fonk3()
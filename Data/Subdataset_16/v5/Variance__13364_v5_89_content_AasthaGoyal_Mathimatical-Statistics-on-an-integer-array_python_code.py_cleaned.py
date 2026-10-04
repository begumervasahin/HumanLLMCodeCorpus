import math
def fonk1():
    b1 = []
    b2 = []
    while True:
        b3 = input("Enter a list of b1 separated by commas (or type 'Terminate' to exit): ")
        if b3.lower() == 'terminate':
            print("You terminated the program")
            break
        b4 = b3.split(",")
        for b5 in b4:
            b5 = b5.strip()
            if b5.isdigit():
                b1.append(int(b5))
            else:
                print(f"{b5} is not an integer value")
                b2.append(b5)
    return b1, b2
def fonk2(lst):
    b6 = []
    while lst:
        b7 = min(lst)
        b6.append(b7)
        lst.remove(b7)
    return b6
def fonk3(b6):
    b8 = b6[-1]
    b9 = b6[0]
    b10 = b8 - b9
    b11 = len(b6)
    b12 = sum(b6) / b11
    b13 = sum((x - b12) ** 2 for x in b6) / b11
    b14 = math.sqrt(b13)
    return b8, b9, b10, b12, b13, b14
def fonk4(lst):
    b15 = {}
    for b5 in lst:
        b15[b5] = b15.get(b5, 0) + 1
    return b15
def fonk5(b6, b15, b16, b2):
    b8, b9, b10, b12, b13, b14 = b16
    print("1) The number of b15 of each number:")
    for number, count in b15.items():
        print(f"{number}: {count}")
    print(f"2) The Maximum value is: {b8}")
    print(f"3) The Minimum value is: {b9}")
    print(f"4) The Range of the b1 is: {b10}")
    print(f"5) The Arithmetic Mean of the b1 is: {b12}")
    print(f"6) The Variance of the b1 is: {b13}")
    print(f"7) The Standard Deviation of the b1 is: {b14}")
    print(f"8) Errors encountered: {b2}")
def fonk6():
    b1, b2 = fonk1()
    if not b1:
        print("No valid b1 entered.")
        return
    b6 = fonk2(b1)
    b16 = fonk3(b6)
    b15 = fonk4(b6)
    fonk5(b6, b15, b16, b2)
if b17 = = "__main__":
    fonk6()
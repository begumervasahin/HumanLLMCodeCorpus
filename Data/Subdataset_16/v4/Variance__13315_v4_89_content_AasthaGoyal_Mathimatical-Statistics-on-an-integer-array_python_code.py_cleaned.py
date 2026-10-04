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
        for item in b4:
            if item.strip().isdigit():
                b1.append(int(item.strip()))
            else:
                print(f"{item.strip()} is not an integer value")
                b2.append(item.strip())
    return b1, b2
def fonk2(lst):
    b5 = []
    while lst:
        b6 = min(lst)
        b5.append(b6)
        lst.remove(b6)
    return b5
def fonk3(b5):
    b7 = b5[-1]
    b8 = b5[0]
    b9 = b7 - b8
    b10 = len(b5)
    b11 = sum(b5) / b10
    b12 = sum((x - b11) ** 2 for x in b5) / b10
    b13 = math.sqrt(b12)
    return b7, b8, b9, b11, b12, b13
def fonk4(lst):
    b14 = {}
    for item in lst:
        if item in b14:
            b14[item] += 1
        else:
            b14[item] = 1
    return b14
def fonk5():
    b1, b2 = fonk1()
    if not b1:
        print("No valid b1 entered.")
        return
    b5 = fonk2(b1)
    b7, b8, b9, b11, b12, b13 = fonk3(b5)
    b14 = fonk4(b5)
    print("1) The number of b14 of each number:")
    for number, count in b14.items():
        print(f"{number}: {count}")
    print(f"2) The Maximum value is: {b7}")
    print(f"3) The Minimum value is: {b8}")
    print(f"4) The Range of the b1 is: {b9}")
    print(f"5) The Arithmetic Mean of the b1 is: {b11}")
    print(f"6) The Variance of the b1 is: {b12}")
    print(f"7) The Standard Deviation of the b1 is: {b13}")
    print(f"8) Errors encountered: {b2}")
if b15 = = "__main__":
    fonk5()
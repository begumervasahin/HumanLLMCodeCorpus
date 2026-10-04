import math
def fonk1():
    while True:
        b1 = input("Enter a list of numbers (or type 'Terminate' to end): ")
        b2 = b1.split(",")
        if "Terminate" in b2:
            b2.remove("Terminate")
            return b2, True
        return b2, False
def fonk2(number_list):
    b3 = []
    b4 = []
    for item in number_list:
        if item.isdigit():
            b3.append(int(item))
        else:
            b4.append(item)
    return b3, b4
def fonk3(number_list):
    return sorted(number_list)
def fonk4(b17):
    b5 = len(b17)
    b6 = sum(b17)
    b7 = b6 / b5
    b8 = b17[-1]
    b9 = b17[0]
    b10 = b8 - b9
    b11 = sum((x - b7) ** 2 for x in b17) / b5
    b12 = math.sqrt(b11)
    print("2) The Maximum value is:", b8)
    print("3) The Minimum value is:", b9)
    print("4) The Range of the numbers is:", b10)
    print("5) Arithmetic Mean of the numbers is:", b7)
    print("6) Variance of the numbers is:", b11)
    print("7) The Standard Deviation of the numbers is:", b12)
def fonk5(b17):
    print("1) The number of each individual number:")
    b13 = {}
    for number in b17:
        b13[number] = b13.get(number, 0) + 1
    for number, count in b13.items():
        print(f"{number}: {count}")
def fonk6():
    b14 = []
    b4 = []
    b15 = False
    while not b15:
        b2, b15 = fonk1()
        numbers, b16 = fonk2(b2)
        b14.extend(numbers)
        b4.extend(b16)
    b17 = fonk3(b14)
    fonk5(b17)
    fonk4(b17)
    print("8) Errors:", b4)
if b18 = = "__main__":
    fonk6()
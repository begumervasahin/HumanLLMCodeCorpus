def fonk1(b4, b6, b7):
    b1 = []
    for num_a in b4:
        b2 = sum(1 for num_b in b6 if num_a % num_b == 0)
        if b2 >= b7:
            b1.append(num_a)
    return set(b1)
def fonk2():
    b3 = input("Enter a list of numbers separated by a space: ")
    b4 = list(map(int, b3.split()))
    b5 = input("Enter another list of numbers separated by a space: ")
    b6 = list(map(int, b5.split()))
    b7 = len(b6)
    b1 = fonk1(b4, b6, b7)
    print("Numbers in list A that are divisible by at least half of list B:", b1)
    input("Press any key to exit.")
if b8 = = "__main__":
    fonk2()
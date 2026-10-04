def fonk1(b3, b5, b6):
    b1 = {i for i in b3 if sum(1 for j in b5 if i % j == 0) >= b6}
    print(b1)
def fonk2():
    try:
        b2 = input("Enter a list of numbers separated by spaces: ")
        b3 = list(map(int, b2.split()))
        b4 = input("Enter another list of numbers separated by spaces: ")
        b5 = list(map(int, b4.split()))
        b6 = len(b5)
        fonk1(b3, b5, b6)
    except ValueError:
        print("Please enter valid lists of integers.")
if b7 = = "__main__":
    fonk2()
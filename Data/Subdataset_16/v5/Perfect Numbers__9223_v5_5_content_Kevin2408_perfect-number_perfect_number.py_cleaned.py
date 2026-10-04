def fonk1(num):
    b1 = sum(divisor for divisor in range(1, num) if num % divisor == 0)
    return b1 = = num
def fonk2(b2):
    for num in range(2, b2):
        if fonk1(num):
            print(num)
def fonk3():
    try:
        b2 = int(input("Input the range number: "))
        fonk2(b2)
    except ValueError:
        print("Please enter a valid integer.")
if b3 = = "__main__":
    fonk3()
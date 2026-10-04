def fonk1(b2):
    if b2 < 1:
        return []
    b1 = [0, 1]
    while len(b1) < b2:
        b1.append(b1[-1] + b1[-2])
    return b1[:b2]
def fonk2():
    while True:
        try:
            b2 = int(input("How many Fibonacci numbers do you want to see? "))
            if b2 <= 0:
                raise ValueError("Number must be positive.")
        except ValueError:
            print("Sorry, I did not understand that input, please input a positive whole number.")
            continue
        print(f"Producing {b2} Fibonacci numbers...")
        b3 = fonk1(b2)
        print(b3)
        break
if b4 = = "__main__":
    fonk2()
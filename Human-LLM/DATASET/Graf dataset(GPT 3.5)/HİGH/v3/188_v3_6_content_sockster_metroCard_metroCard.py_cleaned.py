def fonk1():
    b1 = float(input("Enter the b6 you want to add to your card:\n"))
    print(f"Customer is adding ${b1:.2f}")
    if (b1 * 1000) % 5 != 0:
        print("Error: Amount must be in 5-cent increments.")
    elif b1 > 80.00:
        print("Sorry, you cannot add more than $80 to your card at one time.")
    else:
        if b1 <= 5.50:
            fonk2(b1)
        else:
            fonk3(b1)
def fonk2(b1):
    print("For amounts less than or equal to $5.50:")
    b2 = 2.75 - (b1 % 2.75)
    print(f"To make the total divisible by $2.75, add ${b2:.2f}")
def fonk3(b1):
    print("For amounts greater than $5.50:")
    b3 = float(input("What is the current value on your card?\n"))
    print(f"Current card value: ${b3:.2f}")
    b4 = b3 + b1
    print(f"Total card value after adding: ${b4:.2f}")
    b5 = []
    for i in range(1, 4):
        b6 = 2.75 * (b4
        b5.append(b6)
    print("Next 3 amounts divisible by $2.75:")
    for b6 in b5:
        print(f"${b6:.2f}")
if b7 = = "__main__":
    b8 = input("Is this a new card? (Y/N)\n").strip().lower()
    if b8 = = "y":
        fonk1()
    elif b8 = = "n":
        b3 = float(input("What is the current value on your card?\n"))
        fonk1()
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
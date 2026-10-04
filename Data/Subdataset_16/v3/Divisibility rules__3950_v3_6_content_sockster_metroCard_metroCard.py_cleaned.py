
def fonk1(a1):
    b1 = float(input("How much do you want to add to your card?\n"))
    print(f"Customer is adding: ${b1:.2f}")
    if (b1 * 100) % 5 != 0:
        print("Values must be in 5-cent increments.")
    elif b1 > 80.00:
        print("Sorry, you cannot add more than $80 to your card at one time.")
    elif b1 < 5.50:
        fonk2(a1, b1)
    else:
        fonk3(a1, b1)
def fonk2(a1, b1):
    print("Handling values less than $5.50...")
    b2 = a1 + b1
    b3 = (2.75 - (b2 % 2.75)) % 2.75
    print(f"To make your total balance divisible by $2.75, add at least: ${b3:.2f}")
def fonk3(a1, b1):
    print("Handling values $5.50 or greater...")
    b4 = b1 * 0.11
    b2 = a1 + b1 + b4
    print(f"With b4, the new value on the card is: ${b2:.2f}")
    b3 = (2.75 - (b2 % 2.75)) % 2.75
    b5 = [b3 + 2.75 * i for i in range(3)]
    print(f"To make your total balance divisible by $2.75, add one of the following amounts: {[f'${amt:.2f}' for amt in b5]}")
def fonk4():
    b6 = input("Is this a new card? (yes/no): ").strip().lower()
    if b6 in ["yes", "y"]:
        a1 = 1.00
    else:
        a1 = float(input("What is the value on your card now? "))
    fonk1(a1)
if b7 = = "__main__":
    fonk4()
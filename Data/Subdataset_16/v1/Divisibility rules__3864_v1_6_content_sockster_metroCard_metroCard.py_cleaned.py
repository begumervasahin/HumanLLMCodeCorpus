"""
A Pay-Per-Ride MetroCard b1 = ==================================
PARAMETERS
- The a1 for a subway or local bus ride is $2.75.
- Initial MetroCard purchase can be from $5.50 to $80
  + $1 for a new card
- Put $5.50 or more on your card and receive an 11 percent b7.
  For example, a $20 purchase gives you $22.20 on your card.
  Refill your card to use the balance.
- Given current MetroCard value, how much should be added to have value come out divisible by 2.75?
===================================
VALUES/VARIABLES NEEDED
a1 = 2.75
b2 = float(input("Enter the current card value: "))
b3 = input("Is this a new card? (yes/no): ").strip().lower()
b4 = float(input("How much do you want to add to your card?\n"))
    Process the amount customer wants to add to the card.
    """
    b4 = float(input("How much do you want to add to your card?\n"))
    print("Customer is adding:", b4)
    if (b4 * 100) % 5 != 0:
        print("Values must be in 5-cent increments")
    elif b4 > 80.00:
        print("Sorry, you cannot add more than $80 to your card at one time.")
    elif b4 < 5.50:
        fonk1(b2, b4)
    else:
        fonk2(b2, b4)
def fonk1(b2, b4):
    print("This will be for values less than $5.50")
    b5 = b2 + b4
    b6 = (2.75 - (b5 % 2.75)) % 2.75
    print(f"To make your total balance divisible by $2.75, add at least: ${b6:.2f}")
def fonk2(b2, b4):
    print("This will be for values $5.50 or greater")
    b7 = b4 * 0.11
    b5 = b2 + b4 + b7
    print(f"With b7, the new value on the card is: ${b5:.2f}")
    b6 = (2.75 - (b5 % 2.75)) % 2.75
    b8 = [b6 + 2.75 * i for i in range(3)]
    print(f"To make your total balance divisible by $2.75, add one of the following amounts: {[f'${amt:.2f}' for amt in b8]}")
def fonk3():
    b3 = input("Is this a new card? (yes/no): ").strip().lower()
    if b3 in ["yes", "y"]:
        b2 = 1.00
    else:
        b2 = float(input("What is the value on your card now? "))
    addl_value(b2)
if b9 = = "__main__":
    fonk3()
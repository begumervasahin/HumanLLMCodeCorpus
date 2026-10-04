
def add_value(card_value):
    cust_adding = float(input("How much do you want to add to your card?\n"))
    print("Customer is adding:", cust_adding)
    if (cust_adding * 100) % 5 != 0:
        print("Values must be in 5-cent increments")
    elif cust_adding > 80.00:
        print("Sorry, you cannot add more than $80 to your card at one time.")
    elif cust_adding < 5.50:
        handle_small_value(card_value, cust_adding)
    else:
        handle_large_value(card_value, cust_adding)
def handle_small_value(card_value, cust_adding):
    print("This will be for values less than $5.50")
    new_value = card_value + cust_adding
    amount_needed = (2.75 - (new_value % 2.75)) % 2.75
    print(f"To make your total balance divisible by $2.75, add at least: ${amount_needed:.2f}")
def handle_large_value(card_value, cust_adding):
    print("This will be for values $5.50 or greater")
    bonus = cust_adding * 0.11
    new_value = card_value + cust_adding + bonus
    print(f"With bonus, the new value on the card is: ${new_value:.2f}")
    amount_needed = (2.75 - (new_value % 2.75)) % 2.75
    next_amounts = [amount_needed + 2.75 * i for i in range(3)]
    print(f"To make your total balance divisible by $2.75, add one of the following amounts: {[f'${amt:.2f}' for amt in next_amounts]}")
def main():
    is_new_card = input("Is this a new card? (yes/no): ").strip().lower()
    if is_new_card in ["yes", "y"]:
        card_value = 1.00
    else:
        card_value = float(input("What is the value on your card now? "))
    add_value(card_value)
if __name__ == "__main__":
    main()
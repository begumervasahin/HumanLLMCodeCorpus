def get_user_input():
    cust_adding = float(input("How much money do you want to add to your card? Enter the amount:\n"))
    if (cust_adding * 1000) % 5 != 0:
        print("Error: Amount must be in 5-cent increments.")
    elif cust_adding > 80.00:
        print("Sorry, you cannot add more than $80 to your card at one time.")
    else:
        process_user_input(cust_adding)
def process_user_input(cust_adding):
    if cust_adding <= 5.50:
        add_small_value(cust_adding)
    else:
        add_big_value(cust_adding)
def add_small_value(cust_adding):
    print("For amounts less than or equal to $5.50:")
    min_amount = 2.75 - (cust_adding % 2.75)
    print(f"To make the total divisible by $2.75, add ${min_amount:.2f}")
def add_big_value(cust_adding):
    print("For amounts greater than $5.50:")
    card_value_1 = float(input("What is the current value on your card?\n"))
    print(f"Current card value: ${card_value_1:.2f}")
    card_value_final = card_value_1 + cust_adding
    print(f"Total card value after adding: ${card_value_final:.2f}")
    next_divisible = []
    for i in range(1, 4):
        amount = 2.75 * (card_value_final
        next_divisible.append(amount)
    print("Next 3 amounts divisible by $2.75:")
    for amount in next_divisible:
        print(f"${amount:.2f}")
if __name__ == "__main__":
    is_new_card = input("Is this a new card? (Y/N)\n").strip().lower()
    if is_new_card == "y":
        get_user_input()
    elif is_new_card == "n":
        card_value_1 = float(input("What is the current value on your card?\n"))
        get_user_input()
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
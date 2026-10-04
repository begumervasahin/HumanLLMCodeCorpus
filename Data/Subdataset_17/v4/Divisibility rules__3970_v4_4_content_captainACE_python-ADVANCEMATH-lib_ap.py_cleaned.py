def arithmetic_progression():
    print("This is an ARITHMETIC PROGRESSION module.")
    print("You can find the last number in a sequence or list of numbers.")
    print("To determine the last number, enter the first term, the common difference, and the number of terms in the AP.")
    try:
        first_term = int(input("Enter the first term of the number sequence: "))
        common_difference = int(input("Enter the common difference in the number sequence: "))
        number_of_terms = int(input("Enter the number of terms: "))
        last_term = first_term + (number_of_terms - 1) * common_difference
        print(f"The last term of the arithmetic progression is: {last_term}")
    except ValueError:
        print("Invalid input. Please enter valid integer values for the first term, common difference, and number of terms.")
if __name__ == "__main__":
    arithmetic_progression()
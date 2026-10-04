def calculate_last_term(first_term, common_difference, number_of_terms):
    return first_term + (number_of_terms - 1) * common_difference
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
def arithmetic_progression():
    print("This is an ARITHMETIC PROGRESSION module.")
    print("You can find the last number in a sequence or list of numbers.")
    print("To determine the last number, enter the first term, the common difference, and the number of terms in the AP.")
    first_term = get_positive_integer("Enter the first term of the number sequence: ")
    common_difference = get_positive_integer("Enter the common difference in the number sequence: ")
    number_of_terms = get_positive_integer("Enter the number of terms: ")
    last_term = calculate_last_term(first_term, common_difference, number_of_terms)
    print(f"The last term of the arithmetic progression is: {last_term}")
if __name__ == "__main__":
    arithmetic_progression()
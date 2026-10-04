def arithmetic_progression():
    print("This is an ARITHMETIC PROGRESSION module.")
    print("You can find the last number in a sequence or list of numbers.")
    print("To determine the last number, enter the first term of the AP and the common difference.")
    try:
        a = int(input("First term of the number sequence: "))
        d = int(input("The common difference in the number sequence: "))
        n = int(input("Number of terms: "))
        last_term = a + (n - 1) * d
        print(f"The last term of the arithmetic progression is: {last_term}")
    except ValueError:
        print("Please enter valid integer values for the first term, common difference, and number of terms.")
if __name__ == "__main__":
    arithmetic_progression()
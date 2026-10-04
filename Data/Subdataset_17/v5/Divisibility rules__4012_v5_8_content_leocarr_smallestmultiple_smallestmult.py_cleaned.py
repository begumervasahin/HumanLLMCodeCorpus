def find_smallest_multiple(max_multiple):
    current = max_multiple
    while True:
        if all(current % i == 0 for i in range(1, max_multiple + 1)):
            return current
        current += max_multiple
def get_valid_max_multiple():
    while True:
        try:
            max_multiple = int(input("What is the max multiple? "))
            if max_multiple < 1:
                print("Please enter a positive integer greater than zero.")
            else:
                return max_multiple
        except ValueError:
            print("Please enter a valid integer.")
def main():
    print("Welcome to the Smallest Multiple Finder!")
    max_multiple = get_valid_max_multiple()
    smallest_multiple = find_smallest_multiple(max_multiple)
    print(f"The smallest number that is evenly divisible by all of the numbers from 1 to {max_multiple} is {smallest_multiple}")
if __name__ == "__main__":
    main()
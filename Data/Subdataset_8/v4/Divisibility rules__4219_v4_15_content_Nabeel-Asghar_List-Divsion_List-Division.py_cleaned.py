def find_divisible_numbers(list_a, list_b, threshold):
    divisible_numbers = []
    for num_a in list_a:
        count = sum(1 for num_b in list_b if num_a % num_b == 0)
        if count >= threshold:
            divisible_numbers.append(num_a)
    return set(divisible_numbers)
def main():
    list_a_input = input("Enter a list of numbers separated by a space: ")
    list_a = list(map(int, list_a_input.split()))
    list_b_input = input("Enter another list of numbers separated by a space: ")
    list_b = list(map(int, list_b_input.split()))
    threshold = len(list_b)
    divisible_numbers = find_divisible_numbers(list_a, list_b, threshold)
    print("Numbers in list A that are divisible by at least half of list B:", divisible_numbers)
    input("Press any key to exit.")
if __name__ == "__main__":
    main()
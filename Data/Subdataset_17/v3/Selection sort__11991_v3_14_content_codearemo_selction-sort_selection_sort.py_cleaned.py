def selection_sort(items):
    n = len(items)
    for step in range(n):
        min_idx = step
        for location in range(step + 1, n):
            if items[location] < items[min_idx]:
                min_idx = location
        items[step], items[min_idx] = items[min_idx], items[step]
    return items
def get_user_input():
    try:
        user_input = input("Enter the numbers to be sorted, separated by spaces: ")
        number_list = [int(x) for x in user_input.split()]
        return number_list
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")
        return []
def main():
    number_list = get_user_input()
    if number_list:
        sorted_list = selection_sort(number_list)
        print("Sorted list:", sorted_list)
        print("Total number of items:", len(sorted_list))
if __name__ == "__main__":
    main()
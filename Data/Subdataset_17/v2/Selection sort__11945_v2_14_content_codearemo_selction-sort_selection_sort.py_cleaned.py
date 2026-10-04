def selection_sort(items):
    n = len(items)
    for step in range(n):
        min_idx = step
        for location in range(step + 1, n):
            if items[location] < items[min_idx]:
                min_idx = location
        items[step], items[min_idx] = items[min_idx], items[step]
    print("Sorted items:", items)
    print("Total number of items:", len(items))
    return items
def main():
    try:
        user_input = input("Enter the numbers to be sorted, separated by spaces: ")
        number_list = [int(x) for x in user_input.split()]
        selection_sort(number_list)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")
if __name__ == "__main__":
    main()
def selection_sort(items):
    for step in range(len(items)):
        location_of_largest = step
        for location in range(step, len(items)):
            if items[location_of_largest] < items[location]:
                location_of_largest = location
        if location_of_largest != step:
            items[step], items[location_of_largest] = items[location_of_largest], items[step]
    print("Sorted items:", items)
    print("Total number of items:", len(items))
try:
    l = input("Enter a list of integers separated by spaces: ").split()
    l = [int(x) for x in l]
    selection_sort(l)
except ValueError:
    print("Invalid input. Please enter a list of integers.")
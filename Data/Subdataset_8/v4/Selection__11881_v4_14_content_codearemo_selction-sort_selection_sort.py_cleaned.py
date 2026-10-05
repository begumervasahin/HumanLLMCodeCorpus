def selection_sort(items):
    for step in range(len(items)):
        location_of_smallest = step
        for location in range(step, len(items)):
            if items[location] < items[location_of_smallest]:
                location_of_smallest = location
        items[step], items[location_of_smallest] = items[location_of_smallest], items[step]
    print("Sorted items:", items)
    print("Total number of items:", len(items))
items = [64, 25, 12, 22, 11]
selection_sort(items)
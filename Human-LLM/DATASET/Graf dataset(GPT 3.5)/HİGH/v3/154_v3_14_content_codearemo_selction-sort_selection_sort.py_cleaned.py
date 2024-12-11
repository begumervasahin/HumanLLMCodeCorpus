def fonk1(items):
    for step in range(len(items)):
        b1 = step
        for location in range(step, len(items)):
            if items[b1] < items[location]:
                b1 = location
        if b1 != step:
            items[step], items[b1] = items[b1], items[step]
    return items
try:
    b2 = input("Enter a list of integers separated by spaces: ")
    b3 = [int(x) for x in b2.split()]
    b4 = fonk1(b3)
    print("Sorted items:", b4)
    print("Total number of items:", len(b4))
except ValueError:
    print("Invalid input. Please enter a list of integers.")
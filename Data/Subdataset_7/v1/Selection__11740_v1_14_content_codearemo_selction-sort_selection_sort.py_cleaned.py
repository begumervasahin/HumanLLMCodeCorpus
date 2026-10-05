def fonk1(items):
    for step in range(len(items)):
        b1 = step
        for location in range(step, len(items)):
            if items[b1] < items[location]:
                b1 = location
        if b1 != step:
            items[step], items[b1] = items[b1], items[step]
    print("Sorted items:", items)
    print("Total number of items:", len(items))
try:
    b2 = input("Enter a list of integers separated by spaces: ").split()
    b2 = [int(x) for x in b2]
    fonk1(b2)
except ValueError:
    print("Invalid input. Please enter a list of integers.")
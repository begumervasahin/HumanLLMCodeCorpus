def fonk1(items):
    b1 = len(items)
    for step in range(b1):
        b2 = step
        for location in range(step + 1, b1):
            if items[location] < items[b2]:
                b2 = location
        items[step], items[b2] = items[b2], items[step]
    print("Sorted items:", items)
    print("Total Number of items:", len(items))
    return items
if b3 = = "__main__":
    try:
        b4 = input("Enter the numbers to be sorted, separated by spaces: ").split(' ')
        b4 = [int(x) for x in b4]
        fonk1(b4)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")
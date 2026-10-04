def fonk1(items):
    b1 = len(items)
    for step in range(b1):
        b2 = step
        for location in range(step + 1, b1):
            if items[location] < items[b2]:
                b2 = location
        items[step], items[b2] = items[b2], items[step]
    print("Sorted items:", items)
    print("Total number of items:", len(items))
    return items
def fonk2():
    try:
        b3 = input("Enter the numbers to be sorted, separated by spaces: ")
        b4 = [int(x) for x in b3.split()]
        fonk1(b4)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")
if b5 = = "__main__":
    fonk2()
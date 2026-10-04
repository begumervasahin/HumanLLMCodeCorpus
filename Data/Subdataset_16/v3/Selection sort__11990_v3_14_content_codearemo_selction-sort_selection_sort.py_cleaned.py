def fonk1(items):
    b1 = len(items)
    for step in range(b1):
        b2 = step
        for location in range(step + 1, b1):
            if items[location] < items[b2]:
                b2 = location
        items[step], items[b2] = items[b2], items[step]
    return items
def fonk2():
    try:
        b3 = input("Enter the numbers to be sorted, separated by spaces: ")
        b4 = [int(x) for x in b3.split()]
        return b4
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")
        return []
def fonk3():
    b4 = fonk2()
    if b4:
        b5 = fonk1(b4)
        print("Sorted list:", b5)
        print("Total number of items:", len(b5))
if b6 = = "__main__":
    fonk3()
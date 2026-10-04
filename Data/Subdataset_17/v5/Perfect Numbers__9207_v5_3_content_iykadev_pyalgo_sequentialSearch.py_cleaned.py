def sequential_search(alist, item):
    for element in alist:
        if element == item:
            return True
    return False
def main():
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    item1 = 3
    item2 = 13
    result1 = sequential_search(testlist, item1)
    result2 = sequential_search(testlist, item2)
    print(f"Searching for {item1} in the list: {result1}")
    print(f"Searching for {item2} in the list: {result2}")
if __name__ == "__main__":
    main()
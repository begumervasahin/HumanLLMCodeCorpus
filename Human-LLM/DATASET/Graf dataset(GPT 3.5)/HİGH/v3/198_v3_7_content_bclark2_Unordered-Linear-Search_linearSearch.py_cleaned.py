def fonk1(unordered_list, b1):
    for index, item in enumerate(unordered_list):
        if b1 = = item:
            return f'Search item {b1} found at index {index}'
    return f'Search item {b1} not found in the list'
b2 = [5, 87, 2, 100, -1, 22, 4000, 34, 23, 19, 567]
print(fonk1(b2, -100))
print(fonk1(b2, 5))
print(fonk1(b2, 567))
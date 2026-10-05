def fonk1(unordered_list, b1):
    for index, item in enumerate(unordered_list):
        if b1 = = item:
            b2 = (
                f'Index of the searched item: {index}\n'
                f'Number you searched for: {b1}\n'
            )
            return b2
    b3 = f'The number {b1} was not found in the list.\n'
    return b3
b4 = [5, 87, 2, 100, -1, 22, 4000, 34, 23, 19, 567]
print(fonk1(b4, -100))
print(fonk1(b4, 5))
print(fonk1(b4, 567))
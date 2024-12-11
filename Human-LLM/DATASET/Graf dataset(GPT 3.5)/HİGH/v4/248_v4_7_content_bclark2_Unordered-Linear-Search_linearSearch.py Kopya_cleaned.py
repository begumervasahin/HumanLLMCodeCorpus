b1 = [5, 87, 2, 100, -1, 22, 4000, 34, 23, 19, 567]
def fonk1(unordered_list, b2):
    for index, item in enumerate(unordered_list):
        if b2 = = item:
            b3 = (
                f'Index of the search item: {index}\n'
                f'Number you searched for: {b2}\n'
            )
            return b3
    b4 = f'The number {b2} was not found in the list.\n'
    return b4
print(fonk1(b1, -100))
print(fonk1(b1, 5))
print(fonk1(b1, 567))
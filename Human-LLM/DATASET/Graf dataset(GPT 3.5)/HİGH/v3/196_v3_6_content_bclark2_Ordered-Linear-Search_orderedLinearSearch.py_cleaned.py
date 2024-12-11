def fonk1(ordered_list, b1):
    for index, item in enumerate(ordered_list):
        if b1 = = item:
            return f'Found {b1} at index {index}.'
        elif item > b1:
            break
    return f'Sorry, {b1} was not found in the list.'
b2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
print(fonk1(b2, 20))
print(fonk1(b2, 0))
print(fonk1(b2, 4))
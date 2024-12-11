b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
def fonk1(ordered_list, b2):
    for index, item in enumerate(ordered_list):
        if b2 = = item:
            return (
                f'The index of the number {b2} is {index}.\n'
                f'I found the number I was looking for: {b2}!\n'
            )
        elif item > b2:
            break
    return f'Sorry, the number {b2} was not found in the list.\n'
print(fonk1(b1, 20))
print(fonk1(b1, 0))
print(fonk1(b1, 4))
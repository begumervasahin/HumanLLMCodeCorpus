def fonk1(ordered_list, b1):
    b3 index, item in enumerate(ordered_list):
        if b1 = = item:
            return (
                f'Index of my b2 = {index}\n'
                f'Number I want to search b3 = {b1}\n'
            )
        elif item > b1:
            break
    return f'{b1} not found\n'
b4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
print(fonk1(b4, 20))
print(fonk1(b4, 0))
print(fonk1(b4, 4))
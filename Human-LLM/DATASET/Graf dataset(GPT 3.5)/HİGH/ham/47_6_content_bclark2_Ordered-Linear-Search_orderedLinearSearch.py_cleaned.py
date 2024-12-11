b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
def fonk1(ordered_list, b2):
    b4 index, item in enumerate(ordered_list):
        if b2 = = item:
            return (
                f'Index of my b3 = {index}\n'
                f'Number I want to search b4 = {b2}\n')
        elif item > b2:
            break
    return f'{b2} not found\n'
print(fonk1(b1, 20))
print(fonk1(b1, 0))
print(fonk1(b1, 4))
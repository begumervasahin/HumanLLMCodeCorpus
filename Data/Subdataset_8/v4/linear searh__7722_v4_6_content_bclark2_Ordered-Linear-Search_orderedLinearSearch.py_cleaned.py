my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
def search(ordered_list, term):
    for index, item in enumerate(ordered_list):
        if term == item:
            return (
                f'The index of the number {term} is {index}.\n'
                f'I found the number I was looking for: {term}!\n'
            )
        elif item > term:
            break
    return f'Sorry, the number {term} was not found in the list.\n'
print(search(my_list, 20))
print(search(my_list, 0))
print(search(my_list, 4))
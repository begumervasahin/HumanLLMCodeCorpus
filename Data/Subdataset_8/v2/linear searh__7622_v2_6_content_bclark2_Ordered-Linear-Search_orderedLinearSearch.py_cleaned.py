def search(ordered_list, term):
    for index, item in enumerate(ordered_list):
        if term == item:
            return (
                f'Found the number {term} at index {index}.\n'
                f'Searching for: {term}\n'
            )
        elif item > term:
            break
    return f'Sorry, {term} was not found in the list.\n'
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
print(search(my_list, 20))
print(search(my_list, 0))
print(search(my_list, 4))
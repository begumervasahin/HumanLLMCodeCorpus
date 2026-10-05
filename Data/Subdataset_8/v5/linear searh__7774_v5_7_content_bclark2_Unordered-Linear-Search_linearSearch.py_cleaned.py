def search_in_list(unordered_list, term):
    for index, item in enumerate(unordered_list):
        if term == item:
            result = (
                f'Index of the searched item: {index}\n'
                f'Number you searched for: {term}\n'
            )
            return result
    not_found_message = f'The number {term} was not found in the list.\n'
    return not_found_message
mylist = [5, 87, 2, 100, -1, 22, 4000, 34, 23, 19, 567]
print(search_in_list(mylist, -100))
print(search_in_list(mylist, 5))
print(search_in_list(mylist, 567))
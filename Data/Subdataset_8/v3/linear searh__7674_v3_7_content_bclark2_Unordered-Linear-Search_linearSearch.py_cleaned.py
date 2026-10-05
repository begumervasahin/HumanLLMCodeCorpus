def search(unordered_list, term):
    for index, item in enumerate(unordered_list):
        if term == item:
            return f'Search item {term} found at index {index}'
    return f'Search item {term} not found in the list'
mylist = [5, 87, 2, 100, -1, 22, 4000, 34, 23, 19, 567]
print(search(mylist, -100))
print(search(mylist, 5))
print(search(mylist, 567))
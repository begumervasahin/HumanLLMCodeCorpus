def search(unordered_list, term):
    for index, item in enumerate(unordered_list):
        if term == item:
            return (
                f'Index of search item = {index}\n'
                f'Number you searched for = {term}\n')
    return f'{term} not found\n'
mylist = [5, 87, 2, 100, -1, 22, 4000, 34, 23, 19, 567]
print(search(mylist, -100))
print(search(mylist, 5))
print(search(mylist, 567))
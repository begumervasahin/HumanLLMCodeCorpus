import sys
def recursive_func(the_list, indent=False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            recursive_func(each_item, indent, level + 1, fh)
        else:
            if indent:
                print('\t' * level, end='', file=fh)
            print(each_item, file=fh)
if __name__ == '__main__':
    example_list = [
        'a',
        ['b', 'c', ['d', 'e', 'f']],
        ['g', 'h'],
        'i'
    ]
    recursive_func(example_list, indent=True)
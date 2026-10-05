import sys
def print_nested_list(nested_list, indent=False, level=0, output=sys.stdout):
    for item in nested_list:
        if isinstance(item, list):
            print_nested_list(item, indent, level + 1, output)
        else:
            if indent:
                print("\t" * level, end='', file=output)
            print(item, file=output)
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
print_nested_list(nested_list, indent=True)
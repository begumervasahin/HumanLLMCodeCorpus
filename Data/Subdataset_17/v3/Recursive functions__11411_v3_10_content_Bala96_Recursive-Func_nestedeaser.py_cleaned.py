import sys
def recursive_func(the_list, indent=False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            recursive_func(each_item, indent, level + 1, fh)
        else:
            if indent:
                print("\t" * level, end='', file=fh)
            print(each_item, file=fh)
def main():
    nested_list = [
        "level 1 - item 1",
        ["level 2 - item 1", "level 2 - item 2",
         ["level 3 - item 1", "level 3 - item 2"]],
        "level 1 - item 2",
        ["level 2 - item 3",
         ["level 3 - item 3", "level 3 - item 4"]]
    ]
    print("Without indentation:")
    recursive_func(nested_list)
    print("\nWith indentation:")
    recursive_func(nested_list, indent=True)
if __name__ == '__main__':
    main()
import sys
def recursive_print(the_list, indent=False, level=0, fh=sys.stdout):
    for item in the_list:
        if isinstance(item, list):
            recursive_print(item, indent, level + 1, fh)
        else:
            if indent:
                print("\t" * level, end='', file=fh)
            print(item, file=fh)
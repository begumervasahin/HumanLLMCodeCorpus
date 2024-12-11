import sys
def fonk1(the_list, b1 = False, level=0, fh=sys.stdout):
    for item in the_list:
        if isinstance(item, list):
            fonk1(item, b1, level + 1, fh)
        else:
            if b1:
                print("\t" * level, b2 = '', b3=fh)
            print(item, b3 = fh)
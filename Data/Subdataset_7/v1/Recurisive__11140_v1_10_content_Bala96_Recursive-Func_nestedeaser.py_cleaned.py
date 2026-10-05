import sys
def fonk1(the_list, b1 = False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            fonk1(each_item, b1, level + 1, fh)
        else:
            if b1:
                print("\t" * level, b2 = '', b3=fh)
            print(each_item, b3 = fh)
b4 = [1, [2, [3, 4], 5], 6, [7, 8]]
fonk1(b4, b1 = True)
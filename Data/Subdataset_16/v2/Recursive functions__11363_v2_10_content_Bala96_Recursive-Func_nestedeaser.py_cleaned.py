import sys
def fonk1(the_list, b1 = False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            fonk1(each_item, b1, level + 1, fh)
        else:
            if b1:
                print("\t" * level, b2 = '', b3=fh)
            print(each_item, b3 = fh)
if b4 = = '__main__':
    b5 = [
        "level 1 - item 1",
        ["level 2 - item 1", "level 2 - item 2",
         ["level 3 - item 1", "level 3 - item 2"]],
        "level 1 - item 2",
        ["level 2 - item 3",
         ["level 3 - item 3", "level 3 - item 4"]]
    ]
    print("Without indentation:")
    fonk1(b5)
    print("\nWith indentation:")
    fonk1(b5, b1 = True)
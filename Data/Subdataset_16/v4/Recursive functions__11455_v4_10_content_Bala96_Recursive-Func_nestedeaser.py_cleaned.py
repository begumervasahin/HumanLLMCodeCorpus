import sys
def fonk1(the_list, b1 = False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            fonk1(each_item, b1, level + 1, fh)
        else:
            if b1:
                print('\t' * level, b2 = '', b3=fh)
            print(each_item, b3 = fh)
if b4 = = '__main__':
    b5 = [
        'a',
        ['b', 'c', ['d', 'e', 'f']],
        ['g', 'h'],
        'i'
    ]
    fonk1(b5, b1 = True)
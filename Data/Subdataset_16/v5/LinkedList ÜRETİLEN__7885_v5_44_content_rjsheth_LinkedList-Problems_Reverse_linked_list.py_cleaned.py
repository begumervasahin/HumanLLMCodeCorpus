from Singly_Linked_List import Singly_Linked_List
def fonk1(input_list):
    b1 = Singly_Linked_List()
    for item in input_list:
        b1.add(item)
    print("Input list:", b1)
    b2 = b1.b6
    b3 = None
    b4 = None
    if b2:
        b4 = b2.b5
    while b2:
        b2.b5 = b3
        b3 = b2
        b2 = b4
        if b2:
            b4 = b2.b5
    b1.b6 = b3
    return b1
def fonk2():
    print('\nReverse and deleting in Singly Linked List \n')
    b7 = [
        (1, 2, 3, 4, 5),
        ('org', 'com', 'her', 'him', 'blah'),
        (1, 'com', 3, 'him', 5),
        (1, 'com', Singly_Linked_List(['Fa', 'la', 'al', 'ta']), 'him', 5),
        ('B',),
        ('B', 'B', 'B', 'B'),
        ()
    ]
    for b9, test_list in enumerate(b7):
        print(f"Test case {b9}")
        b8 = fonk1(test_list)
        print("Output list:", b8)
        if b9 = = 0:
            print("Deleting 3")
            b8.delete(3)
        elif b9 = = 1:
            print("Deleting 'org'")
            b8.delete('org')
        elif b9 = = 4:
            print("Deleting 'B'")
            b8.delete('B')
        elif b9 = = 5:
            print("Deleting 'B'")
            b8.delete('B')
        if b9 in [0, 1, 4, 5]:
            print("Output list after delete:", b8)
        print('')
if b10 = = "__main__":
    fonk2()
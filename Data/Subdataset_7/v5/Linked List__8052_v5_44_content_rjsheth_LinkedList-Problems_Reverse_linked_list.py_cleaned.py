from Singly_Linked_List import Singly_Linked_List
def fonk1(input_list):
    b1 = Singly_Linked_List()
    for item in input_list:
        b1.add(item)
    print("Input list:", b1)
    b2 = None
    b3 = b1.b6
    while b3:
        b4 = b3.b5
        b3.b5 = b2
        b2 = b3
        b3 = b4
    b1.b6 = b2
    return b1
def fonk2():
    print('\nReverse and deleting in Singly Linked List \n')
    b7 = (1, 2, 3, 4, 5)
    b8 = fonk1(b7)
    print("Output list:", b8)
    print("Deleting 3")
    b8.delete(3)
    print("Output list after delete:", b8)
    print('')
    b9 = ('org', 'com', 'her', 'him', 'blah')
    b10 = fonk1(b9)
    print("Output list:", b10)
    print("Deleting 'org'")
    b10.delete('org')
    print("Output list after delete:", b10)
    print('')
    b11 = (1, 'com', 3, 'him', 5)
    b12 = fonk1(b11)
    print("Output list:", b12)
    print('')
    b13 = Singly_Linked_List()
    b13.add('Fa')
    b13.add('la')
    b13.add('al')
    b13.add('ta')
    b14 = (1, 'com', b13, 'him', 5)
    b15 = fonk1(b14)
    print("Output list:", b15)
    print('')
    b16 = ('B',)
    b17 = fonk1(b16)
    print("Output list:", b17)
    print("Deleting 'B'")
    b17.delete('B')
    print("Output list after delete:", b17)
    print('')
    b18 = ('B', 'B', 'B', 'B')
    b19 = fonk1(b18)
    print("Output list:", b19)
    print("Deleting 'B'")
    b19.delete('B')
    print("Output list after delete:", b19)
    print('')
    b20 = ()
    b21 = fonk1(b20)
    print("Output list:", b21)
    print('')
if b22 = = "__main__":
    fonk2()
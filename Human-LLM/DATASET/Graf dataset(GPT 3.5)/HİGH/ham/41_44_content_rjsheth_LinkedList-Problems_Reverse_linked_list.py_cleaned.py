from Singly_Linked_List import *
def fonk1(list):
    b1 = Singly_Linked_List()
    for i in list:
        b1.add(i)
    print("input list: ", b1)
    b2 = b1.b6
    b3 = None
    b4 = None
    if(b2 != None):
        b4 = b2.b5
    while(b2 != None):
        b2.b5 = b3
        b3 = b2
        b2 = b4
        if(b2 != None):
            b4 = b2.b5
    b1.b6 = b3
    return b1
print('\nReverse and deleting in Singly Linked List \n')
b7 = (1,2,3,4,5)
b8 = fonk1(b7)
print("output list: ",b8)
print("deleting 3")
b8.delete(3)
print("output list after delete: ",b8)
print('')
b9 = ('org','com','her','him','blah')
b10 = fonk1(b9)
print("output list: ",b10)
print("deleting 'org'")
b10.delete('org')
print("output list after delete: ",b10)
print('')
b11 = (1,'com',3,'him',5)
b12 = fonk1(b11)
print("output list: ",b12)
print('')
b13 = Singly_Linked_List()
b13.add('Fa')
b13.add('la')
b13.add('al')
b13.add('ta')
b14 = (1,'com',b13,'him',5)
b15 = fonk1(b14)
print("output list: ",b15)
print('')
b16 = ('B')
b17 = fonk1(b16)
print("output list: ",b17)
print("deleting 'B'")
b17.delete('B')
print("output list after delete: ",b17)
print('')
b18 = ('B','B','B','B')
b19 = fonk1(b18)
print("output list: ",b19)
print("deleting 'B'")
b19.delete('B')
print("output list after delete: ",b19)
print('')
b20 = ()
b21 = fonk1(b20)
print("output list: ",b21)
print('')
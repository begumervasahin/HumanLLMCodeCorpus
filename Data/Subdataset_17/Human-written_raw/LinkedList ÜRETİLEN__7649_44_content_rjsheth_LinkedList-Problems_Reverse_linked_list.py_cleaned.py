from Singly_Linked_List import *
def reverse_list(list):
    l = Singly_Linked_List()
    for i in list:
        l.add(i)
    print("input list: ", l)
    currNode = l.head
    prevNode = None
    nextNode = None
    if(currNode != None):
        nextNode = currNode.next
    while(currNode != None):
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
        if(currNode != None):
            nextNode = currNode.next
    l.head = prevNode
    return l
print('\nReverse and deleting in Singly Linked List \n')
test_list0 = (1,2,3,4,5)
returned_test0 = reverse_list(test_list0)
print("output list: ",returned_test0)
print("deleting 3")
returned_test0.delete(3)
print("output list after delete: ",returned_test0)
print('')
test_list1 = ('org','com','her','him','blah')
returned_test1 = reverse_list(test_list1)
print("output list: ",returned_test1)
print("deleting 'org'")
returned_test1.delete('org')
print("output list after delete: ",returned_test1)
print('')
test_list2 = (1,'com',3,'him',5)
returned_test2 = reverse_list(test_list2)
print("output list: ",returned_test2)
print('')
lp = Singly_Linked_List()
lp.add('Fa')
lp.add('la')
lp.add('al')
lp.add('ta')
test_list3 = (1,'com',lp,'him',5)
returned_test3 = reverse_list(test_list3)
print("output list: ",returned_test3)
print('')
test_list4 = ('B')
returned_test4 = reverse_list(test_list4)
print("output list: ",returned_test4)
print("deleting 'B'")
returned_test4.delete('B')
print("output list after delete: ",returned_test4)
print('')
test_list5 = ('B','B','B','B')
returned_test5 = reverse_list(test_list5)
print("output list: ",returned_test5)
print("deleting 'B'")
returned_test5.delete('B')
print("output list after delete: ",returned_test5)
print('')
test_list6 = ()
returned_test6 = reverse_list(test_list6)
print("output list: ",returned_test6)
print('')
from linkedLists import class1
from linkedLists import class2
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
a1 = 0
b1 = TestLogger("SingleLinkedListTest.txt")
b1.log_to_both("Testing class class1", b1.test_log_level_always)
b2 = TestLinkedList(class1, b1.test_log)
a1 += b2.test_all()
if a1 = = 0:
    b3 = "class1 TEST PASSED with "+str(a1)+" errors"
else:
    b3 = "class1 TEST FAILED with "+str(a1)+" errors"
b1.log_to_both(b3, b1.test_log_level_error)
b1.close_test_log()
del b2
a1 = 0
b1.open_test_log("DoubleLinkedListTest.txt")
b1.log_to_both("Testing class class2", b1.test_log_level_always)
b2 = TestLinkedList(class2, b1.test_log)
a1 += b2.test_push()
a1 += b2.test_pop()
a1 += b2.test_shift()
a1 += b2.test_unshift()
a1 += b2.test_contains()
a1 += b2.test_remove()
if a1 = = 0:
    b3 = "class2 TEST PASSED with "+str(a1)+" errors"
else:
    b3 = "class2 TEST FAILED with "+str(a1)+" errors"
b1.log_to_both(b3, b1.test_log_level_error)
b1.close_test_log()
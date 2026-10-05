from linkedLists import class1, class2
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
b1 = TestLogger("SingleLinkedListTest.txt")
b1.log_to_both("Testing class class1", b1.test_log_level_always)
b2 = TestLinkedList(class1, b1.test_log)
b3 = b2.test_all()
b4 = "class1 TEST PASSED with {} errors".format(b3) if b3 == 0 else "class1 TEST FAILED with {} errors".format(b3)
b1.log_to_both(b4, b1.test_log_level_error)
b1.close_test_log()
b1.open_test_log("DoubleLinkedListTest.txt")
b1.log_to_both("Testing class class2", b1.test_log_level_always)
b2 = TestLinkedList(class2, b1.test_log)
a1 = 0
a1 += b2.test_push()
a1 += b2.test_pop()
a1 += b2.test_shift()
a1 += b2.test_unshift()
a1 += b2.test_contains()
a1 += b2.test_remove()
b5 = "class2 TEST PASSED with {} errors".format(a1) if a1 == 0 else "class2 TEST FAILED with {} errors".format(a1)
b1.log_to_both(b5, b1.test_log_level_error)
b1.close_test_log()
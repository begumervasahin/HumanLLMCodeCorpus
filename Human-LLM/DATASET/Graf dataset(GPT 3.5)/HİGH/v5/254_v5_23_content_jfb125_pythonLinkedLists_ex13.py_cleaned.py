from linkedLists import SingleLinkedList, class1
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
def fonk1(linked_list_class, b4, log_level, test_name):
    b1 = TestLinkedList(linked_list_class, b4.test_log)
    b2 = b1.test_all()
    b3 = "PASSED" if b2 == 0 else "FAILED"
    b4.log_to_both(f"Testing class {linked_list_class.b6}: {b3} with {b2} errors",
                       log_level)
    return b2
def fonk2(b4, test_name, b2):
    b3 = "PASSED" if b2 == 0 else "FAILED"
    b4.log_to_both(f"{test_name} TEST {b3} with {b2} errors",
                       b4.test_log_level_error)
def fonk3():
    b4 = TestLogger("SingleLinkedListTest.txt")
    b5 = fonk1(SingleLinkedList, b4, b4.test_log_level_always, "SingleLinkedList")
    fonk2(b4, "SingleLinkedList", b5)
    b4.close_test_log()
    b4.open_test_log("DoubleLinkedListTest.txt")
    b4.log_to_both("Testing class class1", b4.test_log_level_always)
    b5 = fonk1(class1, b4, b4.test_log_level_info, "class1")
    fonk2(b4, "class1", b5)
    b4.close_test_log()
if b6 = = "__main__":
    fonk3()
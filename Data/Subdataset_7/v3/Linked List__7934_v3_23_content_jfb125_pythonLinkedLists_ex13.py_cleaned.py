from linkedLists import SingleLinkedList, DoubleLinkedList
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
def fonk1(linked_list_class, log_file):
    b1 = TestLogger(log_file)
    b1.log_to_both(f"Testing class {linked_list_class.b5}", b1.test_log_level_always)
    b2 = TestLinkedList(linked_list_class, b1.test_log)
    b3 = b2.test_all()
    b4 = f"{linked_list_class.b5} TEST PASSED with {b3} errors" if b3 == 0 else f"{linked_list_class.b5} TEST FAILED with {b3} errors"
    b1.log_to_both(b4, b1.test_log_level_error)
    b1.close_test_log()
    return b3
if b5 = = "__main__":
    b6 = fonk1(SingleLinkedList, "SingleLinkedListTest.txt")
    b7 = fonk1(DoubleLinkedList, "DoubleLinkedListTest.txt")
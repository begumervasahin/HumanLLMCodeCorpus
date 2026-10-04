from linkedLists import SingleLinkedList
from linkedLists import DoubleLinkedList
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
master_error_count = 0
logger = TestLogger("SingleLinkedListTest.txt")
logger.log_to_both("Testing class SingleLinkedList", logger.test_log_level_always)
tester = TestLinkedList(SingleLinkedList, logger.test_log)
master_error_count += tester.test_all()
if master_error_count == 0:
    test_out_string = "SingleLinkedList TEST PASSED with "+str(master_error_count)+" errors"
else:
    test_out_string = "SingleLinkedList TEST FAILED with "+str(master_error_count)+" errors"
logger.log_to_both(test_out_string, logger.test_log_level_error)
logger.close_test_log()
del tester
master_error_count = 0
logger.open_test_log("DoubleLinkedListTest.txt")
logger.log_to_both("Testing class DoubleLinkedList", logger.test_log_level_always)
tester = TestLinkedList(DoubleLinkedList, logger.test_log)
master_error_count += tester.test_push()
master_error_count += tester.test_pop()
master_error_count += tester.test_shift()
master_error_count += tester.test_unshift()
master_error_count += tester.test_contains()
master_error_count += tester.test_remove()
if master_error_count == 0:
    test_out_string = "DoubleLinkedList TEST PASSED with "+str(master_error_count)+" errors"
else:
    test_out_string = "DoubleLinkedList TEST FAILED with "+str(master_error_count)+" errors"
logger.log_to_both(test_out_string, logger.test_log_level_error)
logger.close_test_log()
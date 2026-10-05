from linkedLists import SingleLinkedList, DoubleLinkedList
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
logger = TestLogger("SingleLinkedListTest.txt")
logger.log_to_both("Testing class SingleLinkedList", logger.test_log_level_always)
tester = TestLinkedList(SingleLinkedList, logger.test_log)
error_count_single = tester.test_all()
test_result_single = "SingleLinkedList TEST PASSED with {} errors".format(error_count_single) if error_count_single == 0 else "SingleLinkedList TEST FAILED with {} errors".format(error_count_single)
logger.log_to_both(test_result_single, logger.test_log_level_error)
logger.close_test_log()
logger.open_test_log("DoubleLinkedListTest.txt")
logger.log_to_both("Testing class DoubleLinkedList", logger.test_log_level_always)
tester = TestLinkedList(DoubleLinkedList, logger.test_log)
error_count_double = 0
error_count_double += tester.test_push()
error_count_double += tester.test_pop()
error_count_double += tester.test_shift()
error_count_double += tester.test_unshift()
error_count_double += tester.test_contains()
error_count_double += tester.test_remove()
test_result_double = "DoubleLinkedList TEST PASSED with {} errors".format(error_count_double) if error_count_double == 0 else "DoubleLinkedList TEST FAILED with {} errors".format(error_count_double)
logger.log_to_both(test_result_double, logger.test_log_level_error)
logger.close_test_log()
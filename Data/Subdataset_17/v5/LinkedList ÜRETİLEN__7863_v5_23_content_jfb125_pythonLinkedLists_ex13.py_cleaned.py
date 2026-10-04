from linkedLists import SingleLinkedList, DoubleLinkedList
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
def run_tests():
    master_error_count = 0
    logger = TestLogger("SingleLinkedListTest.txt")
    logger.log_to_both("Testing class SingleLinkedList", logger.test_log_level_always)
    tester = TestLinkedList(SingleLinkedList, logger.test_log)
    master_error_count += tester.test_all()
    if master_error_count == 0:
        test_out_string = f"SingleLinkedList TEST PASSED with {master_error_count} errors"
    else:
        test_out_string = f"SingleLinkedList TEST FAILED with {master_error_count} errors"
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
        test_out_string = f"DoubleLinkedList TEST PASSED with {master_error_count} errors"
    else:
        test_out_string = f"DoubleLinkedList TEST FAILED with {master_error_count} errors"
    logger.log_to_both(test_out_string, logger.test_log_level_error)
    logger.close_test_log()
if __name__ == "__main__":
    run_tests()
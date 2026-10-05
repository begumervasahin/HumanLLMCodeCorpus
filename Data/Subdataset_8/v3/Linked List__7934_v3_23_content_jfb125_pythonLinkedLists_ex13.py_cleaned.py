from linkedLists import SingleLinkedList, DoubleLinkedList
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
def run_linked_list_tests(linked_list_class, log_file):
    logger = TestLogger(log_file)
    logger.log_to_both(f"Testing class {linked_list_class.__name__}", logger.test_log_level_always)
    tester = TestLinkedList(linked_list_class, logger.test_log)
    error_count = tester.test_all()
    test_result = f"{linked_list_class.__name__} TEST PASSED with {error_count} errors" if error_count == 0 else f"{linked_list_class.__name__} TEST FAILED with {error_count} errors"
    logger.log_to_both(test_result, logger.test_log_level_error)
    logger.close_test_log()
    return error_count
if __name__ == "__main__":
    single_linked_list_error_count = run_linked_list_tests(SingleLinkedList, "SingleLinkedListTest.txt")
    double_linked_list_error_count = run_linked_list_tests(DoubleLinkedList, "DoubleLinkedListTest.txt")
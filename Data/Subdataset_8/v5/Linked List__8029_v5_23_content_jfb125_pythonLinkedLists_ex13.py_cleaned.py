from linkedLists import SingleLinkedList, DoubleLinkedList
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
def run_tests(linked_list_class, logger, log_level, test_name):
    tester = TestLinkedList(linked_list_class, logger.test_log)
    error_count = tester.test_all()
    test_result = "PASSED" if error_count == 0 else "FAILED"
    logger.log_to_both(f"Testing class {linked_list_class.__name__}: {test_result} with {error_count} errors",
                       log_level)
    return error_count
def log_test_result(logger, test_name, error_count):
    test_result = "PASSED" if error_count == 0 else "FAILED"
    logger.log_to_both(f"{test_name} TEST {test_result} with {error_count} errors",
                       logger.test_log_level_error)
def main():
    logger = TestLogger("SingleLinkedListTest.txt")
    master_error_count = run_tests(SingleLinkedList, logger, logger.test_log_level_always, "SingleLinkedList")
    log_test_result(logger, "SingleLinkedList", master_error_count)
    logger.close_test_log()
    logger.open_test_log("DoubleLinkedListTest.txt")
    logger.log_to_both("Testing class DoubleLinkedList", logger.test_log_level_always)
    master_error_count = run_tests(DoubleLinkedList, logger, logger.test_log_level_info, "DoubleLinkedList")
    log_test_result(logger, "DoubleLinkedList", master_error_count)
    logger.close_test_log()
if __name__ == "__main__":
    main()
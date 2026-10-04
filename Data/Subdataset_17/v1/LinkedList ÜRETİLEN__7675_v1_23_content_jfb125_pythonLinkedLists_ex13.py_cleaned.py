class SingleLinkedList:
    pass
class DoubleLinkedList:
    pass
class TestLinkedList:
    def __init__(self, linked_list_class, log_func):
        self.linked_list_class = linked_list_class
        self.log_func = log_func
    def test_all(self):
        error_count = 0
        error_count += self.test_push()
        error_count += self.test_pop()
        error_count += self.test_shift()
        error_count += self.test_unshift()
        error_count += self.test_contains()
        error_count += self.test_remove()
        return error_count
    def test_push(self):
        return 0
    def test_pop(self):
        return 0
    def test_shift(self):
        return 0
    def test_unshift(self):
        return 0
    def test_contains(self):
        return 0
    def test_remove(self):
        return 0
class TestLogger:
    test_log_level_always = 1
    test_log_level_error = 2
    def __init__(self, filename):
        self.filename = filename
        self.log_file = open(filename, 'w')
    def log_to_both(self, message, level):
        self.log(message, level)
        print(message)
    def log(self, message, level):
        if level >= self.test_log_level_always:
            self.log_file.write(message + '\n')
    def close_test_log(self):
        self.log_file.close()
    def open_test_log(self, filename):
        self.log_file = open(filename, 'w')
from linkedLists import SingleLinkedList, DoubleLinkedList
from linkedListsTests import TestLinkedList
from testLogger import TestLogger
def main():
    master_error_count = 0
    logger = TestLogger("SingleLinkedListTest.txt")
    logger.log_to_both("Testing class SingleLinkedList", logger.test_log_level_always)
    tester = TestLinkedList(SingleLinkedList, logger.log)
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
    tester = TestLinkedList(DoubleLinkedList, logger.log)
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
    main()
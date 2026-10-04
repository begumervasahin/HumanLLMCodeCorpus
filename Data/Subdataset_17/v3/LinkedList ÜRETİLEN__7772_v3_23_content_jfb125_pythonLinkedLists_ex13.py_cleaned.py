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
        self.log_func("Running test_push", TestLogger.LOG_LEVEL_ALWAYS)
        return 0
    def test_pop(self):
        self.log_func("Running test_pop", TestLogger.LOG_LEVEL_ALWAYS)
        return 0
    def test_shift(self):
        self.log_func("Running test_shift", TestLogger.LOG_LEVEL_ALWAYS)
        return 0
    def test_unshift(self):
        self.log_func("Running test_unshift", TestLogger.LOG_LEVEL_ALWAYS)
        return 0
    def test_contains(self):
        self.log_func("Running test_contains", TestLogger.LOG_LEVEL_ALWAYS)
        return 0
    def test_remove(self):
        self.log_func("Running test_remove", TestLogger.LOG_LEVEL_ALWAYS)
        return 0
class TestLogger:
    LOG_LEVEL_ALWAYS = 1
    LOG_LEVEL_ERROR = 2
    def __init__(self, filename):
        self.filename = filename
        self.log_file = open(filename, 'w')
    def log_to_both(self, message, level):
        self.log(message, level)
        print(message)
    def log(self, message, level):
        if level >= self.LOG_LEVEL_ALWAYS:
            self.log_file.write(message + '\n')
    def close_log(self):
        self.log_file.close()
    def open_log(self, filename):
        self.log_file = open(filename, 'w')
def main():
    def run_tests(linked_list_class, log_filename):
        logger = TestLogger(log_filename)
        logger.log_to_both(f"Testing class {linked_list_class.__name__}", TestLogger.LOG_LEVEL_ALWAYS)
        tester = TestLinkedList(linked_list_class, logger.log)
        error_count = tester.test_all()
        test_result = "PASSED" if error_count == 0 else "FAILED"
        logger.log_to_both(f"{linked_list_class.__name__} TEST {test_result} with {error_count} errors", TestLogger.LOG_LEVEL_ERROR)
        logger.close_log()
        return error_count
    master_error_count = run_tests(SingleLinkedList, "SingleLinkedListTest.txt")
    master_error_count += run_tests(DoubleLinkedList, "DoubleLinkedListTest.txt")
if __name__ == "__main__":
    main()
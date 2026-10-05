from collections import deque
class ChameleonState:
    def __init__(self, red=0, green=0, blue=0):
        self._red_count = red
        self._green_count = green
        self._blue_count = blue
        self._parent = None
    @property
    def red_count(self):
        return self._red_count
    @property
    def green_count(self):
        return self._green_count
    @property
    def blue_count(self):
        return self._blue_count
    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, obj):
        self._parent = obj
    def has_only_one_color(self):
        return (self.red_count == 0 and self.green_count > 0 and self.blue_count == 0) or \
               (self.red_count == 0 and self.green_count == 0 and self.blue_count > 0) or \
               (self.red_count > 0 and self.green_count == 0 and self.blue_count == 0)
    def red_met_green(self):
        if self.red_count < 1 or self.green_count < 1:
            raise ValueError('Invalid red or green count')
        red_count = self.red_count - 1
        green_count = self.green_count - 1
        blue_count = self.blue_count + 2
        return ChameleonState(red_count, green_count, blue_count)
    def green_met_blue(self):
        if self.green_count < 1 or self.blue_count < 1:
            raise ValueError('Invalid green or blue count')
        red_count = self.red_count + 2
        green_count = self.green_count - 1
        blue_count = self.blue_count - 1
        return ChameleonState(red_count, green_count, blue_count)
    def blue_met_red(self):
        if self.red_count < 1 or self.blue_count < 1:
            raise ValueError('Invalid blue or red count')
        red_count = self.red_count - 1
        green_count = self.green_count + 2
        blue_count = self.blue_count - 1
        return ChameleonState(red_count, green_count, blue_count)
    def get_path(self):
        path = deque([str(self)])
        parent = self.parent
        while parent:
            path.appendleft(str(parent))
            parent = parent.parent
        return path
    def __str__(self):
        return f'(red={self.red_count}, green={self.green_count}, blue={self.blue_count})'
def run_algorithm_test(algorithm_name):
    test_filename = f'{algorithm_name}.test.py'
    print(f"Running test for {algorithm_name} algorithm...")
    try:
        exec(open(test_filename).read())
    except FileNotFoundError:
        print(f"Test file {test_filename} not found!")
def main():
    print("Welcome to the Chameleon Problem Solver!")
    print("This program simulates chameleons changing colors until they all become of the same color.")
    print("You can test the algorithms using the provided tests.")
    print("Running all tests...")
    algorithms = ["depth_first_search", "breadth_first_search", "a_star"]
    for algorithm in algorithms:
        run_algorithm_test(algorithm)
if __name__ == "__main__":
    main()
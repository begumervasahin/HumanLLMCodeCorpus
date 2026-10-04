from collections import defaultdict
import operator
class Driver:
    def __init__(self, modules):
        self._modules = modules
        self._intervals = []
        self._values = []
        self._print_module_headers()
    def _print_module_headers(self):
        print('Interval\t|\t', end='')
        for module in self._modules:
            print(f'{module}\t', end='')
        print('Winner')
    def set_module(self, index, value=None, interval=None):
        if index < len(self._modules):
            if value is not None:
                self._modules[index]._last_value = value
            if interval is not None:
                self._modules[index]._last_interval = interval
    def test(self, intervals):
        for interval in intervals:
            self._process_interval(interval)
    def run(self, interval):
        self._process_interval(interval)
    def _process_interval(self, interval):
        results = [module.get_result(interval) for module in self._modules]
        votes = defaultdict(int)
        print(f'{interval}\t|\t', end='')
        for result in results:
            print(f'{result}\t', end='')
            votes[result] += 1
        winner = max(votes.items(), key=operator.itemgetter(1))[0]
        print(winner)
        self._values.append(winner)
        self._intervals.append(interval)
        self._provide_feedback(results, winner)
    def _provide_feedback(self, results, winner):
        for i, module in enumerate(self._modules):
            feedback = {'status': 'ok'} if results[i] == winner else {'status': 'error', 'good_value': winner}
            module.receive_feedback(feedback)
class Module:
    def __init__(self, name):
        self.name = name
        self._last_value = None
        self._last_interval = None
    def get_result(self, interval):
        return interval % 3
    def receive_feedback(self, feedback):
        pass
    def __str__(self):
        return self.name
if __name__ == "__main__":
    modules = [Module("Module1"), Module("Module2"), Module("Module3")]
    driver = Driver(modules)
    driver.test([1, 2, 3, 4, 5])
    driver.run(6)
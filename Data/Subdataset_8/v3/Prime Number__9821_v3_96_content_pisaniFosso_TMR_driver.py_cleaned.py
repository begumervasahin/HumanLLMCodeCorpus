from collections import defaultdict
import operator
class Driver:
    def __init__(self, modules):
        self.modules = modules
        self.intervals = []
        self.values = []
        print('modules\t|\t', end='')
        for i, m in enumerate(modules):
            print(f"{m}\t", end='')
        print('Winner')
    def set_module(self, index, value=None, interval=None):
        if index < len(self.modules):
            if value is not None:
                self.modules[index].last_value = value
            if interval is not None:
                self.modules[index].last_interval = interval
    def test(self, intervals):
        for index, interval in enumerate(intervals):
            results = [module.get_result(interval) for module in self.modules]
            votes = defaultdict(int)
            print(f"{interval}\t|\t", end='')
            for res in results:
                print(f"{res}\t", end='')
                votes[res] += 1
            winner = max(votes.items(), key=operator.itemgetter(1))[0]
            print(winner)
            self.values.append(winner)
            self.intervals.append(interval)
            for i, module in enumerate(self.modules):
                if results[i] == winner:
                    module.receive_feedback({'status': 'ok'})
                else:
                    module.receive_feedback({'status': 'error', "goodValue": winner})
    def run(self, interval):
        results = [module.get_result(interval) for module in self.modules]
        votes = defaultdict(int)
        print(f"{interval}\t|\t", end='')
        for res in results:
            print(f"{res}\t", end='')
            votes[res] += 1
        winner = max(votes.items(), key=operator.itemgetter(1))[0]
        print(winner)
        self.values.append(winner)
        self.intervals.append(interval)
        for i, module in enumerate(self.modules):
            if results[i] == winner:
                module.receive_feedback({'status': 'ok'})
            else:
                module.receive_feedback({'status': 'error', "goodValue": winner})
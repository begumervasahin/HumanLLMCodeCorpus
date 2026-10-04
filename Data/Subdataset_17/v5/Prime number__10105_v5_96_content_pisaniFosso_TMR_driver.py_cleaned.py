from collections import defaultdict
import operator
class Driver:
    def __init__(self, modules):
        self._modules = modules
        self._intervals = []
        self._values = []
        self.print_modules()
    def print_modules(self):
        print('Modules\t|\t', end='')
        for module in self._modules:
            print(f'{module}\t', end='')
        print('Winner')
    def set_module(self, index, value=None, interval=None):
        if index < len(self._modules):
            if value is not None:
                self._modules[index]._lastValue = value
            if interval is not None:
                self._modules[index]._lastInterval = interval
    def test(self, intervals):
        for interval in intervals:
            self.run(interval)
    def run(self, interval):
        results = [module.getResult(interval) for module in self._modules]
        votes = self.count_votes(results)
        winner = self.get_winner(votes)
        self.print_results(interval, results, winner)
        self._values.append(winner)
        self._intervals.append(interval)
        self.give_feedback(results, winner)
    def count_votes(self, results):
        votes = defaultdict(int)
        for res in results:
            votes[res] += 1
        return votes
    def get_winner(self, votes):
        return max(votes.items(), key=operator.itemgetter(1))[0]
    def print_results(self, interval, results, winner):
        print(f'{interval}\t|\t', end='')
        for res in results:
            print(f'{res}\t', end='')
        print(winner)
    def give_feedback(self, results, winner):
        for i, module in enumerate(self._modules):
            feedback = {'status': 'ok'} if results[i] == winner else {'status': 'error', 'goodValue': winner}
            module.receiveFeedback(feedback)
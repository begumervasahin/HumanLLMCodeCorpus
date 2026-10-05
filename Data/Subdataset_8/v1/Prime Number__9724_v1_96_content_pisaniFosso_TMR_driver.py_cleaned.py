class Driver(object):
    def __init__(self, modules):
        self._modules = modules
        self._intervals = []
        self._values = []
        print('modules\t|\t', end='')
        for i, m in enumerate(modules):
            print(str(m) + '\t', end='')
        print('Winner')
    def setModule(self, i, value=None, interval=None):
        if i < len(self._modules):
            if value is not None:
                self._modules[i]._lastValue = value
            if interval is not None:
                self._modules[i]._lastInterval = interval
    def test(self, intervals):
        for index, interval in enumerate(intervals):
            results = [module.getResult(interval) for module in self._modules]
            from collections import defaultdict
            votes = defaultdict(int)
            print(str(interval) + '\t|\t', end='')
            for res in results:
                print(str(res) + '\t', end='')
                votes[res] += 1
            import operator
            winner = max(votes.items(), key=operator.itemgetter(1))[0]
            print(winner)
            self._values.append(winner)
            self._intervals.append(interval)
            for i, module in enumerate(self._modules):
                if results[i] == winner:
                    module.receiveFeedback({'status': 'ok'})
                else:
                    module.receiveFeedback({'status': 'error', "goodValue": winner})
    def run(self, interval):
        results = [module.getResult(interval) for module in self._modules]
        from collections import defaultdict
        votes = defaultdict(int)
        print(str(interval) + '\t|\t', end='')
        for res in results:
            print(str(res) + '\t', end='')
            votes[res] += 1
        import operator
        winner = max(votes.items(), key=operator.itemgetter(1))[0]
        print(winner)
        self._values.append(winner)
        self._intervals.append(interval)
        for i, module in enumerate(self._modules):
            if results[i] == winner:
                module.receiveFeedback({'status': 'ok'})
            else:
                module.receiveFeedback({'status': 'error', "goodValue": winner})
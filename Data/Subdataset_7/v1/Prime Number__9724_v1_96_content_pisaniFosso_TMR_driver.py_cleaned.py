class class1(object):
    def fonk1(self, modules):
        self.b1 = modules
        self.b2 = []
        self.b3 = []
        print('modules\t|\t', b4 = '')
        for i, m in enumerate(modules):
            print(str(m) + '\t', b4 = '')
        print('Winner')
    def fonk2(self, i, b5 = None, interval=None):
        if i < len(self.b1):
            if b5 is not None:
                self.b1[i].b6 = b5
            if interval is not None:
                self.b1[i].b7 = interval
    def fonk3(self, intervals):
        for index, interval in enumerate(intervals):
            b8 = [module.getResult(interval) for module in self.b1]
            from collections import defaultdict
            b9 = defaultdict(int)
            print(str(interval) + '\t|\t', b4 = '')
            for res in b8:
                print(str(res) + '\t', b4 = '')
                b9[res] += 1
            import operator
            b10 = max(b9.items(), key=operator.itemgetter(1))[0]
            print(b10)
            self.b3.append(b10)
            self.b2.append(interval)
            for i, module in enumerate(self.b1):
                if b8[i] == b10:
                    module.receiveFeedback({'status': 'ok'})
                else:
                    module.receiveFeedback({'status': 'error', "goodValue": b10})
    def fonk4(self, interval):
        b8 = [module.getResult(interval) for module in self.b1]
        from collections import defaultdict
        b9 = defaultdict(int)
        print(str(interval) + '\t|\t', b4 = '')
        for res in b8:
            print(str(res) + '\t', b4 = '')
            b9[res] += 1
        import operator
        b10 = max(b9.items(), key=operator.itemgetter(1))[0]
        print(b10)
        self.b3.append(b10)
        self.b2.append(interval)
        for i, module in enumerate(self.b1):
            if b8[i] == b10:
                module.receiveFeedback({'status': 'ok'})
            else:
                module.receiveFeedback({'status': 'error', "goodValue": b10})
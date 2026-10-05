from itertools import chain, combinations
class Apriori:
    @staticmethod
    def open_data(filename):
        f = open(filename, 'rU')
        for l in f:
            l = l.strip().rstrip(',')
            row = frozenset(l.split(','))
            yield row
    @staticmethod
    def itemset_from_data(data):
        itemset = set()
        transaction_list = list()
        for row in data:
            transaction_list.append(frozenset(row))
            for item in row:
                if item:
                    itemset.add(frozenset([item]))
        return itemset, transaction_list
    @staticmethod
    def itemset_support(transaction_list, itemset, min_support=0):
        len_transaction_list = len(transaction_list)
        l = [
            (item, float(sum(1 for row in transaction_list if item.issubset(row))) / len_transaction_list)
            for item in itemset
        ]
        return dict([(item, support) for item, support in l if support >= min_support])
    @staticmethod
    def frequent_itemset(transaction_list, c_itemset, min_support):
        f_itemset = dict()
        k = 1
        while True:
            if k > 1:
                c_itemset = Apriori.joinset(l_itemset, k)
            l_itemset = Apriori.itemset_support(transaction_list, c_itemset, min_support)
            if not l_itemset:
                break
            f_itemset.update(l_itemset)
            k += 1
        return f_itemset
    @staticmethod
    def joinset(itemset, k):
        return set([i.union(j) for i in itemset for j in itemset if len(i.union(j)) == k])
    @staticmethod
    def subsets(itemset):
        return chain(*[combinations(itemset, i + 1) for i, a in enumerate(itemset)])
    @staticmethod
    def get_rules(f_itemset, min_confidence, min_lift):
        rules = list()
        for item, support in f_itemset.items():
            if len(item) > 1:
                for antecedent in Apriori.subsets(item):
                    consequent = item.difference(antecedent)
                    if consequent:
                        antecedent = frozenset(antecedent)
                        XY = antecedent.union(consequent)
                        confidence = float(f_itemset[XY]) / f_itemset[antecedent]
                        lift = confidence / (f_itemset[antecedent] * f_itemset[consequent])
                        if confidence >= min_confidence:
                            if lift >= min_lift:
                                rules.append((antecedent, consequent, confidence, lift))
        return rules
    @staticmethod
    def generate_itemsets_rules(data, min_support, min_confidence, min_lift):
        csv = Apriori.open_data(data)
        itemset, transaction_list = Apriori.itemset_from_data(csv)
        f_itemset = Apriori.frequent_itemset(transaction_list, itemset, min_support)
        rules = Apriori.get_rules(f_itemset, min_confidence, min_lift)
        return rules
    @staticmethod
    def print_result(rules):
        print('--Rules--')
        for antecedent, consequent, confidence, lift in sorted(rules, key=lambda iterator: iterator[0]):
            print('RULES: {} => {} : {} : {}'.format(tuple(antecedent), tuple(consequent), round(confidence, 5),
                                                     round(lift, 3)))
class FPGrowth:
    @staticmethod
    def generate_patterns_rules(data, min_support, min_confidence):
        pass
    @staticmethod
    def print_result(rules):
        pass
def store_result(rules, frequent_itemset):
    rulesnew = []
    ant = []
    cons = []
    conf = []
    lift = []
    for antecedent, consequent, confidence, lift in sorted(rules, key=lambda iterator: iterator[0]):
        ant.append(tuple(antecedent))
        cons.append(tuple(consequent))
        conf.append(round(confidence, 4))
        lift.append(round(lift, 3))
    return ant, cons, conf, lift
def mine(csv, default_support=0.014, default_confidence=0.9, default_lift=1):
    rules = Apriori.generate_itemsets_rules(csv, default_support, default_confidence, default_lift)
    return store_result(rules, itemset)
if __name__ == "__main__":
    csv_file = "your_data.csv"
    antecedents, consequents, confidences, lifts = mine(csv_file)
    print("Antecedents:", antecedents)
    print("Consequents:", consequents)
    print("Confidences:", confidences)
    print("Lifts:", lifts)
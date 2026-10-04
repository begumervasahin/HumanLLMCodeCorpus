
import pandas as pd
from apyori import apriori
def load_dataset(file_path):
    dataset = pd.read_csv(file_path, header=None)
    transactions = [
        [str(dataset.values[i, j]) for j in range(dataset.shape[1])]
        for i in range(len(dataset))
    ]
    return transactions
def apply_apriori(transactions, min_support, min_confidence, min_lift, min_length):
    rules = apriori(
        transactions,
        min_support=min_support,
        min_confidence=min_confidence,
        min_lift=min_lift,
        min_length=min_length
    )
    return list(rules)
def display_rules(rules):
    for rule in rules:
        items = [item for item in rule.items]
        print(f"Rule: {items[:-1]} -> {items[-1]}")
        print(f"Support: {rule.support}")
        for ordered_stat in rule.ordered_statistics:
            print(f"Confidence: {ordered_stat.confidence}")
            print(f"Lift: {ordered_stat.lift}")
        print("")
def main():
    file_path = 'Market_Basket_Optimisation.csv'
    min_support = 0.003
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    transactions = load_dataset(file_path)
    rules = apply_apriori(transactions, min_support, min_confidence, min_lift, min_length)
    display_rules(rules)
if __name__ == "__main__":
    main()
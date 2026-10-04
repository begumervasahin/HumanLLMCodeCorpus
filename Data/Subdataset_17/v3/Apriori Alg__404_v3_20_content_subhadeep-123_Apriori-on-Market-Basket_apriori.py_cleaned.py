
import pandas as pd
from apyori import apriori
def load_data(filename):
    dataset = pd.read_csv(filename, header=None)
    transactions = [
        [str(dataset.values[i, j]) for j in range(dataset.shape[1]) if pd.notna(dataset.values[i, j])]
        for i in range(dataset.shape[0])
    ]
    return transactions
def train_apriori(transactions, min_support, min_confidence, min_lift, min_length):
    rules = apriori(
        transactions,
        min_support=min_support,
        min_confidence=min_confidence,
        min_lift=min_lift,
        min_length=min_length
    )
    return list(rules)
def visualize_rules(rules):
    for rule in rules:
        items = list(rule.items)
        support = rule.support
        ordered_stat = rule.ordered_statistics[0]
        confidence = ordered_stat.confidence
        lift = ordered_stat.lift
        print(f"Rule: {items}")
        print(f"Support: {support:.4f}")
        print(f"Confidence: {confidence:.4f}")
        print(f"Lift: {lift:.4f}")
        print("=====================================")
if __name__ == "__main__":
    filename = 'Market_Basket_Optimisation.csv'
    transactions = load_data(filename)
    min_support = 0.003
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    rules = train_apriori(transactions, min_support, min_confidence, min_lift, min_length)
    visualize_rules(rules)
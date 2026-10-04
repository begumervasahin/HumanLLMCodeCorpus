
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori
def load_transactions(file_path):
    dataset = pd.read_csv(file_path, header=None)
    transactions = []
    for i in range(len(dataset)):
        transaction = [str(dataset.values[i, j]) for j in range(dataset.shape[1]) if pd.notna(dataset.values[i, j])]
        transactions.append(transaction)
    return transactions
def generate_apriori_rules(transactions, min_support, min_confidence, min_lift, min_length):
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
        support = rule.support
        confidence = rule.ordered_statistics[0].confidence
        lift = rule.ordered_statistics[0].lift
        print(f"Rule: {items}")
        print(f"Support: {support:.4f}")
        print(f"Confidence: {confidence:.4f}")
        print(f"Lift: {lift:.4f}")
        print("-" * 20)
def plot_item_frequencies(rules):
    items = []
    supports = []
    for rule in rules:
        for item in rule.items:
            items.append(item)
            supports.append(rule.support)
    plt.figure(figsize=(10, 6))
    plt.bar(items, supports, color='blue')
    plt.xlabel('Items')
    plt.ylabel('Support')
    plt.title('Item Frequencies')
    plt.xticks(rotation=90)
    plt.show()
if __name__ == "__main__":
    file_path = 'F:
    transactions = load_transactions(file_path)
    min_support = 0.003
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    rules = generate_apriori_rules(transactions, min_support, min_confidence, min_lift, min_length)
    display_rules(rules)
    plot_item_frequencies(rules)
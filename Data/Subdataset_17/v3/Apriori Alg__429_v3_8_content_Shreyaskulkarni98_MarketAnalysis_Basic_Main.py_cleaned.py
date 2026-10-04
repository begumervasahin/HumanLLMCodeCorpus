import pandas as pd
from apyori import apriori
def load_dataset(file_path):
    return pd.read_csv(file_path, header=None)
def preprocess_data(data):
    transactions = []
    for i in range(len(data)):
        transaction = [str(data.values[i, j]) for j in range(data.shape[1]) if str(data.values[i, j]) != 'nan']
        transactions.append(transaction)
    return transactions
def apply_apriori(transactions, min_support, min_confidence, min_lift, min_length):
    return list(apriori(transactions, min_support=min_support,
                        min_confidence=min_confidence, min_lift=min_lift,
                        min_length=min_length))
def print_association_rules(rules):
    print(f"Number of association rules: {len(rules)}")
    for rule in rules:
        items = list(rule.items)
        support = rule.support
        confidence = rule.ordered_statistics[0].confidence
        lift = rule.ordered_statistics[0].lift
        print(f"Rule: {items[0]} -> {items[1]}")
        print(f"Support: {support}")
        print(f"Confidence: {confidence}")
        print(f"Lift: {lift}")
        print("=====================================")
def main():
    file_path = 'D:/Shreyas Kulkarni/Documents/PycharmProjects/MarketAnalysis_Apriori_Basic/store_data.csv'
    store_data = load_dataset(file_path)
    print(store_data.head())
    transactions = preprocess_data(store_data)
    association_rules = apply_apriori(transactions, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
    print_association_rules(association_rules)
if __name__ == "__main__":
    main()
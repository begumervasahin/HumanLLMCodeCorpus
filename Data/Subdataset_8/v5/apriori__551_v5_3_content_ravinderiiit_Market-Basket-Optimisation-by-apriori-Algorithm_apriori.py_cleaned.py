
import pandas as pd
from apyori import apriori
def load_dataset(file_path):
    dataset = pd.read_csv(file_path, header=None)
    transactions = []
    for i in range(len(dataset)):
        transactions.append([str(dataset.values[i, j]) for j in range(len(dataset.columns))])
    return transactions
def generate_association_rules(transactions, min_support, min_confidence, min_lift, min_length):
    rules = apriori(transactions,
                    min_support=min_support,
                    min_confidence=min_confidence,
                    min_lift=min_lift,
                    min_length=min_length)
    return list(rules)
def main():
    file_path = 'Market_Basket_Optimisation.csv'
    min_support = 0.003
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    transactions = load_dataset(file_path)
    rules = generate_association_rules(transactions, min_support, min_confidence, min_lift, min_length)
    for rule in rules:
        print("Association Rule:", rule.items)
        print("Support:", rule.support)
        print("Confidence:", rule.ordered_statistics[0].confidence)
        print("Lift:", rule.ordered_statistics[0].lift)
        print("===================================")
if __name__ == "__main__":
    main()
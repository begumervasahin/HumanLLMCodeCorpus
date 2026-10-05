
import pandas as pd
from apyori import apriori
def load_dataset(file_path):
    dataset = pd.read_csv(file_path, header=None)
    transactions = []
    for i in range(len(dataset)):
        transactions.append([str(dataset.values[i, j]) for j in range(len(dataset.columns))])
    return transactions
def main():
    file_path = 'Market_Basket_Optimisation.csv'
    min_support = 0.003
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    transactions = load_dataset(file_path)
    rules = apriori(transactions,
                    min_support=min_support,
                    min_confidence=min_confidence,
                    min_lift=min_lift,
                    min_length=min_length)
    results = list(rules)
    for result in results:
        print("Association Rule:", result.items)
        print("Support:", result.support)
        print("Confidence:", result.ordered_statistics[0].confidence)
        print("Lift:", result.ordered_statistics[0].lift)
        print("===================================")
if __name__ == "__main__":
    main()

import pandas as pd
from apyori import apriori
dataset = pd.read_csv('FYP.csv')
customer_transactions = dataset.iloc[:, [5, 10]].values
customer_transactions = customer_transactions[customer_transactions[:, 0].argsort()]
transactions = []
temp_transaction = []
for i in range(len(customer_transactions)):
    if i > 0 and customer_transactions[i][0] != customer_transactions[i - 1][0]:
        transactions.append(list(set(temp_transaction)))
        temp_transaction = []
    temp_transaction.append(str(customer_transactions[i][1]))
transactions.append(list(set(temp_transaction)))
rules = apriori(transactions, min_support=0.02, min_confidence=0.2, min_lift=1.4, min_length=2)
results = list(rules)
def extract_results(results):
    extracted_results = []
    for result in results:
        rhs = tuple(result.ordered_statistics[0].items_base)
        lhs = tuple(result.ordered_statistics[0].items_add)
        support = result.support
        confidence = result.ordered_statistics[0].confidence
        lift = result.ordered_statistics[0].lift
        extracted_results.append((rhs, lhs, support, confidence, lift))
    return extracted_results
extracted_results = extract_results(results)
final_lhs = [result[1] for result in extracted_results[:19]]
final_rhs = [result[0] for result in extracted_results[:19]]
print("Final LHS Values:")
print(final_lhs)
print("Final RHS Values:")
print(final_rhs)
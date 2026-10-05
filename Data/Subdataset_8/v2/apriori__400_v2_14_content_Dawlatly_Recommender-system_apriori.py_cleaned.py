import pandas as pd
from apyori import apriori
dataset = pd.read_csv('FYP.csv')
customer_ID = dataset.iloc[:, [5, 10]].values
customer_ID = customer_ID[customer_ID[:, 0].argsort()]
transactions = [['Labels']]
for i in range(1, len(customer_ID)):
    if customer_ID[i][0] == customer_ID[i - 1][0]:
        transactions[-1].append(str(customer_ID[i][1]))
    else:
        transactions[-1] = list(set(transactions[-1]))
        transactions.append([str(customer_ID[i][1])])
rules = apriori(transactions, min_support=0.02, min_confidence=0.2, min_lift=1.4, min_length=2)
results = list(rules)
def inspect_results(results):
    extracted_results = []
    for result in results:
        rhs = tuple(result.ordered_statistics[0].items_base)
        lhs = tuple(result.ordered_statistics[0].items_add)
        support = result.support
        confidence = result.ordered_statistics[0].confidence
        lift = result.ordered_statistics[0].lift
        extracted_results.append((rhs, lhs, support, confidence, lift))
    return extracted_results
extracted_results = inspect_results(results)
final_lhs = [result[1] for result in extracted_results[:19]]
final_rhs = [result[0] for result in extracted_results[:19]]
print("Final LHS Values:")
print(final_lhs)
print("Final RHS Values:")
print(final_rhs)
import pandas as pd
from apyori import apriori
data = pd.read_excel('D:\\ML-Class\\Data Sets\\Apriori\\Online Retail.xlsx')
transactions_france = data[data['Country'] == 'France']
transactions_relevant = transactions_france[['InvoiceNo', 'Description']]
transaction_list = []
for invoice_no in transactions_relevant['InvoiceNo'].unique():
    items = list(transactions_relevant[transactions_relevant['InvoiceNo'] == invoice_no]['Description'])
    transaction_list.append(items)
association_rules = apriori(transaction_list, min_support=0.05, min_confidence=0.2, min_lift=3, min_length=3)
rules_list = list(association_rules)
rules_df = pd.DataFrame(columns=['Base_item', 'Add_item', 'Confidence', 'Lift'])
for rule in rules_list:
    rule_info = rule.ordered_statistics[0]
    base_item = list(rule_info.items_base)
    add_item = list(rule_info.items_add)
    confidence = rule_info.confidence
    lift = rule_info.lift
    rules_df = rules_df.append({'Base_item': base_item, 'Add_item': add_item, 'Confidence': confidence, 'Lift': lift}, ignore_index=True)
print(rules_df.head(10))
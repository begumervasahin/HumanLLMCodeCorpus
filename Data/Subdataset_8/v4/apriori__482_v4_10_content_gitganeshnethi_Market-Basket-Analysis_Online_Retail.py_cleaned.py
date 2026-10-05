
import pandas as pd
from apyori import apriori
data = pd.read_excel('D:\\ML-Class\\Data Sets\\Apriori\\Online Retail.xlsx')
data_france = data[data['Country'] == 'France']
main_data = data_france.iloc[:, [0, 2]]
transaction_list = []
for invoice in main_data['InvoiceNo'].unique():
    items = list(main_data[main_data['InvoiceNo'] == invoice]['Description'])
    transaction_list.append(items)
association_rules = apriori(transaction_list, min_support=0.05, min_confidence=0.2, min_lift=3, min_length=3)
rules_list = list(association_rules)
rules_df = pd.DataFrame()
for rule in rules_list:
    rule_info = rule[2][0]
    curr_row = {'Base_item': rule_info[0], 'Add_item': rule_info[1], 'Confidence': rule_info[2], 'Lift': rule_info[3]}
    rules_df = rules_df.append(curr_row, ignore_index=True)
print(rules_df.head(10))
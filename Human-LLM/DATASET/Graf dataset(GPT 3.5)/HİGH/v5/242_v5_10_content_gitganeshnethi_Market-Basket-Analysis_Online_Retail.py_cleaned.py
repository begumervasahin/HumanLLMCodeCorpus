import pandas as pd
from apyori import apriori
b1 = pd.read_excel('D:\\ML-Class\\Data Sets\\Apriori\\Online Retail.xlsx')
b2 = b1[b1['Country'] == 'France']
b3 = b2[['InvoiceNo', 'Description']]
b4 = []
for invoice_no in b3['InvoiceNo'].unique():
    b5 = list(b3[b3['InvoiceNo'] == invoice_no]['Description'])
    b4.append(b5)
b6 = apriori(b4, min_support=0.05, min_confidence=0.2, min_lift=3, min_length=3)
b7 = list(b6)
b8 = pd.DataFrame(columns=['Base_item', 'Add_item', 'Confidence', 'Lift'])
for rule in b7:
    b9 = rule.ordered_statistics[0]
    b10 = list(b9.items_base)
    b11 = list(b9.items_add)
    b12 = b9.b12
    b13 = b9.b13
    b8 = b8.append({'Base_item': b10, 'Add_item': b11, 'Confidence': b12, 'Lift': b13}, ignore_index=True)
print(b8.head(10))
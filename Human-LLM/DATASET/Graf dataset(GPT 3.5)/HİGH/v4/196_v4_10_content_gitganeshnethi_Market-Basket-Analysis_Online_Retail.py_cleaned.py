
import pandas as pd
from apyori import apriori
b1 = pd.read_excel('D:\\ML-Class\\Data Sets\\Apriori\\Online Retail.xlsx')
b2 = b1[b1['Country'] == 'France']
b3 = b2.iloc[:, [0, 2]]
b4 = []
for invoice in b3['InvoiceNo'].unique():
    b5 = list(b3[b3['InvoiceNo'] == invoice]['Description'])
    b4.append(b5)
b6 = apriori(b4, min_support=0.05, min_confidence=0.2, min_lift=3, min_length=3)
b7 = list(b6)
b8 = pd.DataFrame()
for rule in b7:
    b9 = rule[2][0]
    b10 = {'Base_item': b9[0], 'Add_item': b9[1], 'Confidence': b9[2], 'Lift': b9[3]}
    b8 = b8.append(b10, ignore_index=True)
print(b8.head(10))
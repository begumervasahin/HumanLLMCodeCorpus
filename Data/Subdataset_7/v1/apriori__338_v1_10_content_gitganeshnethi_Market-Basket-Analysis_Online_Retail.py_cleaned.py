import pandas as pd
from apyori import apriori
def fonk1(data_file, b1 = 'France', min_support=0.05, min_confidence=0.2, b7=3, min_length=3):
    b2 = pd.read_excel(data_file)
    b3 = b2[b2['Country'] == b1]
    b4 = b3[['InvoiceNo', 'Description']]
    b5 = b4.groupby('InvoiceNo')['Description'].apply(list).values.tolist()
    b6 = apriori(b5, min_support=min_support, min_confidence=min_confidence,
                                b7 = b7, min_length=min_length)
    b8 = list(b6)
    b9 = pd.DataFrame(columns=['Base_item', 'Add_item', 'Confidence', 'Lift'])
    for rule in b8:
        b10 = rule.ordered_statistics[0].items_base
        b11 = rule.ordered_statistics[0].items_add
        b12 = rule.ordered_statistics[0].b12
        b13 = rule.ordered_statistics[0].b13
        b9 = b9.append({'Base_item': list(b10), 'Add_item': list(b11),
                                    'Confidence': b12, 'Lift': b13}, b14 = True)
    return b9
if b15 = = "__main__":
    b16 = 'D:\\ML-Class\\Data Sets\\Apriori\\Online Retail.xlsx'
    b9 = fonk1(b16, b1='France')
    print(b9)
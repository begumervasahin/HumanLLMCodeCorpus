import pandas as pd
from apyori import apriori
def market_basket_analysis(data_file, country='France', min_support=0.05, min_confidence=0.2, min_lift=3, min_length=3):
    data = pd.read_excel(data_file)
    data_country = data[data['Country'] == country]
    main_data = data_country[['InvoiceNo', 'Description']]
    transactions = main_data.groupby('InvoiceNo')['Description'].apply(list).values.tolist()
    association_rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence,
                                min_lift=min_lift, min_length=min_length)
    rules_list = list(association_rules)
    rules_df = pd.DataFrame(columns=['Base_item', 'Add_item', 'Confidence', 'Lift'])
    for rule in rules_list:
        base_item = rule.ordered_statistics[0].items_base
        add_item = rule.ordered_statistics[0].items_add
        confidence = rule.ordered_statistics[0].confidence
        lift = rule.ordered_statistics[0].lift
        rules_df = rules_df.append({'Base_item': list(base_item), 'Add_item': list(add_item),
                                    'Confidence': confidence, 'Lift': lift}, ignore_index=True)
    return rules_df
if __name__ == "__main__":
    data_file_path = 'D:\\ML-Class\\Data Sets\\Apriori\\Online Retail.xlsx'
    rules_df = market_basket_analysis(data_file_path, country='France')
    print(rules_df)
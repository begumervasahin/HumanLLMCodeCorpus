import pandas as pd
from sklearn.preprocessing import LabelEncoder
train_data = pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv", na_values='.')
test_data = pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv")
train_data['source'] = 'train_data'
test_data['source'] = 'test_data'
combined_data = pd.concat([train_data, test_data], ignore_index=True)
print("Train dataset shape:", train_data.shape)
print("Test dataset shape:", test_data.shape)
print("Combined dataset shape:", combined_data.shape)
print("\nSummary for unique values:\n", combined_data.apply(lambda x: len(x.unique())))
print("Summary for missing values:\n", combined_data.isnull().sum())
print("Percentage of missing values:\n", combined_data.isnull().sum() / combined_data.shape[0] * 100)
print("\nStatistical Summary of Item Visibility:\n", combined_data['Item_Visibility'].describe())
print("\n", combined_data.describe())
category_columns = [col for col in combined_data.select_dtypes(include='object').columns if col not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
for column in category_columns:
    print('\nFrequency of Categories for variable', column)
    print(combined_data[column].value_counts())
item_avg_weight = combined_data.groupby('Item_Identifier')['Item_Weight'].mean()
combined_data['Item_Weight'] = combined_data['Item_Weight'].fillna(combined_data['Item_Identifier'].map(item_avg_weight))
outlet_size_mode = combined_data.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x: x.mode().iloc[0])
combined_data['Outlet_Size'] = combined_data['Outlet_Size'].fillna(combined_data['Outlet_Type'].map(outlet_size_mode))
visibility_avg = combined_data.groupby('Item_Identifier')['Item_Visibility'].mean()
combined_data.loc[combined_data['Item_Visibility'] == 0, 'Item_Visibility'] = combined_data[combined_data['Item_Visibility'] == 0].apply(lambda row: visibility_avg[row['Item_Identifier']], axis=1)
combined_data['Outlet_Years'] = 2013 - combined_data['Outlet_Establishment_Year']
combined_data['Item_Type_Combined'] = combined_data['Item_Identifier'].apply(lambda x: x[:2]).map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
combined_data['Item_Fat_Content'] = combined_data['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
combined_data.loc[combined_data['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
combined_data['Item_Visibility_MeanRatio'] = combined_data.apply(lambda x: x['Item_Visibility'] / visibility_avg[x['Item_Identifier']], axis=1)
le = LabelEncoder()
for col in ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']:
    combined_data[col] = le.fit_transform(combined_data[col])
combined_data = pd.get_dummies(combined_data, columns=['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Outlet_Type', 'Item_Type_Combined', 'Outlet'])
combined_data.drop(['Item_Type', 'Outlet_Establishment_Year'], axis=1, inplace=True)
train = combined_data.loc[combined_data['source'] == "train_data"].drop(columns=['source'])
test = combined_data.loc[combined_data['source'] == "test_data"].drop(columns=['source', 'Item_Outlet_Sales'])
train.to_csv("D:/Github/Big Mart Sales/train_modified.csv", index=False)
test.to_csv("D:/Github/Big Mart Sales/test_modified.csv", index=False)
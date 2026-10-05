import pandas as pd
from sklearn.preprocessing import LabelEncoder
b1 = pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv", na_values='.')
b2 = pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv")
b1['source'] = 'b1'
b2['source'] = 'b2'
b3 = pd.concat([b1, b2], ignore_index=True)
print("Train dataset shape:", b1.shape)
print("Test dataset shape:", b2.shape)
print("Combined dataset shape:", b3.shape)
print("\nSummary for unique values:\n", b3.apply(lambda x: len(x.unique())))
print("Summary for missing values:\n", b3.isnull().sum())
print("Percentage of missing values:\n", b3.isnull().sum() / b3.shape[0] * 100)
print("\nStatistical Summary of Item Visibility:\n", b3['Item_Visibility'].describe())
print("\n", b3.describe())
b4 = [col for col in b3.select_dtypes(include='object').columns if col not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
for column in b4:
    print('\nFrequency of Categories for variable', column)
    print(b3[column].value_counts())
b5 = b3.groupby('Item_Identifier')['Item_Weight'].mean()
b3['Item_Weight'] = b3['Item_Weight'].fillna(b3['Item_Identifier'].map(b5))
b6 = b3.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x: x.mode().iloc[0])
b3['Outlet_Size'] = b3['Outlet_Size'].fillna(b3['Outlet_Type'].map(b6))
b7 = b3.groupby('Item_Identifier')['Item_Visibility'].mean()
b3.loc[b3['Item_Visibility'] == 0, 'Item_Visibility'] = b3[b3['Item_Visibility'] == 0].apply(lambda row: b7[row['Item_Identifier']], b8 = 1)
b3['Outlet_Years'] = 2013 - b3['Outlet_Establishment_Year']
b3['Item_Type_Combined'] = b3['Item_Identifier'].apply(lambda x: x[:2]).map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
b3['Item_Fat_Content'] = b3['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
b3.loc[b3['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
b3['Item_Visibility_MeanRatio'] = b3.apply(lambda x: x['Item_Visibility'] / b7[x['Item_Identifier']], b8 = 1)
b9 = LabelEncoder()
for col in ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']:
    b3[col] = b9.fit_transform(b3[col])
b3 = pd.get_dummies(b3, columns=['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Outlet_Type', 'Item_Type_Combined', 'Outlet'])
b3.drop(['Item_Type', 'Outlet_Establishment_Year'], b8 = 1, inplace=True)
b10 = b3.loc[b3['source'] == "b1"].drop(columns=['source'])
b11 = b3.loc[b3['source'] == "b2"].drop(columns=['source', 'Item_Outlet_Sales'])
b10.to_csv("D:/Github/Big Mart Sales/train_modified.csv", b12 = False)
b11.to_csv("D:/Github/Big Mart Sales/test_modified.csv", b12 = False)
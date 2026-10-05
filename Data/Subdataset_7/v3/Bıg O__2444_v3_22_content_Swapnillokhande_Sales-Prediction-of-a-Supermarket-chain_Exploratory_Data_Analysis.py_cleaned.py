import pandas as pd
from sklearn.preprocessing import LabelEncoder
b1 = pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv", na_values='.')
b2 = pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv')
b1['source'] = 'b1'
b2['source'] = 'b2'
b3 = pd.concat([b1, b2], ignore_index=True)
print("Data Shapes:")
print("Train dataset shape:", b1.shape)
print("Test dataset shape:", b2.shape)
print("Combined dataset shape:", b3.shape)
print("\nSummary for Unique Values:\n", b3.apply(lambda x: len(x.unique())))
print("\nSummary for Missing Values:\n", b3.isnull().sum())
print("Percentage of Missing Values:\n", b3.isnull().sum() / b3.shape[0] * 100)
print("\nStatistical Summary of Item Visibility:\n", b3['Item_Visibility'].describe())
print("\nStatistical Summary of Dataset:\n", b3.describe())
b4 = [col for col in b3.select_dtypes(include='object').columns if col not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
for column in b4:
    print('\nFrequency of Categories for variable', column)
    print(b3[column].value_counts())
b5 = b3.groupby('Item_Identifier')['Item_Weight'].transform('mean')
b3['Item_Weight'].fillna(b5, b6 = True)
b7 = b3.groupby('Outlet_Type')['Outlet_Size'].transform(lambda x: x.mode().iloc[0])
b3['Outlet_Size'].fillna(b7, b6 = True)
b8 = b3.groupby('Item_Identifier')['Item_Visibility'].transform('mean')
b3.loc[b3['Item_Visibility'] == 0, 'Item_Visibility'] = b8
b3['Outlet_Years'] = 2013 - b3['Outlet_Establishment_Year']
b3['Item_Type_Combined'] = b3['Item_Identifier'].apply(lambda x: x[:2]).map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
b3['Item_Fat_Content'] = b3['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
b3.loc[b3['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
b3['Item_Visibility_MeanRatio'] = b3['Item_Visibility'] / b8
b9 = LabelEncoder()
b10 = ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']
for col in b10:
    b3[col] = b9.fit_transform(b3[col])
b3 = pd.get_dummies(b3, columns=b10)
b3.drop(['Item_Type', 'Outlet_Establishment_Year'], b11 = 1, b6=True)
b12 = b3.loc[b3['source'] == "b1"].drop(columns=['source'])
b13 = b3.loc[b3['source'] == "b2"].drop(columns=['source', 'Item_Outlet_Sales'])
b12.to_csv("D:/Github/Big Mart Sales/train_modified.csv", b14 = False)
b13.to_csv("D:/Github/Big Mart Sales/test_modified.csv", b14 = False)
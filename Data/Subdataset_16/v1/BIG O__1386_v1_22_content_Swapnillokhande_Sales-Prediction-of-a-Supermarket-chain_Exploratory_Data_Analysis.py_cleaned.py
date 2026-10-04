import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
b1 = pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv", na_values='.')
b2 = pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv")
b1['source'] = 'b1'
b2['source'] = 'b2'
b3 = pd.concat([b1, b2], ignore_index=True)
print("Number of rows and columns in Train dataset:", b1.shape)
print("Number of rows and columns in Test dataset:", b2.shape)
print("Number of rows and columns in combined dataset:", b3.shape)
print("\nSummary for unique values\n", b3.apply(lambda x: len(x.unique())))
print("\nSummary for missing values\n", b3.isnull().sum())
print("\nPercentage of missing values\n", b3.isnull().sum() / b3.shape[0] * 100)
print("\nStatistical Summary of Item Visibility\n", b3['Item_Visibility'].describe())
print("\nStatistical Summary of combined data\n", b3.describe())
b4 = [col for col in b3.dtypes.b13 if b3.dtypes[col] == 'object']
b4 = [col for col in b4 if col not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
for column in b4:
    print(f'\nFrequency of Categories for variable {column}')
    print(b3[column].value_counts())
b5 = b3.pivot_table(values='Item_Weight', b13='Item_Identifier')
b3['Item_Weight'] = b3.groupby('Item_Identifier')['Item_Weight'].transform(lambda x: x.fillna(x.mean()))
b6 = b3.pivot_table(values='Outlet_Size', columns='Outlet_Type', aggfunc=lambda x: x.mode()[0])
b3['Outlet_Size'] = b3.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x: x.fillna(x.mode()[0]))
b3['Item_Visibility'] = b3.groupby('Item_Identifier')['Item_Visibility'].transform(lambda x: x.replace(0, x.mean()))
b3['Outlet_Years'] = 2013 - b3['Outlet_Establishment_Year']
b3['Item_Type_Combined'] = b3['Item_Identifier'].apply(lambda x: x[0:2])
b3['Item_Type_Combined'] = b3['Item_Type_Combined'].map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
b3['Item_Fat_Content'] = b3['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
b3.loc[b3['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
b7 = b3.pivot_table(values='Item_Visibility', b13='Item_Identifier')
b3['Item_Visibility_MeanRatio'] = b3.apply(lambda x: x['Item_Visibility'] / b7.loc[x['Item_Identifier']][0], b8 = 1)
b9 = LabelEncoder()
b3['Outlet'] = b9.fit_transform(b3['Outlet_Identifier'])
b10 = ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']
for var in b10:
    b3[var] = b9.fit_transform(b3[var])
b3 = pd.get_dummies(b3, columns=b10)
b3.drop(['Item_Type', 'Outlet_Establishment_Year'], b8 = 1, inplace=True)
b11 = b3[b3['source'] == "b1"].drop(['source'], b8=1)
b12 = b3[b3['source'] == "b2"].drop(['source', 'Item_Outlet_Sales'], b8=1)
b11.to_csv("D:/Github/Big Mart Sales/train_modified.csv", b13 = False)
b12.to_csv("D:/Github/Big Mart Sales/test_modified.csv", b13 = False)
import pandas as pd
import numpy as np
b1 = pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv", na_values='.')
b2 = pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv")
b1['source'] = 'b1'
b2['source'] = 'b2'
b3 = pd.concat([b1, b2], ignore_index=True)
print("Number of rows and columns in Train dataset:", b1.shape)
print("Number of rows and columns in Test dataset:", b2.shape)
print("Number of rows and columns in combined dataset:", b3.shape)
print("\nSummary for unique values:\n", b3.apply(lambda x: len(x.unique())))
print("Summary for missing values:\n", b3.isnull().sum())
print(b3.isnull().sum() / b3.shape[0] * 100)
print("\nStatistical Summary of Item Visibility:\n", b3['Item_Visibility'].describe())
print("\n", b3.describe())
b4 = [x for x in b3.dtypes.b16 if b3.dtypes[x] == 'object']
b4 = [x for x in b4 if x not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
for column in b4:
    print('\nFrequency of Categories for variable %s' % column)
    print(b3[column].value_counts())
b5 = b3.pivot_table(values='Item_Weight', b16='Item_Identifier')
b6 = b3['Item_Weight'].isnull()
print('Missing values before imputation:', sum(b6))
b3.loc[b6, 'Item_Weight'] = b3.loc[b6, 'Item_Identifier'].apply(lambda x: b5.at[x, 'Item_Weight'])
print('Final count of missing values:', sum(b3['Item_Weight'].isnull()))
b7 = b3.pivot_table(values='Outlet_Size', columns='Outlet_Type', aggfunc=lambda x: x.mode().iat[0])
b6 = b3['Outlet_Size'].isnull()
print('Original missing values:', sum(b6))
for outlet_type in b7.columns:
    b3.loc[b6 & (b3['Outlet_Type'] == outlet_type), 'Outlet_Size'] = b7[outlet_type].iloc[0]
print('Final count of missing values:', sum(b3['Outlet_Size'].isnull()))
b8 = b3.pivot_table(values='Item_Visibility', b16='Item_Identifier')
b9 = (b3['Item_Visibility'] == 0)
print('Number of 0 values initially:', sum(b9))
b3.loc[b9, 'Item_Visibility'] = b3.loc[b9, 'Item_Identifier'].apply(lambda x: b8.at[x, 'Item_Visibility'])
print('Number of 0 values after modification:', sum(b3['Item_Visibility'] == 0))
b3['Outlet_Years'] = 2013 - b3['Outlet_Establishment_Year']
b3['Item_Type_Combined'] = b3['Item_Identifier'].apply(lambda x: x[0:2])
b3['Item_Type_Combined'] = b3['Item_Type_Combined'].map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
b3['Item_Fat_Content'] = b3['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
b3.loc[b3['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
b10 = lambda x: x['Item_Visibility'] / b8.at[x['Item_Identifier'], 'Item_Visibility']
b3['Item_Visibility_MeanRatio'] = b3.apply(b10, b11 = 1).astype(float)
from sklearn.preprocessing import LabelEncoder
b12 = LabelEncoder()
b13 = ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']
for i in b13:
    b3[i] = b12.fit_transform(b3[i])
b3 = pd.get_dummies(b3, columns=['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Outlet_Type', 'Item_Type_Combined', 'Outlet'])
b3.drop(['Item_Type', 'Outlet_Establishment_Year'], b11 = 1, inplace=True)
b14 = b3.loc[b3['source'] == "b1"]
b15 = b3.loc[b3['source'] == "b2"]
b14.drop(['source'], b11 = 1, inplace=True)
b15.drop(['Item_Outlet_Sales', 'source'], b11 = 1, inplace=True)
b14.to_csv("D:/Github/Big Mart Sales/train_modified.csv", b16 = False)
b15.to_csv("D:/Github/Big Mart Sales/test_modified.csv", b16 = False)
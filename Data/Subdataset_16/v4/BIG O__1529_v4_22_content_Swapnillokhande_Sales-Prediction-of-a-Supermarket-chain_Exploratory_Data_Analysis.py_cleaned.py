import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
def fonk1():
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
    b4 = [col for col in b3.dtypes.b14 if b3.dtypes[col] == 'object']
    b4 = [col for col in b4 if col not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
    for column in b4:
        print(f'\nFrequency of Categories for variable {column}')
        print(b3[column].value_counts())
    b5 = b3.pivot_table(values='Item_Weight', b14='Item_Identifier')
    print(b5)
    print('Missing values before imputation:', b3['Item_Weight'].isnull().sum())
    b3['Item_Weight'] = b3.groupby('Item_Identifier')['Item_Weight'].transform(lambda x: x.fillna(x.mean()))
    print('Final count of missing values:', b3['Item_Weight'].isnull().sum())
    b6 = b3.pivot_table(values='Outlet_Size', columns='Outlet_Type', aggfunc=lambda x: x.mode().iat[0])
    print('Mode for each Outlet_Type:')
    print(b6)
    print('Original missing values:', b3['Outlet_Size'].isnull().sum())
    b3['Outlet_Size'] = b3.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x: x.fillna(x.mode().iloc[0]))
    print('Final count of missing values:', b3['Outlet_Size'].isnull().sum())
    b7 = b3.pivot_table(values='Item_Visibility', b14='Item_Identifier')
    print('Number of 0 values initially:', (b3['Item_Visibility'] == 0).sum())
    b3.loc[b3['Item_Visibility'] == 0, 'Item_Visibility'] = b3.groupby('Item_Identifier')['Item_Visibility'].transform('mean')
    print('Number of 0 values after modification:', (b3['Item_Visibility'] == 0).sum())
    b3['Outlet_Years'] = 2013 - b3['Outlet_Establishment_Year']
    print(b3['Outlet_Years'].describe())
    b3['Item_Type_Combined'] = b3['Item_Identifier'].apply(lambda x: x[0:2])
    b3['Item_Type_Combined'] = b3['Item_Type_Combined'].map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
    print(b3['Item_Type_Combined'].value_counts())
    print('Original Categories:')
    print(b3['Item_Fat_Content'].value_counts())
    b3['Item_Fat_Content'] = b3['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
    b3.loc[b3['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
    print('\nModified Categories:')
    print(b3['Item_Fat_Content'].value_counts())
    b8 = b7['Item_Visibility'].to_dict()
    b3['Item_Visibility_MeanRatio'] = b3.apply(lambda x: x['Item_Visibility'] / b8[x['Item_Identifier']], b9 = 1)
    print(b3['Item_Visibility_MeanRatio'].describe())
    b10 = LabelEncoder()
    b3['Outlet'] = b10.fit_transform(b3['Outlet_Identifier'])
    b11 = ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']
    for col in b11:
        b3[col] = b10.fit_transform(b3[col])
    b3 = pd.get_dummies(b3, columns=b11)
    b3.drop(['Item_Type', 'Outlet_Establishment_Year'], b9 = 1, inplace=True)
    b12 = b3[b3['source'] == "b1"].copy()
    b13 = b3[b3['source'] == "b2"].copy()
    b12.drop(['source'], b9 = 1, inplace=True)
    b13.drop(['Item_Outlet_Sales', 'source'], b9 = 1, inplace=True)
    b12.to_csv("D:/Github/Big Mart Sales/train_modified.csv", b14 = False)
    b13.to_csv("D:/Github/Big Mart Sales/test_modified.csv", b14 = False)
if b15 = = "__main__":
    fonk1()
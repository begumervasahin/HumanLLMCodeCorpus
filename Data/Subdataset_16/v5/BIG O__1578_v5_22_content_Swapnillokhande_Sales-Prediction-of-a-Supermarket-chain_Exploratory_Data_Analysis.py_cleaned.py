import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
def fonk1(b14, b15):
    b1 = pd.read_csv(b14, na_values='.')
    b2 = pd.read_csv(b15)
    return b1, b2
def fonk2(b1, b2):
    b1['source'] = 'b1'
    b2['source'] = 'b2'
    return pd.concat([b1, b2], b3 = True)
def fonk3(b16):
    print("Number of rows and b10 in combined dataset:", b16.shape)
    print("\nSummary for unique values:\n", b16.apply(lambda x: len(x.unique())))
    print("Summary for missing values:\n", b16.isnull().sum())
    print(b16.isnull().sum() / b16.shape[0] * 100)
    print("\nStatistical Summary of Item Visibility:\n", b16['Item_Visibility'].describe())
    print("\n", b16.describe())
def fonk4(b16):
    b4 = [col for col in b16.dtypes.b13 if b16.dtypes[col] == 'object']
    b4 = [col for col in b4 if col not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
    for column in b4:
        print(f'\nFrequency of Categories for variable {column}')
        print(b16[column].value_counts())
def fonk5(b16):
    b16['Item_Weight'] = b16.groupby('Item_Identifier')['Item_Weight'].transform(lambda x: x.fillna(x.mean()))
    b16['Outlet_Size'] = b16.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x: x.fillna(x.mode().iloc[0]))
    return b16
def fonk6(b16):
    b16['Item_Visibility'] = b16.groupby('Item_Identifier')['Item_Visibility'].transform(lambda x: x.replace(0, x.mean()))
def fonk7(b16):
    b16['Outlet_Years'] = 2013 - b16['Outlet_Establishment_Year']
    b16['Item_Type_Combined'] = b16['Item_Identifier'].apply(lambda x: x[0:2])
    b16['Item_Type_Combined'] = b16['Item_Type_Combined'].map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
    b16['Item_Fat_Content'] = b16['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
    b16.loc[b16['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
    b5 = b16.pivot_table(values='Item_Visibility', b13='Item_Identifier')
    b6 = b5['Item_Visibility'].to_dict()
    b16['Item_Visibility_MeanRatio'] = b16.apply(lambda x: x['Item_Visibility'] / b6[x['Item_Identifier']], b7 = 1)
def fonk8(b16):
    b8 = LabelEncoder()
    b16['Outlet'] = b8.fit_transform(b16['Outlet_Identifier'])
    b9 = ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']
    for col in b9:
        b16[col] = b8.fit_transform(b16[col])
    return pd.get_dummies(b16, b10 = b9)
def fonk9(b16, b14, b15):
    b11 = b16[b16['source'] == "b1"].copy()
    b12 = b16[b16['source'] == "b2"].copy()
    b11.drop(['source'], b7 = 1, inplace=True)
    b12.drop(['Item_Outlet_Sales', 'source'], b7 = 1, inplace=True)
    b11.to_csv(b14, b13 = False)
    b12.to_csv(b15, b13 = False)
def fonk10():
    b14 = "D:/Github/Big Mart Sales/Train_Data.csv"
    b15 = "D:/Github/Big Mart Sales/Test_Data.csv"
    b1, b2 = fonk1(b14, b15)
    b16 = fonk2(b1, b2)
    fonk3(b16)
    fonk4(b16)
    b16 = fonk5(b16)
    fonk6(b16)
    fonk7(b16)
    b16 = fonk8(b16)
    b16.drop(['Item_Type', 'Outlet_Establishment_Year'], b7 = 1, inplace=True)
    fonk9(b16, "D:/Github/Big Mart Sales/train_modified.csv", "D:/Github/Big Mart Sales/test_modified.csv")
if b17 = = "__main__":
    fonk10()
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
train_data = pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv", na_values='.')
test_data = pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv")
train_data['source'] = 'train_data'
test_data['source'] = 'test_data'
combined_data = pd.concat([train_data, test_data], ignore_index=True)
print("Number of rows and columns in Train dataset:", train_data.shape)
print("Number of rows and columns in Test dataset:", test_data.shape)
print("Number of rows and columns in combined dataset:", combined_data.shape)
print("\nSummary for unique values\n", combined_data.apply(lambda x: len(x.unique())))
print("\nSummary for missing values\n", combined_data.isnull().sum())
print("\nPercentage of missing values\n", combined_data.isnull().sum() / combined_data.shape[0] * 100)
print("\nStatistical Summary of Item Visibility\n", combined_data['Item_Visibility'].describe())
print("\nStatistical Summary of combined data\n", combined_data.describe())
category_columns = [col for col in combined_data.dtypes.index if combined_data.dtypes[col] == 'object']
category_columns = [col for col in category_columns if col not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
for column in category_columns:
    print(f'\nFrequency of Categories for variable {column}')
    print(combined_data[column].value_counts())
combined_data['Item_Weight'] = combined_data.groupby('Item_Identifier')['Item_Weight'].transform(lambda x: x.fillna(x.mean()))
combined_data['Outlet_Size'] = combined_data.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x: x.fillna(x.mode()[0]))
combined_data['Item_Visibility'] = combined_data.groupby('Item_Identifier')['Item_Visibility'].transform(lambda x: x.replace(0, x.mean()))
combined_data['Outlet_Years'] = 2013 - combined_data['Outlet_Establishment_Year']
combined_data['Item_Type_Combined'] = combined_data['Item_Identifier'].apply(lambda x: x[0:2])
combined_data['Item_Type_Combined'] = combined_data['Item_Type_Combined'].map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
combined_data['Item_Fat_Content'] = combined_data['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
combined_data.loc[combined_data['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
visibility_avg = combined_data.pivot_table(values='Item_Visibility', index='Item_Identifier')
combined_data['Item_Visibility_MeanRatio'] = combined_data.apply(lambda x: x['Item_Visibility'] / visibility_avg.loc[x['Item_Identifier']][0], axis=1)
le = LabelEncoder()
combined_data['Outlet'] = le.fit_transform(combined_data['Outlet_Identifier'])
var_mod = ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']
for var in var_mod:
    combined_data[var] = le.fit_transform(combined_data[var])
combined_data = pd.get_dummies(combined_data, columns=var_mod)
combined_data.drop(['Item_Type', 'Outlet_Establishment_Year'], axis=1, inplace=True)
train = combined_data[combined_data['source'] == "train_data"].drop(['source'], axis=1)
test = combined_data[combined_data['source'] == "test_data"].drop(['source', 'Item_Outlet_Sales'], axis=1)
train.to_csv("D:/Github/Big Mart Sales/train_modified.csv", index=False)
test.to_csv("D:/Github/Big Mart Sales/test_modified.csv", index=False)
print("Preprocessing complete. Modified datasets saved.")
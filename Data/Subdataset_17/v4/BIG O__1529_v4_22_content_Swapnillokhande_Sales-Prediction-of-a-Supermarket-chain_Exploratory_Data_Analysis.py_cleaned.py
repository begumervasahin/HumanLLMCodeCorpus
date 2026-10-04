import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
def main():
    train_data = pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv", na_values='.')
    test_data = pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv")
    train_data['source'] = 'train_data'
    test_data['source'] = 'test_data'
    combined_data = pd.concat([train_data, test_data], ignore_index=True)
    print("Number of rows and columns in Train dataset:", train_data.shape)
    print("Number of rows and columns in Test dataset:", test_data.shape)
    print("Number of rows and columns in combined dataset:", combined_data.shape)
    print("\nSummary for unique values:\n", combined_data.apply(lambda x: len(x.unique())))
    print("Summary for missing values:\n", combined_data.isnull().sum())
    print(combined_data.isnull().sum() / combined_data.shape[0] * 100)
    print("\nStatistical Summary of Item Visibility:\n", combined_data['Item_Visibility'].describe())
    print("\n", combined_data.describe())
    categorical_columns = [col for col in combined_data.dtypes.index if combined_data.dtypes[col] == 'object']
    categorical_columns = [col for col in categorical_columns if col not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
    for column in categorical_columns:
        print(f'\nFrequency of Categories for variable {column}')
        print(combined_data[column].value_counts())
    item_avg_weight = combined_data.pivot_table(values='Item_Weight', index='Item_Identifier')
    print(item_avg_weight)
    print('Missing values before imputation:', combined_data['Item_Weight'].isnull().sum())
    combined_data['Item_Weight'] = combined_data.groupby('Item_Identifier')['Item_Weight'].transform(lambda x: x.fillna(x.mean()))
    print('Final count of missing values:', combined_data['Item_Weight'].isnull().sum())
    outlet_size_mode = combined_data.pivot_table(values='Outlet_Size', columns='Outlet_Type', aggfunc=lambda x: x.mode().iat[0])
    print('Mode for each Outlet_Type:')
    print(outlet_size_mode)
    print('Original missing values:', combined_data['Outlet_Size'].isnull().sum())
    combined_data['Outlet_Size'] = combined_data.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x: x.fillna(x.mode().iloc[0]))
    print('Final count of missing values:', combined_data['Outlet_Size'].isnull().sum())
    visibility_avg = combined_data.pivot_table(values='Item_Visibility', index='Item_Identifier')
    print('Number of 0 values initially:', (combined_data['Item_Visibility'] == 0).sum())
    combined_data.loc[combined_data['Item_Visibility'] == 0, 'Item_Visibility'] = combined_data.groupby('Item_Identifier')['Item_Visibility'].transform('mean')
    print('Number of 0 values after modification:', (combined_data['Item_Visibility'] == 0).sum())
    combined_data['Outlet_Years'] = 2013 - combined_data['Outlet_Establishment_Year']
    print(combined_data['Outlet_Years'].describe())
    combined_data['Item_Type_Combined'] = combined_data['Item_Identifier'].apply(lambda x: x[0:2])
    combined_data['Item_Type_Combined'] = combined_data['Item_Type_Combined'].map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
    print(combined_data['Item_Type_Combined'].value_counts())
    print('Original Categories:')
    print(combined_data['Item_Fat_Content'].value_counts())
    combined_data['Item_Fat_Content'] = combined_data['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
    combined_data.loc[combined_data['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
    print('\nModified Categories:')
    print(combined_data['Item_Fat_Content'].value_counts())
    visibility_avg_dict = visibility_avg['Item_Visibility'].to_dict()
    combined_data['Item_Visibility_MeanRatio'] = combined_data.apply(lambda x: x['Item_Visibility'] / visibility_avg_dict[x['Item_Identifier']], axis=1)
    print(combined_data['Item_Visibility_MeanRatio'].describe())
    le = LabelEncoder()
    combined_data['Outlet'] = le.fit_transform(combined_data['Outlet_Identifier'])
    var_mod = ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']
    for col in var_mod:
        combined_data[col] = le.fit_transform(combined_data[col])
    combined_data = pd.get_dummies(combined_data, columns=var_mod)
    combined_data.drop(['Item_Type', 'Outlet_Establishment_Year'], axis=1, inplace=True)
    train = combined_data[combined_data['source'] == "train_data"].copy()
    test = combined_data[combined_data['source'] == "test_data"].copy()
    train.drop(['source'], axis=1, inplace=True)
    test.drop(['Item_Outlet_Sales', 'source'], axis=1, inplace=True)
    train.to_csv("D:/Github/Big Mart Sales/train_modified.csv", index=False)
    test.to_csv("D:/Github/Big Mart Sales/test_modified.csv", index=False)
if __name__ == "__main__":
    main()
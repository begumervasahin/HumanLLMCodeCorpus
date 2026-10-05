import pandas as pd
from sklearn.preprocessing import LabelEncoder
train_data = pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv", na_values='.')
test_data = pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv")
train_data['source'] = 'train_data'
test_data['source'] = 'test_data'
comb_data = pd.concat([train_data, test_data], ignore_index=True)
print("Number of rows and columns in Train dataset:", train_data.shape)
print("Number of rows and columns in Test dataset:", test_data.shape)
print("Number of rows and columns in combined dataset:", comb_data.shape)
print("\nSummary for unique values:\n", comb_data.apply(lambda x: len(x.unique())))
print("Summary for missing values:\n", comb_data.isnull().sum())
print("Percentage of missing values:\n", comb_data.isnull().sum() / comb_data.shape[0] * 100)
print("\nStatistical Summary of Item Visibility:\n", comb_data['Item_Visibility'].describe())
print("\nStatistical Summary of Dataset:\n", comb_data.describe())
category_columns = [col for col in comb_data.select_dtypes(include='object').columns if col not in ['Item_Identifier', 'Outlet_Identifier', 'source']]
for column in category_columns:
    print('\nFrequency of Categories for variable', column)
    print(comb_data[column].value_counts())
item_avg_weight = comb_data.groupby('Item_Identifier')['Item_Weight'].mean()
comb_data['Item_Weight'].fillna(item_avg_weight, inplace=True)
outlet_size_mode = comb_data.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x: x.mode().iat[0])
comb_data['Outlet_Size'].fillna(outlet_size_mode, inplace=True)
visibility_avg = comb_data.groupby('Item_Identifier')['Item_Visibility'].mean()
comb_data.loc[comb_data['Item_Visibility'] == 0, 'Item_Visibility'] = comb_data.groupby('Item_Identifier')['Item_Visibility'].transform('mean')
comb_data['Outlet_Years'] = 2013 - comb_data['Outlet_Establishment_Year']
comb_data['Item_Type_Combined'] = comb_data['Item_Identifier'].apply(lambda x: x[:2]).map({'FD': 'Food', 'NC': 'Non-Consumable', 'DR': 'Drinks'})
comb_data['Item_Fat_Content'] = comb_data['Item_Fat_Content'].replace({'LF': 'Low Fat', 'reg': 'Regular', 'low fat': 'Low Fat'})
comb_data.loc[comb_data['Item_Type_Combined'] == "Non-Consumable", 'Item_Fat_Content'] = "Non-Edible"
visibility_avg = comb_data.pivot_table(values='Item_Visibility', index='Item_Identifier')
comb_data['Item_Visibility_MeanRatio'] = comb_data.apply(lambda x: x['Item_Visibility'] / visibility_avg.at[x['Item_Identifier'], 'Item_Visibility'], axis=1)
le = LabelEncoder()
categorical_cols = ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Size', 'Item_Type_Combined', 'Outlet_Type', 'Outlet']
for col in categorical_cols:
    comb_data[col] = le.fit_transform(comb_data[col])
comb_data = pd.get_dummies(comb_data, columns=categorical_cols)
comb_data.drop(['Item_Type', 'Outlet_Establishment_Year'], axis=1, inplace=True)
train = comb_data.loc[comb_data['source'] == "train_data"].drop(columns=['source'])
test = comb_data.loc[comb_data['source'] == "test_data"].drop(columns=['source', 'Item_Outlet_Sales'])
train.to_csv("D:/Github/Big Mart Sales/train_modified.csv", index=False)
test.to_csv("D:/Github/Big Mart Sales/test_modified.csv", index=False)
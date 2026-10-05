import pandas as pd
import numpy as np
train_data=pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv",na_values='.')
test_data=pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv")
train_data['source']='train_data'
test_data['source']='test_data'
comb_data = pd.concat([train_data, test_data],ignore_index=True)
print ("number of rows and columns in Train dataset ",train_data.shape)
print("number of rows and columns in Test dataset ",test_data.shape)
print("number of rows and columns in combined dataset ",comb_data.shape)
print("\nSummary for unique values\n",comb_data.apply(lambda x: len(x.unique())))
print("Summary for missing values\n",comb_data.isnull().sum())
print(comb_data.isnull().sum()/comb_data.shape[0]*100)
print("\nStatistical Summary of Item Visibility\n",comb_data['Item_Visibility'].describe())
print("\n",comb_data.describe())
category_column = [x for x in comb_data.dtypes.index if comb_data.dtypes[x]=='object']
category_column = [x for x in category_column if x not in ['Item_Identifier','Outlet_Identifier','source']]
for column in category_column:
    print ('\nFrequency of Categories for varible %s'%column)
    print (comb_data[column].value_counts())
item_avg_weight = comb_data.pivot_table(values='Item_Weight', index='Item_Identifier')
print(item_avg_weight)
miss_cells = comb_data['Item_Weight'].isnull()
print ('missing values before imputation: %d'% sum(miss_cells))
comb_data.loc[comb_data.Item_Weight.isnull(), 'Item_Weight'] = comb_data.groupby('Item_Identifier').Item_Weight.transform('mean')
print ('Final count of missing values: %d'% sum(comb_data['Item_Weight'].isnull()))
outlet_size_mode = comb_data.pivot_table(values='Outlet_Size',
                                   columns='Outlet_Type',
                                   aggfunc=lambda x: x.mode().iat[0])
print ('Mode for each Outlet_Type:')
print (outlet_size_mode)
miss_cells = comb_data['Outlet_Size'].isnull()
print ('\nOrignal missing values: %d'% sum(miss_cells))
comb_data.loc[comb_data.Outlet_Size.isnull(),'Outlet_Size']=comb_data.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x:x.fillna(x.value_counts().index.tolist()[0]))
print ('\nFinal count of missing values: %d'% sum(comb_data['Outlet_Size'].isnull()))
visibility_avg = comb_data.pivot_table(values='Item_Visibility', index='Item_Identifier')
miss_cell = (comb_data['Item_Visibility'] == 0)
print ('Number of 0 values initially: %d'%sum(miss_cell))
comb_data.loc[comb_data['Item_Visibility'] == 0,'Item_Visibility'] = comb_data.groupby('Item_Identifier').Item_Visibility.transform('mean')
print ('Number of 0 values after modification: %d'%sum(comb_data['Item_Visibility'] == 0))
comb_data['Outlet_Years'] = 2013 - comb_data['Outlet_Establishment_Year']
print(comb_data['Outlet_Years'].describe())
comb_data['Item_Type_Combined'] = comb_data['Item_Identifier'].apply(lambda x: x[0:2])
comb_data['Item_Type_Combined'] = comb_data['Item_Type_Combined'].map({'FD':'Food',
                                                             'NC':'Non-Consumable',
                                                             'DR':'Drinks'})
print(comb_data['Item_Type_Combined'].value_counts())
print ('Original Categories:')
print (comb_data['Item_Fat_Content'].value_counts())
comb_data['Item_Fat_Content'] = comb_data['Item_Fat_Content'].replace({'LF':'Low Fat',
                                                             'reg':'Regular',
                                                             'low fat':'Low Fat'})
print (comb_data['Item_Fat_Content'].value_counts)
comb_data.loc[comb_data['Item_Type_Combined']=="Non-Consumable",'Item_Fat_Content'] = "Non-Edible"
print ('\nModified Categories:')
print(comb_data['Item_Fat_Content'].value_counts())
func = lambda x: x['Item_Visibility']/visibility_avg['Item_Visibility'][visibility_avg.index == x['Item_Identifier']][0]
comb_data['Item_Visibility_MeanRatio'] = comb_data.apply(func,axis=1).astype(float)
print(comb_data['Item_Visibility_MeanRatio'].describe())
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
comb_data['Outlet'] = le.fit_transform(comb_data['Outlet_Identifier'])
var_mod = ['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Item_Type_Combined','Outlet_Type','Outlet']
for i in var_mod:
    comb_data[i] = le.fit_transform(comb_data[i])
comb_data = pd.get_dummies(comb_data, columns=['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Outlet_Type','Item_Type_Combined','Outlet'])
comb_data.drop(['Item_Type','Outlet_Establishment_Year'],axis=1,inplace=True)
train = comb_data.loc[comb_data['source']=="train_data"]
test = comb_data.loc[comb_data['source']=="test_data"]
test.drop(['Item_Outlet_Sales','source'],axis=1,inplace=True)
train.drop(['source'],axis=1,inplace=True)
train.to_csv("D:/Github/Big Mart Sales/train_modified.csv",index=False)
test.to_csv("D:/Github/Big Mart Sales/test_modified.csv",index=False)
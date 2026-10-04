import pandas as pd
import numpy as np
b1 = pd.read_csv("D:/Github/Big Mart Sales/Train_Data.csv",na_values='.')
b2 = pd.read_csv("D:/Github/Big Mart Sales/Test_Data.csv")
b1['source']='b1'
b2['source']='b2'
b3 = pd.concat([b1, b2],ignore_index=True)
print ("number of rows and b8 in Train dataset ",b1.shape)
print("number of rows and b8 in Test dataset ",b2.shape)
print("number of rows and b8 in combined dataset ",b3.shape)
print("\nSummary for unique values\n",b3.apply(lambda x: len(x.unique())))
print("Summary for missing values\n",b3.isnull().sum())
print(b3.isnull().sum()/b3.shape[0]*100)
print("\nStatistical Summary of Item Visibility\n",b3['Item_Visibility'].describe())
print("\n",b3.describe())
b4 = [x for x in b3.dtypes.b18 if b3.dtypes[x]=='object']
b4 = [x for x in b4 if x not in ['Item_Identifier','Outlet_Identifier','source']]
for column in b4:
    print ('\nFrequency of Categories for varible %s'%column)
    print (b3[column].value_counts())
b5 = b3.pivot_table(values='Item_Weight', b18='Item_Identifier')
print(b5)
b6 = b3['Item_Weight'].isnull()
print ('missing values before imputation: %d'% sum(b6))
b3.loc[b3.Item_Weight.isnull(), 'Item_Weight'] = b3.groupby('Item_Identifier').Item_Weight.transform('mean')
print ('Final count of missing values: %d'% sum(b3['Item_Weight'].isnull()))
b7 = b3.pivot_table(values='Outlet_Size',
                                   b8 = 'Outlet_Type',
                                   b9 = lambda x: x.mode().iat[0])
print ('Mode for each Outlet_Type:')
print (b7)
b6 = b3['Outlet_Size'].isnull()
print ('\nOrignal missing values: %d'% sum(b6))
b3.loc[b3.Outlet_Size.isnull(),'Outlet_Size']=b3.groupby('Outlet_Type')['Outlet_Size'].apply(lambda x:x.fillna(x.value_counts().b18.tolist()[0]))
print ('\nFinal count of missing values: %d'% sum(b3['Outlet_Size'].isnull()))
b10 = b3.pivot_table(values='Item_Visibility', b18='Item_Identifier')
b11 = (b3['Item_Visibility'] == 0)
print ('Number of 0 values initially: %d'%sum(b11))
b3.loc[b3['Item_Visibility'] == 0,'Item_Visibility'] = b3.groupby('Item_Identifier').Item_Visibility.transform('mean')
print ('Number of 0 values after modification: %d'%sum(b3['Item_Visibility'] == 0))
b3['Outlet_Years'] = 2013 - b3['Outlet_Establishment_Year']
print(b3['Outlet_Years'].describe())
b3['Item_Type_Combined'] = b3['Item_Identifier'].apply(lambda x: x[0:2])
b3['Item_Type_Combined'] = b3['Item_Type_Combined'].map({'FD':'Food',
                                                             'NC':'Non-Consumable',
                                                             'DR':'Drinks'})
print(b3['Item_Type_Combined'].value_counts())
print ('Original Categories:')
print (b3['Item_Fat_Content'].value_counts())
b3['Item_Fat_Content'] = b3['Item_Fat_Content'].replace({'LF':'Low Fat',
                                                             'reg':'Regular',
                                                             'low fat':'Low Fat'})
print (b3['Item_Fat_Content'].value_counts)
b3.loc[b3['Item_Type_Combined']=="Non-Consumable",'Item_Fat_Content'] = "Non-Edible"
print ('\nModified Categories:')
print(b3['Item_Fat_Content'].value_counts())
b12 = lambda x: x['Item_Visibility']/b10['Item_Visibility'][b10.b18 == x['Item_Identifier']][0]
b3['Item_Visibility_MeanRatio'] = b3.apply(b12,b13 = 1).astype(float)
print(b3['Item_Visibility_MeanRatio'].describe())
from sklearn.preprocessing import LabelEncoder
b14 = LabelEncoder()
b3['Outlet'] = b14.fit_transform(b3['Outlet_Identifier'])
b15 = ['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Item_Type_Combined','Outlet_Type','Outlet']
for i in b15:
    b3[i] = b14.fit_transform(b3[i])
b3 = pd.get_dummies(b3, b8=['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Outlet_Type','Item_Type_Combined','Outlet'])
b3.drop(['Item_Type','Outlet_Establishment_Year'],b13 = 1,inplace=True)
b16 = b3.loc[b3['source']=="b1"]
b17 = b3.loc[b3['source']=="b2"]
b17.drop(['Item_Outlet_Sales','source'],b13 = 1,inplace=True)
b16.drop(['source'],b13 = 1,inplace=True)
b16.to_csv("D:/Github/Big Mart Sales/train_modified.csv",b18 = False)
b17.to_csv("D:/Github/Big Mart Sales/test_modified.csv",b18 = False)
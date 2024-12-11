
import pandas as pd
import numpy as np
from fbprophet import Prophet
from datetime import datetime,date
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from math import sqrt
b1 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx',b29='newtable')
b1.head()
b1.dtypes
b1['start_time']=pd.to_datetime(b1['start_time'],b2 = "%d/%b22/%Y %I:%M:%S %p")
b1['end_time']=pd.to_datetime(b1['end_time'],b2 = "%d/%b22/%Y %I:%M:%S %p")
def fonk1(b6,duration,time):
   a1 = 1.75
   if(time<date(b3 = 2018,month=7,day=12)):
      a1 = 3.5
   a2 = 0
   b4 = int(duration/30)
   b5 = duration %30
   if(b5!=0):
      b4 = b4+1
   if(b6 = = 'Monthly Pass' or b6== 'Annual Pass' or b6 == 'One Day Pass' or b6 == 'Flex Pass'):
      b4 = b4-1
   if(b4<0):
      b4 = 0
   a2 = a1*b4
   return a2
b7 = list()
for b6,duration,time in zip(b1['passholder_type'],b1['trip_duration'],b1['start_time']):
    b7.append(fonk1(b6,duration,time.date()))
b1['revenue']=b7
b1['end_time'].head(10)
b8 = pd.pivot_table(b1[['revenue','start_time']],aggfunc='sum',b9=b1['start_time'].dt.date,columns=['revenue'],fill_value=0)
b8.b9 = pd.to_datetime(b8.b9)
b10 = pd.DataFrame()
b11 = []
b12 = []
for i,v in enumerate(b8.columns):
    def fonk2(b1,b13 = 0):
        b14 = pd.DataFrame()
        b14['ds'] = b1.b9
        b14['y'] = list(b1.iloc[:,i])
        return(b14)
    def fonk3(b8,b15 = 'D',train_prop = 0.80):
        b8 = b8.resample(b15).sum()
        b16 = ['2016-08-14','2018-10-16','2017-03-26','2017-05-11','2017-08-13','2017-10-08',\
           '2017-12-10','2018-04-22','2018-06-24','2018-09-30','2018-12-02']
        b8['temp']=b8.b9
        for l in b16:
            b8 = b8[b8.temp!=l]
        b8.drop('temp',b17 = 1,inplace=True)
        b18 = pd.DataFrame()
        b19 = pd.DataFrame()
        b18 = b8.loc[b8.b9[:int(train_prop*len(b8.b9))]]
        b19 = b8.loc[b8.b9[int(train_prop*len(b8.b9)):]]
        b18 = fonk2(b18,i)
        b19 = fonk2(b19,i)
        return(b18,b19)
    b20 = 'D'
    trn, b21 = fonk3(b8,b20)
    b22 = Prophet(yearly_seasonality=True,weekly_seasonality= True,daily_seasonality=True)
    b22.fit(trn)
    b23 = b22.make_future_dataframe(periods=len(b21),freq=b20)
    b24 = b22.predict(b23)
    b10[v]=b24['yhat']
    b25 = b21['y']
    b26 = b10[v][b10.b9[int(0.8*len(b10.b9)):]]
    b12.append(sqrt(mean_squared_error(b25, b26)))
    b27 = trn['y']
    b28 = b10[v][b10.b9[:int(0.8*len(b10.b9))]]
    b11.append(sqrt(mean_squared_error(b27, b28)))
b10['ds']=b24['ds']
b16 = ['2016-08-14','2018-10-16','2017-03-26','2017-05-11','2017-08-13','2017-10-08',\
           '2017-12-10','2018-04-22','2018-06-24','2018-09-30','2018-12-02']
b8['ds']=b8.b9
for l in b16:
    b8 = b8[b8.ds!=l]
b8 = b8.reset_index(drop=True)
b11 = pd.DataFrame(b11)
b12 = pd.DataFrame(b12)
with pd.ExcelWriter('outputY_Passholder.xlsx') as writer:
    b8.to_excel(writer,b29 = 'actual(YWD)')
    b10.to_excel(writer,b29 = 'predicted(YWD)')
    b11.to_excel(writer,b29 = 'b11(YWD)')
    b12.to_excel(writer,b29 = 'b12(YWD)')

import pandas as pd
import numpy as np
from fbprophet import Prophet
from datetime import datetime,date
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from math import sqrt
df = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx',sheet_name='newtable')
df.head()
df.dtypes
df['start_time']=pd.to_datetime(df['start_time'],format="%d/%m/%Y %I:%M:%S %p")
df['end_time']=pd.to_datetime(df['end_time'],format="%d/%m/%Y %I:%M:%S %p")
def revenue(passtype,duration,time):
   perthirty=1.75
   if(time<date(year=2018,month=7,day=12)):
      perthirty=3.5
   cost=0
   qty=int(duration/30)
   extra=duration %30
   if(extra!=0):
      qty=qty+1
   if(passtype== 'Monthly Pass' or passtype== 'Annual Pass' or passtype == 'One Day Pass' or passtype == 'Flex Pass'):
      qty=qty-1
   if(qty<0):
      qty=0
   cost=perthirty*qty
   return cost
rev=list()
for passtype,duration,time in zip(df['passholder_type'],df['trip_duration'],df['start_time']):
    rev.append(revenue(passtype,duration,time.date()))
df['revenue']=rev
df['end_time'].head(10)
df_d = pd.pivot_table(df[['revenue','start_time']],aggfunc='sum',index=df['start_time'].dt.date,columns=['revenue'],fill_value=0)
df_d.index = pd.to_datetime(df_d.index)
df_o=pd.DataFrame()
mse_trn=[]
mse_tst=[]
for i,v in enumerate(df_d.columns):
    def prophet_inputize(df,column_num = 0):
        df_1 = pd.DataFrame()
        df_1['ds'] = df.index
        df_1['y'] = list(df.iloc[:,i])
        return(df_1)
    def do_something(df_d,sample ='D',train_prop = 0.80):
        df_d = df_d.resample(sample).sum()
        rem=['2016-08-14','2018-10-16','2017-03-26','2017-05-11','2017-08-13','2017-10-08',\
           '2017-12-10','2018-04-22','2018-06-24','2018-09-30','2018-12-02']
        df_d['temp']=df_d.index
        for l in rem:
            df_d=df_d[df_d.temp!=l]
        df_d.drop('temp',axis=1,inplace=True)
        df_d_trn = pd.DataFrame()
        df_d_tst = pd.DataFrame()
        df_d_trn = df_d.loc[df_d.index[:int(train_prop*len(df_d.index))]]
        df_d_tst = df_d.loc[df_d.index[int(train_prop*len(df_d.index)):]]
        df_d_trn = prophet_inputize(df_d_trn,i)
        df_d_tst = prophet_inputize(df_d_tst,i)
        return(df_d_trn,df_d_tst)
    sample_freq = 'D'
    trn, tst = do_something(df_d,sample_freq)
    m = Prophet(yearly_seasonality=True,weekly_seasonality= True,daily_seasonality=True)
    m.fit(trn)
    future = m.make_future_dataframe(periods=len(tst),freq=sample_freq)
    forecast = m.predict(future)
    df_o[v]=forecast['yhat']
    y_actual_tst=tst['y']
    y_predicted_tst=df_o[v][df_o.index[int(0.8*len(df_o.index)):]]
    mse_tst.append(sqrt(mean_squared_error(y_actual_tst, y_predicted_tst)))
    y_actual_trn=trn['y']
    y_predicted_trn=df_o[v][df_o.index[:int(0.8*len(df_o.index))]]
    mse_trn.append(sqrt(mean_squared_error(y_actual_trn, y_predicted_trn)))
df_o['ds']=forecast['ds']
rem=['2016-08-14','2018-10-16','2017-03-26','2017-05-11','2017-08-13','2017-10-08',\
           '2017-12-10','2018-04-22','2018-06-24','2018-09-30','2018-12-02']
df_d['ds']=df_d.index
for l in rem:
    df_d=df_d[df_d.ds!=l]
df_d=df_d.reset_index(drop=True)
mse_trn=pd.DataFrame(mse_trn)
mse_tst=pd.DataFrame(mse_tst)
with pd.ExcelWriter('outputY_Passholder.xlsx') as writer:
    df_d.to_excel(writer,sheet_name='actual(YWD)')
    df_o.to_excel(writer,sheet_name='predicted(YWD)')
    mse_trn.to_excel(writer,sheet_name='mse_trn(YWD)')
    mse_tst.to_excel(writer,sheet_name='mse_tst(YWD)')
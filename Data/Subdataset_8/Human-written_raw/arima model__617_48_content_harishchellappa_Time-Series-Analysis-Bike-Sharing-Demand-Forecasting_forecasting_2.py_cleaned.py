
import pandas as pd
import numpy as np
from fbprophet import Prophet
from datetime import datetime
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from math import sqrt
df = pd.read_excel('newtable.xlsx',sheet_name='newtable')
df.head()
df.dtypes
df['start_time']=pd.to_datetime(df['start_time'],format="%d/%m/%Y %I:%M:%S %p")
df['end_time']=pd.to_datetime(df['end_time'],format="%d/%m/%Y %I:%M:%S %p")
df_d = pd.pivot_table(df[['start_station','start_time']],aggfunc='count',index=df['start_time'].dt.date,columns=['start_station'],fill_value=0)
ial=[('start_time',3021),	('start_time',3053),	('start_time',3055),	('start_time',3059),
     ('start_time',3060),	('start_time',3061),	('start_time',3079),	('start_time',3080),
     ('start_time',4108),	('start_time',4138),	('start_time',4142),	('start_time',4143),
     ('start_time',4144),	('start_time',4146),	('start_time',4147),	('start_time',4148),
     ('start_time',4149),	('start_time',4150),	('start_time',4151),	('start_time',4152),
     ('start_time',4153),	('start_time',4154),	('start_time',4155),	('start_time',4156),
     ('start_time',4157),	('start_time',4158),	('start_time',4159),	('start_time',4160),
     ('start_time',4162),	('start_time',4163),	('start_time',4165),	('start_time',4166),
     ('start_time',4167),	('start_time',4169),	('start_time',4170),	('start_time',4174),
     ('start_time',4176),	('start_time',4177),	('start_time',4180),	('start_time',4181),
     ('start_time',4183),	('start_time',4194),	('start_time',4244),
     ('start_time',4276)]
df_d.drop(labels=ial,axis=1,inplace=True)
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
    def do_something(df_d,sample ='D',test =-184):
        rem=['2016-08-14','2018-10-16','2017-03-26','2017-05-11','2017-08-13','2017-10-08',\
           '2017-12-10','2018-04-22','2018-06-24','2018-09-30','2018-12-02']
        df_d['temp']=df_d.index
        for l in rem:
            df_d=df_d[df_d.temp!=l]
        df_d.drop('temp',axis=1,inplace=True)
        df_d_trn = pd.DataFrame()
        df_d_tst = pd.DataFrame()
        df_d_trn = df_d.loc[df_d.index[:test]]
        df_d_tst = df_d.loc[df_d.index[test:]]
        df_d_trn = prophet_inputize(df_d_trn,i)
        df_d_tst = prophet_inputize(df_d_tst,i)
        return(df_d_trn,df_d_tst)
    sample_freq = 'D'
    trn, tst = do_something(df_d,sample_freq,-184)
    m = Prophet(yearly_seasonality=True,weekly_seasonality= False,daily_seasonality=False)
    m.fit(trn)
    future = m.make_future_dataframe(periods=len(tst)+90+3,freq=sample_freq)
    forecast = m.predict(future)
    df_o[v]=forecast['yhat']
    y_actual_tst=tst['y']
    y_predicted_tst=df_o[v][df_o.index[-184:]]
    mse_tst.append(sqrt(mean_squared_error(y_actual_tst, y_predicted_tst)))
    y_actual_trn=trn['y']
    y_predicted_trn=df_o[v][df_o.index[:-184-93]]
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
with pd.ExcelWriter('outputY.xlsx') as writer:
    df_d.to_excel(writer,sheet_name='actual(Y)')
    df_o.to_excel(writer,sheet_name='predicted(Y)')
    mse_trn.to_excel(writer,sheet_name='mse_trn(Y)')
    mse_tst.to_excel(writer,sheet_name='mse_tst(Y)')
 '''
df_o.tail()
tst.tail()
df_o.loc[df_o.index[int(0.8*len(df_o.index)):]].plot(x='ds',y=v)
tst.plot(x='ds',y='y')
y_actual=tst['y']
y_predicted=df_o[v][df_o.index[int(0.8*len(df_o.index)):]]
mse = sqrt(mean_squared_error(y_actual, y_predicted))
print(mse)
'''
'''
mse with weekly 11.685
mse without weekly 13.04
'''
dft1=pd.DataFrame(list(df_d['index']),columns=['ds'])
dft1.rename(columns={'0':'ds'}, inplace=True)
dft1['y']=list(df_d.iloc[:,0])
dft1.head()
dft2=dft1.iloc[0:-25,:]
dft2.tail()
dftv=dft1.iloc[-25:,:]
dftv.head()
dft2.plot(x='ds',y='y')
dftv.plot(x='ds',y='y')
m=Prophet()
m.fit(dft2)
future = m.make_future_dataframe(periods=25)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
df_m['index']=df_m.index
dft1 = pd.DataFrame(list(df_m['index']))
dft1['y']=list(df_m.iloc[:,0])
dft1.head()
df_m.columns[0]
df_m.plot(x='index',y=df_m.columns[0])
dft2=dft1.iloc[0:-25,:]
dft2.tail()
dftv=dft1.iloc[-25:,:]
dftv.head()
dft2.plot(x='ds',y='y')
dftv.plot(x='ds',y='y')
m=Prophet()
m.fit(dft2)
future = m.make_future_dataframe(periods=25)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast)
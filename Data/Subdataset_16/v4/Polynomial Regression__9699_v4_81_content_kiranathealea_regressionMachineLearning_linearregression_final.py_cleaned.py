import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
b1 = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY',
    'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan',
    'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya'
]
b2 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'
b3 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear/'
for kota in b1:
    b4 = os.path.join(b2, f'{kota}.csv')
    b5 = pd.read_csv(b4, usecols=['Year'])
    b6 = np.array(b5).ravel()
    b7 = pd.read_csv(b4, usecols=['Crop'])
    b8 = np.array(b7)
    b9 = LinearRegression()
    b9.fit(b6.reshape(-1, 1), b8)
    b10 = b9.predict(b6.reshape(-1, 1))
    b11 = mean_squared_error(b8, b10)
    b12 = r2_score(b8, b10)
    print(f'The RMSE of the linear regression b9 for {kota} is {b11}')
    print(f'The R2 score of the linear regression b9 for {kota} is {b12}')
    b13 = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    b14 = b9.predict(b13)
    b14 = np.round(b14, 4)
    b15 = np.concatenate((b6, b13.ravel()))
    b16 = np.concatenate((b10.ravel(), b14.ravel()))
    b17 = pd.read_csv(b4, usecols=['Entity']).iloc[0, 0]
    b18 = pd.read_csv(b4, usecols=['Code']).iloc[0, 0]
    b17 = [b17] * len(b15)
    b18 = [b18] * len(b15)
    b19 = DataFrame({
        'Entity': b17,
        'Code': b18,
        'Year': b15,
        'crop(tonnes per hectare)': b16
    })
    b20 = os.path.join(b3, f'{kota}_tomato.csv')
    b19.to_csv(b20, b21 = False)
os.chdir(b3)
b22 = glob.glob('*.csv')
b23 = pd.concat([pd.read_csv(f) for f in b22])
b23.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_tomato.csv", b21 = False, encoding='utf-8-sig')
print('All done')
import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from pandas import DataFrame
b1 = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur',
    'Cirebon', 'DIY', 'Garut', 'Gunung Kidul', 'Indramayu',
    'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka',
    'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang',
    'Tasikmalaya'
]
b2 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'
b3 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly/'
b4 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly_tomato.csv'
for city in b1:
    b5 = os.path.join(b2, city + ".csv")
    b6 = pd.read_csv(b5, usecols=['Year'])
    b7 = pd.read_csv(b5, usecols=['Crop'])
    b8 = np.array(b6).ravel()
    b9 = np.array(b7)
    b10 = PolynomialFeatures(degree=2)
    b11 = b10.fit_transform(b8.reshape(-1, 1))
    b12 = LinearRegression()
    b12.fit(b11, b9)
    b13 = b12.predict(b11)
    b14 = mean_squared_error(b9, b13)
    b15 = r2_score(b9, b13)
    print(f'The RMSE of the linear regression b12 for {city} is {b14}')
    print(f'The R2 score of the linear regression b12 for {city} is {b15}')
    b16 = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    b17 = b10.fit_transform(b16)
    b18 = b12.predict(b17)
    b19 = np.concatenate((b8, b16.ravel()))
    b20 = np.concatenate((b13, b18)).ravel()
    b21 = np.concatenate((b9, b18)).ravel()
    b22 = pd.read_csv(b5, usecols=['Entity']).values.ravel()
    b23 = pd.read_csv(b5, usecols=['Code']).values.ravel()
    b24 = np.concatenate((b22, b22[:6]))
    b25 = np.concatenate((b23, b23[:6]))
    b26 = DataFrame({
        'Entity': b24,
        'Code': b25,
        'Year': b19,
        'crop(tonnes per hectare)': b21
    })
    b27 = os.path.join(b3, city + '_tomato.csv')
    b26.to_csv(b27, b28 = False)
os.chdir(b3)
b29 = [f for f in glob.glob('*.csv')]
b30 = pd.concat([pd.read_csv(f) for f in b29])
b30.to_csv(b4, b28 = False, encoding='utf-8-sig')
print('All done')
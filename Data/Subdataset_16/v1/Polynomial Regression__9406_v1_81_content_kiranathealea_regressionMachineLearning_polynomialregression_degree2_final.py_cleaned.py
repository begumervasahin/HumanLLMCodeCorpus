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
for kota in b1:
    b5 = os.path.join(b2, kota + ".csv")
    b6 = pd.read_csv(b5, usecols=['Year'])
    b7 = np.array(b6)
    b8 = b7.ravel()
    b9 = pd.read_csv(b5, usecols=['Crop'])
    b10 = np.array(b9)
    b11 = PolynomialFeatures(degree=2)
    b12 = b11.fit_transform(b7)
    b13 = LinearRegression()
    b13.fit(b12, b10)
    b14 = b13.predict(b12)
    b15 = mean_squared_error(b10, b14)
    b16 = r2_score(b10, b14)
    print(f'The RMSE of the linear regression b13 for {kota} is {b15}')
    print(f'The R2 score of the linear regression b13 for {kota} is {b16}')
    b17 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
    b18 = b17[:, np.newaxis]
    b18 = b11.fit_transform(b18)
    b19 = b13.predict(b18)
    b19 = np.round(b19, 4)
    b20 = np.concatenate((b8, b17))
    b21 = np.concatenate((b14, b19))
    b22 = np.concatenate((b10, b19))
    b23 = pd.read_csv(b5, usecols=['Entity'])
    b23 = np.array(b23).ravel()
    b24 = b23[0:6]
    b23 = np.concatenate((b23, b24))
    b25 = pd.read_csv(b5, usecols=['Code'])
    b25 = np.array(b25).ravel()
    b26 = b25[0:6]
    b25 = np.concatenate((b25, b26))
    b27 = {
        'Entity': b23,
        'Code': b25,
        'Year': b20,
        'crop(tonnes per hectare)': b22.ravel()
    }
    b28 = DataFrame(b27, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
    b29 = os.path.join(b3, kota + '_tomato.csv')
    b28.to_csv(b29, b30 = None, header=True)
os.chdir(b3)
b31 = 'csv'
b32 = [i for i in glob.glob(f'*.{b31}')]
b33 = pd.concat([pd.read_csv(f) for f in b32])
b33.to_csv(b4, b30 = False, encoding='utf-8-sig')
print('All done')
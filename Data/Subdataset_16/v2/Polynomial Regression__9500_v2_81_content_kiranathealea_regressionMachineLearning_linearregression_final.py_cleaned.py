import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
b1 = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY', 'Garut',
    'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka',
    'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya'
]
for city in b1:
    b2 = f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/{city}.csv'
    b3 = pd.read_csv(b2, usecols=['Year'])
    b4 = pd.read_csv(b2, usecols=['Crop'])
    b5 = np.array(b3).reshape(-1, 1)
    b6 = np.array(b4).reshape(-1, 1)
    b7 = LinearRegression()
    b7.fit(b5, b6)
    b8 = b7.predict(b5)
    b9 = mean_squared_error(b6, b8)
    b10 = r2_score(b6, b8)
    print(f'The RMSE of the linear regression b7 for {city} is {b9}')
    print(f'The R2 score of the linear regression b7 for {city} is {b10}')
    b11 = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    b12 = np.round(b7.predict(b11), 4)
    b13 = np.concatenate((b5, b11))
    b14 = np.concatenate((b8, b12))
    b15 = np.concatenate((b6, b12))
    b16 = pd.read_csv(b2, usecols=['Entity']).values.ravel()
    b17 = pd.read_csv(b2, usecols=['Code']).values.ravel()
    b18 = np.concatenate((b16, b16[:6]))
    b19 = np.concatenate((b17, b17[:6]))
    b20 = pd.DataFrame({
        'Entity': b18,
        'Code': b19,
        'Year': b13.ravel(),
        'crop(tonnes per hectare)': b15.ravel()
    })
    b20.to_csv(f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear/{city}_tomato.csv', b21 = False)
b22 = "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear"
os.chdir(b22)
b23 = glob.glob('*.csv')
b24 = pd.concat([pd.read_csv(f) for f in b23])
b24.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_tomato.csv", b21 = False, encoding='utf-8-sig')
print('All done')
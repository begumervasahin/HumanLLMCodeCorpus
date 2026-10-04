import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
b1 = ['Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya']
for city in b1:
    b2 = f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/{city}.csv'
    b3 = pd.read_csv(b2, usecols=['Year'])
    b4 = pd.read_csv(b2, usecols=['Crop'])
    b5 = b3.values
    b6 = b4.values
    b7 = b5.ravel()
    b8 = PolynomialFeatures(degree=3)
    b9 = b8.fit_transform(b5)
    b10 = LinearRegression()
    b10.fit(b9, b6)
    b11 = b10.predict(b9)
    b12 = mean_squared_error(b6, b11)
    b13 = r2_score(b6, b11)
    print(f'The RMSE of the linear regression b10 for {city} is {b12}')
    print(f'The R2 score of the linear regression b10 for {city} is {b13}')
    b14 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
    b15 = b8.fit_transform(b14[:, np.newaxis])
    b16 = b10.predict(b15)
    b16 = np.round(b16, 4)
    b17 = np.concatenate((b7, b14))
    b18 = np.concatenate((b11, b16))
    b19 = np.concatenate((b6, b16))
    b20 = pd.read_csv(b2, usecols=['Entity']).values.ravel()
    b20 = np.concatenate((b20, b20[:6]))
    b21 = pd.read_csv(b2, usecols=['Code']).values.ravel()
    b21 = np.concatenate((b21, b21[:6]))
    b22 = {
        'Entity': b20,
        'Code': b21,
        'Year': b17,
        'Crop (tonnes per hectare)': b19.ravel()
    }
    b23 = pd.DataFrame(b22)
    b24 = f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly2/{city}_tomato.csv'
    b23.to_csv(b24, b25 = False)
else:
    b26 = "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly2"
    os.chdir(b26)
    b27 = glob.glob('*.csv')
    b28 = pd.concat([pd.read_csv(f) for f in b27])
    b28.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly2_tomato.csv", b25 = False, encoding='utf-8-sig')
    print('All done')
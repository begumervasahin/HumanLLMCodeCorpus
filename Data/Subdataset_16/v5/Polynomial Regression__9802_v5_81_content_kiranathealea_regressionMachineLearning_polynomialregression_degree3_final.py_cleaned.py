import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
b1 = ['Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya']
def fonk1(city):
    b2 = f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/{city}.csv'
    b3 = pd.read_csv(b2, usecols=['Year'])
    b4 = pd.read_csv(b2, usecols=['Crop'])
    b5 = pd.read_csv(b2, usecols=['Entity']).values.ravel()
    b6 = pd.read_csv(b2, usecols=['Code']).values.ravel()
    b7 = b3.values
    b8 = b4.values
    b9 = b7.ravel()
    b10 = PolynomialFeatures(degree=3)
    b11 = b10.fit_transform(b7)
    b12 = LinearRegression()
    b12.fit(b11, b8)
    b13 = b12.predict(b11)
    b14 = mean_squared_error(b8, b13)
    b15 = r2_score(b8, b13)
    print(f'The RMSE of the linear regression b12 for {city} is {b14}')
    print(f'The R2 score of the linear regression b12 for {city} is {b15}')
    b16 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
    b17 = b10.fit_transform(b16[:, np.newaxis])
    b18 = b12.predict(b17)
    b18 = np.round(b18, 4)
    b19 = np.concatenate((b9, b16))
    b20 = np.concatenate((b13, b18))
    b21 = np.concatenate((b8, b18))
    b22 = np.concatenate((b5, b5[:6]))
    b23 = np.concatenate((b6, b6[:6]))
    b24 = {
        'Entity': b22,
        'Code': b23,
        'Year': b19,
        'Crop (tonnes per hectare)': b21.ravel()
    }
    b25 = pd.DataFrame(b24)
    b26 = f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly2/{city}_tomato.csv'
    b25.to_csv(b26, b27 = False)
for city in b1:
    fonk1(city)
b28 = "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly2"
os.chdir(b28)
b29 = glob.glob('*.csv')
b30 = pd.concat([pd.read_csv(f) for f in b29])
b30.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly2_tomato.csv", b27 = False, encoding='utf-8-sig')
print('All done')
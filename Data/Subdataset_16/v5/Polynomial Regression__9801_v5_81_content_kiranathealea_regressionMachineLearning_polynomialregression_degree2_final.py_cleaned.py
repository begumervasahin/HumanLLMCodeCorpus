import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
b1 = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon',
    'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo',
    'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi',
    'Sumedang', 'Tasikmalaya'
]
b2 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'
b3 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/b9/'
b4 = "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly_tomato.csv"
for kota in b1[:-2]:
    b5 = os.path.join(b2, f"{kota}.csv")
    b6 = pd.read_csv(b5)
    b7 = b6['Year'].values.reshape(-1, 1)
    b8 = b6['Crop'].values
    b9 = PolynomialFeatures(degree=2)
    b10 = b9.fit_transform(b7)
    b11 = LinearRegression()
    b11.fit(b10, b8)
    b12 = b11.predict(b10)
    b13 = mean_squared_error(b8, b12)
    b14 = r2_score(b8, b12)
    print(f'The RMSE of the polynomial regression b11 for {kota} is {b13}')
    print(f'The R2 score of the polynomial regression b11 for {kota} is {b14}')
    b15 = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    b16 = b9.transform(b15)
    b17 = b11.predict(b16)
    b18 = np.concatenate((b7.ravel(), b15.ravel()))
    b19 = np.concatenate((b12, b17))
    b20 = np.concatenate((b8, b17))
    b21 = np.concatenate((b6['Entity'].values, b6['Entity'].values[:6]))
    b22 = np.concatenate((b6['Code'].values, b6['Code'].values[:6]))
    b23 = pd.DataFrame({
        'Entity': b21,
        'Code': b22,
        'Year': b18,
        'crop(tonnes per hectare)': b20
    })
    b23.to_csv(os.path.join(b3, f"{kota}_tomato.csv"), b24 = False)
os.chdir(b3)
b25 = glob.glob('*.csv')
b26 = pd.concat([pd.read_csv(f) for f in b25])
b26.to_csv(b4, b24 = False, encoding='utf-8-sig')
print('All done')
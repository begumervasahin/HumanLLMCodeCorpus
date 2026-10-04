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
for kota in b1[:-2]:
    b2 = f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/{kota}.csv'
    b3 = pd.read_csv(b2, usecols=['Year'])
    b4 = pd.read_csv(b2, usecols=['Crop'])
    b5 = np.array(b3).ravel()
    b6 = np.array(b4).ravel()
    b7 = PolynomialFeatures(degree=2)
    b8 = b7.fit_transform(b5[:, np.newaxis])
    b9 = LinearRegression()
    b9.fit(b8, b6)
    b10 = b9.predict(b8)
    b11 = mean_squared_error(b6, b10)
    b12 = r2_score(b6, b10)
    print(f'The RMSE of the linear regression b9 for {kota} is {b11}')
    print(f'The R2 score of the linear regression b9 for {kota} is {b12}')
    b13 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
    b14 = b7.transform(b13[:, np.newaxis])
    b15 = b9.predict(b14)
    b16 = np.concatenate((b5, b13))
    b17 = np.concatenate((b10, b15))
    b18 = np.concatenate((b6, b15))
    b19 = pd.read_csv(b2, usecols=['Entity']).values.ravel()
    b20 = pd.read_csv(b2, usecols=['Code']).values.ravel()
    b21 = np.concatenate((b19, b19[:6]))
    b22 = np.concatenate((b20, b20[:6]))
    b23 = {
        'Entity': b21,
        'Code': b22,
        'Year': b16,
        'crop(tonnes per hectare)': b18
    }
    b24 = pd.DataFrame(b23)
    b25 = f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly/{kota}_tomato.csv'
    b24.to_csv(b25, b26 = False)
os.chdir("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly")
b27 = 'csv'
b28 = glob.glob(f'*.{b27}')
b29 = pd.concat([pd.read_csv(f) for f in b28])
b29.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly_tomato.csv", b26 = False, encoding='utf-8-sig')
print('All done')
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
b3 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly2/'
def fonk1(city):
    b4 = os.path.join(b2, city + ".csv")
    b5 = pd.read_csv(b4)
    b6 = b5['Year'].values.reshape(-1, 1)
    b7 = b5['Crop'].values.reshape(-1, 1)
    b8 = PolynomialFeatures(degree=3)
    b9 = b8.fit_transform(b6)
    b10 = LinearRegression()
    b10.fit(b9, b7)
    b11 = b10.predict(b9)
    b12 = mean_squared_error(b7, b11)
    b13 = r2_score(b7, b11)
    print(f'The RMSE of the linear regression b10 for {city} is {b12}')
    print(f'The R2 score of the linear regression b10 for {city} is {b13}')
    b14 = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    b15 = b8.transform(b14)
    b16 = b10.predict(b15)
    b17 = np.concatenate((b6.ravel(), b14.ravel()))
    b18 = np.concatenate((b11.ravel(), b16.ravel()))
    b19 = np.concatenate((b7.ravel(), b16.ravel()))
    b20 = np.concatenate((b5['Entity'].values, b5['Entity'].values[:6]))
    b21 = np.concatenate((b5['Code'].values, b5['Code'].values[:6]))
    b22 = pd.DataFrame({
        'Entity': b20,
        'Code': b21,
        'Year': b17,
        'crop(tonnes per hectare)': b19
    })
    b22.to_csv(os.path.join(b3, f'{city}_tomato.csv'), b23 = False)
for city in b1[:19]:
    fonk1(city)
os.chdir(b3)
b24 = 'csv'
b25 = glob.glob(f'*.{b24}')
b26 = pd.concat([pd.read_csv(f) for f in b25])
b26.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly2_tomato.csv", b23 = False, encoding='utf-8-sig')
print('All done')
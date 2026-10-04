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
def fonk1(b16):
    b4 = pd.read_csv(b16)
    b5 = b4['Year'].values.reshape(-1, 1)
    b6 = b4['Crop'].values.reshape(-1, 1)
    b7 = b4['Entity'].values
    b8 = b4['Code'].values
    return b5, b6, b7, b8
def fonk2(b5, b6, b9 = 3):
    b10 = PolynomialFeatures(b9=b9)
    b11 = b10.fit_transform(b5)
    b12 = LinearRegression()
    b12.fit(b11, b6)
    return b12, b10, b11
def fonk3(b12, b10, b20):
    b13 = b10.transform(b20)
    return b12.predict(b13)
def fonk4(city, b7, b8, b22, b23, output_folder):
    b14 = pd.DataFrame({
        'Entity': b7,
        'Code': b8,
        'Year': b22,
        'crop(tonnes per hectare)': b23
    })
    b14.to_csv(os.path.join(output_folder, f'{city}_tomato.csv'), b15 = False)
def fonk5(city):
    b16 = os.path.join(b2, city + ".csv")
    b5, b6, b7, b8 = fonk1(b16)
    b12, b10, b11 = fonk2(b5, b6)
    b17 = b12.predict(b11)
    b18 = mean_squared_error(b6, b17)
    b19 = r2_score(b6, b17)
    print(f'The RMSE of the linear regression b12 for {city} is {b18}')
    print(f'The R2 score of the linear regression b12 for {city} is {b19}')
    b20 = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    b21 = fonk3(b12, b10, b20)
    b22 = np.concatenate((b5.ravel(), b20.ravel()))
    b23 = np.concatenate((b6.ravel(), b21.ravel()))
    b24 = np.concatenate((b7, b7[:len(b20)]))
    b25 = np.concatenate((b8, b8[:len(b20)]))
    fonk4(city, b24, b25, b22, b23, b3)
def fonk6(output_folder):
    os.chdir(output_folder)
    b26 = 'csv'
    b27 = glob.glob(f'*.{b26}')
    b28 = pd.concat([pd.read_csv(f) for f in b27])
    b28.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly2_tomato.csv", b15 = False, encoding='utf-8-sig')
def fonk7():
    for city in b1[:19]:
        fonk5(city)
    fonk6(b3)
    print('All done')
if b29 = = "__main__":
    fonk7()
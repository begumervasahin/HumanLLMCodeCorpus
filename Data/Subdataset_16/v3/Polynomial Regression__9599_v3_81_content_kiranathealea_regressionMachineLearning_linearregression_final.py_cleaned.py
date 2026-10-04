import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
def fonk1(b15):
    b1 = pd.read_csv(b15, usecols=['Year'])
    b2 = pd.read_csv(b15, usecols=['Crop'])
    return b1.values.reshape(-1, 1), b2.values.reshape(-1, 1)
def fonk2(x, b16):
    b3 = LinearRegression()
    b3.fit(x, b16)
    b4 = b3.predict(x)
    b5 = mean_squared_error(b16, b4)
    b6 = r2_score(b16, b4)
    return b3, b4, b5, b6
def fonk3(b3, years):
    b7 = np.round(b3.predict(years.reshape(-1, 1)), 4)
    return b7
def fonk4(x, b4, b17, b7):
    b8 = np.concatenate((x, b17))
    b9 = np.concatenate((b4, b7))
    return b8, b9
def fonk5(original_data):
    return np.concatenate((original_data, original_data[:6]))
def fonk6(city, b8, b18, b19, b20):
    b10 = fonk5(b19)
    b11 = fonk5(b20)
    b12 = pd.DataFrame({
        'Entity': b10,
        'Code': b11,
        'Year': b8.ravel(),
        'crop(tonnes per hectare)': b18.ravel()
    })
    return b12
def fonk7(df, path):
    df.to_csv(path, b13 = False)
def fonk8():
    b14 = [
        'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY', 'Garut',
        'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka',
        'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya'
    ]
    for city in b14:
        b15 = f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/{city}.csv'
        x, b16 = fonk1(b15)
        b3, b4, b5, b6 = fonk2(x, b16)
        print(f'The RMSE of the linear regression b3 for {city} is {b5}')
        print(f'The R2 score of the linear regression b3 for {city} is {b6}')
        b17 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
        b7 = fonk3(b3, b17)
        b8, b9 = fonk4(x, b4, b17, b7)
        b18 = np.concatenate((b16, b7))
        b19 = pd.read_csv(b15, usecols=['Entity']).values.ravel()
        b20 = pd.read_csv(b15, usecols=['Code']).values.ravel()
        b12 = fonk6(city, b8, b18, b19, b20)
        fonk7(b12, f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear/{city}_tomato.csv')
    b21 = "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear"
    os.chdir(b21)
    b22 = glob.glob('*.csv')
    b23 = pd.concat([pd.read_csv(f) for f in b22])
    fonk7(b23, "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_tomato.csv")
    print('All done')
if b24 = = "__main__":
    fonk8()
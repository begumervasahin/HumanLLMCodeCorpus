import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
b1 = ['Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya']
a1 = 0
for a1 in range (19):
    b2 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'+b1[a1]+".csv"
    b3 = pd.read_csv(b2, usecols = ['Year'])
    b4 = np.array(b3)
    b5 = b4.ravel()
    b6 = pd.read_csv(b2, usecols = ['Crop'])
    b7 = np.array(b6)
    b8 = PolynomialFeatures(degree=2)
    b9 = b8.fit_transform(b4)
    b10 = LinearRegression()
    b10.fit(b9, b7)
    b11 = b10.predict(b9)
    b12 = mean_squared_error(b7, b11)
    b13 = r2_score(b7, b11)
    print('The RMSE of the linear regression b10 is {}'.format(b12))
    print('The R2 score of the linear regression b10 is {}'.format(b13))
    b14 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
    b15 = b14[:, np.newaxis]
    b15 = b8.fit_transform(b15)
    b16 = b10.predict(b15)
    b16 = np.round(b16,4)
    b17 = np.concatenate((b5, b14))
    b18 = np.concatenate((b11, b16))
    b19 = np.concatenate((b7, b16))
    b20 = b14
    b21 = b16
    b22 = pd.read_csv(b2, usecols = ['Entity'])
    b22 = np.array(b22)
    b22 = b22.ravel()
    b23 = b22[0:6]
    b22 = np.concatenate((b22, b23))
    b24 = pd.read_csv(b2, usecols=['Code'])
    b24 = np.array(b24)
    b24 = b24.ravel()
    b25 = b24[0:6]
    b24 = np.concatenate((b24, b25))
    b26 = {
            'Entity' : b22,
            'Code' : b24,
            'Year': b17,
            'crop(tonnes per hectare)': b19.ravel()
            }
    b27 = DataFrame(b26, columns= ['Entity','Code','Year', 'crop(tonnes per hectare)'])
    b28 = b27.to_csv(r'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly/'+b1[a1]+r'_tomato.csv', b32 = None, header=True)
else:
    os.chdir("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly")
    b29 = 'csv'
    b30 = [a1 for a1 in glob.glob('*.{}'.format(b29))]
    b31 = pd.concat([pd.read_csv(f) for f in b30 ])
    b31.to_csv( "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly_tomato.csv", b32 = False, encoding='utf-8-sig')
    print('all done')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
b1 = ['Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya']
a1 = 0
for a1 in range (19):
    b2 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'+b1[a1]+".csv"
    b3 = pd.read_csv(b2, usecols = ['Year'])
    b4 = np.array(b3)
    b5 = b4.ravel()
    b6 = pd.read_csv(b2, usecols = ['Crop'])
    b7 = np.array(b6)
    b8 = LinearRegression()
    b8.fit(b4, b7)
    b9 = b8.predict(b4)
    b10 = mean_squared_error(b7, b9)
    b11 = r2_score(b7, b9)
    print('The RMSE of the linear regression b8 is {}'.format(b10))
    print('The R2 score of the linear regression b8 is {}'.format(b11))
    b12 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
    b13 = b12[:, np.newaxis]
    b14 = b8.predict(b13)
    b14 = np.round(b14,4)
    b15 = np.concatenate((b5, b12))
    b16 = np.concatenate((b9, b14))
    b17 = np.concatenate((b7, b14))
    b18 = b12
    b19 = b14
    b20 = pd.read_csv(b2, usecols = ['Entity'])
    b20 = np.array(b20)
    b20 = b20.ravel()
    b21 = b20[0:6]
    b20 = np.concatenate((b20, b21))
    b22 = pd.read_csv(b2, usecols=['Code'])
    b22 = np.array(b22)
    b22 = b22.ravel()
    b23 = b22[0:6]
    b22 = np.concatenate((b22, b23))
    b24 = {
            'Entity' : b20,
            'Code' : b22,
            'Year': b15,
            'crop(tonnes per hectare)': b17.ravel()
            }
    b25 = DataFrame(b24, columns= ['Entity','Code','Year', 'crop(tonnes per hectare)'])
    b26 = b25.to_csv(r'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear/'+b1[a1]+r'_tomato.csv', b30 = None, header=True)
else:
    os.chdir("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear")
    b27 = 'csv'
    b28 = [a1 for a1 in glob.glob('*.{}'.format(b27))]
    b29 = pd.concat([pd.read_csv(f) for f in b28 ])
    b29.to_csv( "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_tomato.csv", b30 = False, encoding='utf-8-sig')
    print('all done')
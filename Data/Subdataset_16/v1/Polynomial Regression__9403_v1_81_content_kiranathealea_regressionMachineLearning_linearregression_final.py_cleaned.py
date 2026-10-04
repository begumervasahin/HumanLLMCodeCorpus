import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
b1 = ['Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya']
for i in range(21):
    b2 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/' + b1[i] + ".csv"
    b3 = pd.read_csv(b2, usecols=['Year'])
    b4 = np.array(b3)
    b5 = b4.ravel()
    b6 = pd.read_csv(b2, usecols=['Crop'])
    b7 = np.array(b6)
    b8 = LinearRegression()
    b8.fit(b4, b7)
    b9 = b8.predict(b4)
    b10 = mean_squared_error(b7, b9)
    b11 = r2_score(b7, b9)
    print(f'The RMSE of the linear regression b8 for {b1[i]} is {b10}')
    print(f'The R2 score of the linear regression b8 for {b1[i]} is {b11}')
    b12 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
    b13 = b12[:, np.newaxis]
    b14 = b8.predict(b13)
    b14 = np.round(b14, 4)
    b15 = np.concatenate((b5, b12))
    b16 = np.concatenate((b9, b14))
    b17 = np.concatenate((b7, b14))
    b18 = pd.read_csv(b2, usecols=['Entity'])
    b18 = np.array(b18)
    b18 = b18.ravel()
    b19 = b18[:6]
    b18 = np.concatenate((b18, b19))
    b20 = pd.read_csv(b2, usecols=['Code'])
    b20 = np.array(b20)
    b20 = b20.ravel()
    b21 = b20[:6]
    b20 = np.concatenate((b20, b21))
    b22 = {
        'Entity': b18,
        'Code': b20,
        'Year': b15,
        'crop(tonnes per hectare)': b17.ravel()
    }
    b23 = pd.DataFrame(b22, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
    b24 = b23.to_csv(f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear/{b1[i]}_tomato.csv', b28=None, header=True)
os.chdir("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear")
b25 = 'csv'
b26 = [i for i in glob.glob('*.{}'.format(b25))]
b27 = pd.concat([pd.read_csv(f) for f in b26])
b27.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_tomato.csv", b28 = False, encoding='utf-8-sig')
print('all done')
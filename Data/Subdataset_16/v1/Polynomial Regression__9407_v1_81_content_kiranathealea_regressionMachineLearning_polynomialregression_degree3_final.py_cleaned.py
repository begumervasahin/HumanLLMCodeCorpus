import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
b1 = ['Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya']
b2 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'
b3 = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly2/'
for i in range(19):
    b4 = os.path.join(b2, b1[i] + ".csv")
    b5 = pd.read_csv(b4, usecols=['Year'])
    b6 = np.array(b5)
    b7 = b6.ravel()
    b8 = pd.read_csv(b4, usecols=['Crop'])
    b9 = np.array(b8)
    b10 = PolynomialFeatures(degree=3)
    b11 = b10.fit_transform(b6)
    b12 = LinearRegression()
    b12.fit(b11, b9)
    b13 = b12.predict(b11)
    b14 = mean_squared_error(b9, b13)
    b15 = r2_score(b9, b13)
    print(f'The RMSE of the linear regression b12 for {b1[i]} is {b14}')
    print(f'The R2 score of the linear regression b12 for {b1[i]} is {b15}')
    b16 = np.array([2015, 2016, 2017, 2018, 2019, 2020])
    b17 = b16[:, np.newaxis]
    b17 = b10.fit_transform(b17)
    b18 = b12.predict(b17)
    b18 = np.round(b18, 4)
    b19 = np.concatenate((b7, b16))
    b20 = np.concatenate((b13, b18))
    b21 = np.concatenate((b9, b18))
    b22 = pd.read_csv(b4, usecols=['Entity'])
    b22 = np.array(b22).ravel()
    b23 = b22[0:6]
    b22 = np.concatenate((b22, b23))
    b24 = pd.read_csv(b4, usecols=['Code'])
    b24 = np.array(b24).ravel()
    b25 = b24[0:6]
    b24 = np.concatenate((b24, b25))
    b26 = {
        'Entity': b22,
        'Code': b24,
        'Year': b19,
        'crop(tonnes per hectare)': b21.ravel()
    }
    b27 = pd.DataFrame(b26, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
    b27.to_csv(os.path.join(b3, b1[i] + '_tomato.csv'), b28 = False, header=True)
os.chdir(b3)
b29 = 'csv'
b30 = [i for i in glob.glob(f'*.{b29}')]
b31 = pd.concat([pd.read_csv(f) for f in b30])
b31.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly2_tomato.csv", b28 = False, encoding='utf-8-sig')
print('All done')
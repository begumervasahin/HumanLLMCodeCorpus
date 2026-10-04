import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from pandas import DataFrame
daftar_kota = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur',
    'Cirebon', 'DIY', 'Garut', 'Gunung Kidul', 'Indramayu',
    'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka',
    'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang',
    'Tasikmalaya'
]
input_folder = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'
output_folder = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly/'
combined_csv_path = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly_tomato.csv'
for kota in daftar_kota:
    folder = os.path.join(input_folder, kota + ".csv")
    data_year_x = pd.read_csv(folder, usecols=['Year'])
    x = np.array(data_year_x)
    x_list = x.ravel()
    data_crop_y = pd.read_csv(folder, usecols=['Crop'])
    y = np.array(data_crop_y)
    polynomial_features = PolynomialFeatures(degree=2)
    x_poly = polynomial_features.fit_transform(x)
    model = LinearRegression()
    model.fit(x_poly, y)
    y_poly_pred = model.predict(x_poly)
    rmse_ = mean_squared_error(y, y_poly_pred)
    r2_ = r2_score(y, y_poly_pred)
    print(f'The RMSE of the linear regression model for {kota} is {rmse_}')
    print(f'The R2 score of the linear regression model for {kota} is {r2_}')
    years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
    year = years[:, np.newaxis]
    year = polynomial_features.fit_transform(year)
    y_next = model.predict(year)
    y_next = np.round(y_next, 4)
    x_final = np.concatenate((x_list, years))
    y_final = np.concatenate((y_poly_pred, y_next))
    y_final_print = np.concatenate((y, y_next))
    wilayah = pd.read_csv(folder, usecols=['Entity'])
    wilayah = np.array(wilayah).ravel()
    wil_tambahan = wilayah[0:6]
    wilayah = np.concatenate((wilayah, wil_tambahan))
    kode = pd.read_csv(folder, usecols=['Code'])
    kode = np.array(kode).ravel()
    kode_tambahan = kode[0:6]
    kode = np.concatenate((kode, kode_tambahan))
    recsv = {
        'Entity': wilayah,
        'Code': kode,
        'Year': x_final,
        'crop(tonnes per hectare)': y_final_print.ravel()
    }
    df = DataFrame(recsv, columns=['Entity', 'Code', 'Year', 'crop(tonnes per hectare)'])
    output_path = os.path.join(output_folder, kota + '_tomato.csv')
    df.to_csv(output_path, index=None, header=True)
os.chdir(output_folder)
extension = 'csv'
all_filenames = [i for i in glob.glob(f'*.{extension}')]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv(combined_csv_path, index=False, encoding='utf-8-sig')
print('All done')
import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
daftar_kota = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY', 'Garut',
    'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan', 'Majalengka',
    'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya'
]
for city in daftar_kota:
    folder = f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/{city}.csv'
    data_year_x = pd.read_csv(folder, usecols=['Year'])
    data_crop_y = pd.read_csv(folder, usecols=['Crop'])
    x = np.array(data_year_x).reshape(-1, 1)
    y = np.array(data_crop_y).reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    rmse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    print(f'The RMSE of the linear regression model for {city} is {rmse}')
    print(f'The R2 score of the linear regression model for {city} is {r2}')
    future_years = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    future_predictions = np.round(model.predict(future_years), 4)
    x_combined = np.concatenate((x, future_years))
    y_combined = np.concatenate((y_pred, future_predictions))
    y_combined_print = np.concatenate((y, future_predictions))
    wilayah = pd.read_csv(folder, usecols=['Entity']).values.ravel()
    kode = pd.read_csv(folder, usecols=['Code']).values.ravel()
    wilayah_extended = np.concatenate((wilayah, wilayah[:6]))
    kode_extended = np.concatenate((kode, kode[:6]))
    result_df = pd.DataFrame({
        'Entity': wilayah_extended,
        'Code': kode_extended,
        'Year': x_combined.ravel(),
        'crop(tonnes per hectare)': y_combined_print.ravel()
    })
    result_df.to_csv(f'/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear/{city}_tomato.csv', index=False)
output_dir = "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear"
os.chdir(output_dir)
all_filenames = glob.glob('*.csv')
combined_df = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_df.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_tomato.csv", index=False, encoding='utf-8-sig')
print('All done')
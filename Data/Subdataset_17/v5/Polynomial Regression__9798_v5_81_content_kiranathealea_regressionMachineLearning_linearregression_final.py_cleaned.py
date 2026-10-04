import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
daftar_kota = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon', 'DIY',
    'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo', 'Kuningan',
    'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya'
]
input_dir = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'
output_dir = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/linear/'
for kota in daftar_kota:
    file_path = os.path.join(input_dir, f'{kota}.csv')
    data_year_x = pd.read_csv(file_path, usecols=['Year'])
    x = data_year_x['Year'].values.reshape(-1, 1)
    data_crop_y = pd.read_csv(file_path, usecols=['Crop'])
    y = data_crop_y['Crop'].values.reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    rmse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    print(f'The RMSE of the linear regression model for {kota} is {rmse}')
    print(f'The R2 score of the linear regression model for {kota} is {r2}')
    future_years = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    y_future_pred = model.predict(future_years)
    x_final = np.concatenate((x.ravel(), future_years.ravel()))
    y_final = np.concatenate((y_pred.ravel(), y_future_pred.ravel()))
    wilayah = pd.read_csv(file_path, usecols=['Entity']).iloc[0, 0]
    kode = pd.read_csv(file_path, usecols=['Code']).iloc[0, 0]
    wilayah = [wilayah] * len(x_final)
    kode = [kode] * len(x_final)
    result_df = pd.DataFrame({
        'Entity': wilayah,
        'Code': kode,
        'Year': x_final,
        'crop(tonnes per hectare)': y_final
    })
    output_file = os.path.join(output_dir, f'{kota}_tomato.csv')
    result_df.to_csv(output_file, index=False)
os.chdir(output_dir)
all_filenames = glob.glob('*.csv')
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_tomato.csv", index=False, encoding='utf-8-sig')
print('All done')
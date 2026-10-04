import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
daftar_kota = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon',
    'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo',
    'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi',
    'Sumedang', 'Tasikmalaya'
]
base_folder = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'
output_folder = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly/'
final_output_path = "/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly_tomato.csv"
for kota in daftar_kota[:-2]:
    file_path = os.path.join(base_folder, f"{kota}.csv")
    data = pd.read_csv(file_path)
    x = data['Year'].values.reshape(-1, 1)
    y = data['Crop'].values
    poly = PolynomialFeatures(degree=2)
    x_poly = poly.fit_transform(x)
    model = LinearRegression()
    model.fit(x_poly, y)
    y_pred = model.predict(x_poly)
    rmse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    print(f'The RMSE of the polynomial regression model for {kota} is {rmse}')
    print(f'The R2 score of the polynomial regression model for {kota} is {r2}')
    future_years = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    future_years_poly = poly.transform(future_years)
    future_predictions = model.predict(future_years_poly)
    combined_years = np.concatenate((x.ravel(), future_years.ravel()))
    combined_predictions = np.concatenate((y_pred, future_predictions))
    combined_actual = np.concatenate((y, future_predictions))
    entities = np.concatenate((data['Entity'].values, data['Entity'].values[:6]))
    codes = np.concatenate((data['Code'].values, data['Code'].values[:6]))
    result_df = pd.DataFrame({
        'Entity': entities,
        'Code': codes,
        'Year': combined_years,
        'crop(tonnes per hectare)': combined_actual
    })
    result_df.to_csv(os.path.join(output_folder, f"{kota}_tomato.csv"), index=False)
os.chdir(output_folder)
all_filenames = glob.glob('*.csv')
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv(final_output_path, index=False, encoding='utf-8-sig')
print('All done')
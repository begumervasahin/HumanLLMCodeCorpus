import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
cities = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon',
    'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo',
    'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi',
    'Sumedang', 'Tasikmalaya'
]
input_folder = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'
output_folder = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly2/'
def process_city(city):
    file_path = os.path.join(input_folder, city + ".csv")
    data = pd.read_csv(file_path)
    x = data['Year'].values.reshape(-1, 1)
    y = data['Crop'].values.reshape(-1, 1)
    poly_features = PolynomialFeatures(degree=3)
    x_poly = poly_features.fit_transform(x)
    model = LinearRegression()
    model.fit(x_poly, y)
    y_poly_pred = model.predict(x_poly)
    rmse = mean_squared_error(y, y_poly_pred)
    r2 = r2_score(y, y_poly_pred)
    print(f'The RMSE of the linear regression model for {city} is {rmse}')
    print(f'The R2 score of the linear regression model for {city} is {r2}')
    future_years = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    future_years_poly = poly_features.transform(future_years)
    y_future_pred = model.predict(future_years_poly)
    all_years = np.concatenate((x.ravel(), future_years.ravel()))
    all_crops = np.concatenate((y_poly_pred.ravel(), y_future_pred.ravel()))
    all_crops_original = np.concatenate((y.ravel(), y_future_pred.ravel()))
    entities = np.concatenate((data['Entity'].values, data['Entity'].values[:6]))
    codes = np.concatenate((data['Code'].values, data['Code'].values[:6]))
    results = pd.DataFrame({
        'Entity': entities,
        'Code': codes,
        'Year': all_years,
        'crop(tonnes per hectare)': all_crops_original
    })
    results.to_csv(os.path.join(output_folder, f'{city}_tomato.csv'), index=False)
for city in cities[:19]:
    process_city(city)
os.chdir(output_folder)
extension = 'csv'
all_filenames = glob.glob(f'*.{extension}')
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly2_tomato.csv", index=False, encoding='utf-8-sig')
print('All done')
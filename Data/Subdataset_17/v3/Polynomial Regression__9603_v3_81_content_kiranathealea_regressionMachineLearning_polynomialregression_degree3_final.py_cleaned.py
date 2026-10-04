import numpy as np
import pandas as pd
import os
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
CITIES = [
    'Bandung', 'Bantul', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur', 'Cirebon',
    'DIY', 'Garut', 'Gunung Kidul', 'Indramayu', 'Karawang', 'Kulon Progo',
    'Kuningan', 'Majalengka', 'Purwakarta', 'Sleman', 'Subang', 'Sukabumi',
    'Sumedang', 'Tasikmalaya'
]
INPUT_FOLDER = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/tomato_csv_perdaerah/'
OUTPUT_FOLDER = '/home/leathea/Downloads/Machine-Learning/PolynomialRegression/hasiltomato/poly2/'
def load_data(file_path):
    data = pd.read_csv(file_path)
    x = data['Year'].values.reshape(-1, 1)
    y = data['Crop'].values.reshape(-1, 1)
    entities = data['Entity'].values
    codes = data['Code'].values
    return x, y, entities, codes
def perform_polynomial_regression(x, y, degree=3):
    poly_features = PolynomialFeatures(degree=degree)
    x_poly = poly_features.fit_transform(x)
    model = LinearRegression()
    model.fit(x_poly, y)
    return model, poly_features, x_poly
def predict_future_values(model, poly_features, future_years):
    future_years_poly = poly_features.transform(future_years)
    return model.predict(future_years_poly)
def save_results(city, entities, codes, all_years, all_crops, output_folder):
    results = pd.DataFrame({
        'Entity': entities,
        'Code': codes,
        'Year': all_years,
        'crop(tonnes per hectare)': all_crops
    })
    results.to_csv(os.path.join(output_folder, f'{city}_tomato.csv'), index=False)
def process_city(city):
    file_path = os.path.join(INPUT_FOLDER, city + ".csv")
    x, y, entities, codes = load_data(file_path)
    model, poly_features, x_poly = perform_polynomial_regression(x, y)
    y_poly_pred = model.predict(x_poly)
    rmse = mean_squared_error(y, y_poly_pred)
    r2 = r2_score(y, y_poly_pred)
    print(f'The RMSE of the linear regression model for {city} is {rmse}')
    print(f'The R2 score of the linear regression model for {city} is {r2}')
    future_years = np.array([2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
    y_future_pred = predict_future_values(model, poly_features, future_years)
    all_years = np.concatenate((x.ravel(), future_years.ravel()))
    all_crops = np.concatenate((y.ravel(), y_future_pred.ravel()))
    entities_extended = np.concatenate((entities, entities[:len(future_years)]))
    codes_extended = np.concatenate((codes, codes[:len(future_years)]))
    save_results(city, entities_extended, codes_extended, all_years, all_crops, OUTPUT_FOLDER)
def combine_csv_files(output_folder):
    os.chdir(output_folder)
    extension = 'csv'
    all_filenames = glob.glob(f'*.{extension}')
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_csv.to_csv("/home/leathea/Downloads/Machine-Learning/PolynomialRegression/predicted_poly2_tomato.csv", index=False, encoding='utf-8-sig')
def main():
    for city in CITIES[:19]:
        process_city(city)
    combine_csv_files(OUTPUT_FOLDER)
    print('All done')
if __name__ == "__main__":
    main()
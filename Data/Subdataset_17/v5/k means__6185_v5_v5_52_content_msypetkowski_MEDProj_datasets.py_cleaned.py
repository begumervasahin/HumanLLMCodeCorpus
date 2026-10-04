
import pandas as pd
def load_iris():
    iris_url = 'https:
    iris_data = pd.read_csv(iris_url)
    return iris_data
def load_adult():
    adult_url = 'https:
    adult_columns = [
        "Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Marital Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"
    ]
    adult_data = pd.read_csv(
        adult_url,
        names=adult_columns,
        sep=r'\s*,\s*',
        engine='python',
        na_values="?"
    )
    return adult_data
def load_ctg():
    ctg_url = 'http:
    ctg_data = pd.read_csv(ctg_url)
    ctg_data_cleaned = ctg_data.drop('Unnamed: 0', axis=1)
    return ctg_data_cleaned
def load_cars():
    cars_url = 'https:
    cars_columns = ["class", "buying", "maint", "doors", "persons", "lug_boot", "safety"]
    cars_data = pd.read_csv(cars_url, names=cars_columns)
    return cars_data
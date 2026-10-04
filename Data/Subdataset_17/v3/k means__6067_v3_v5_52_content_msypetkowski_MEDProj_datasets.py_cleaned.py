
import pandas as pd
def load_dataset(url, column_names=None, sep=',', na_values=None, drop_column=None):
    df = pd.read_csv(url, names=column_names, sep=sep, na_values=na_values, engine='python')
    if drop_column:
        df = df.drop(drop_column, axis=1)
    return df
def load_iris():
    url = 'https:
    return load_dataset(url)
def load_adult():
    url = 'https:
    column_names = ["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Marital Status",
                    "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
                    "Hours per week", "Country", "Target"]
    return load_dataset(url, column_names, sep=r'\s*,\s*', na_values="?")
def load_ctg():
    url = 'http:
    return load_dataset(url, drop_column='Unnamed: 0')
def load_cars():
    url = 'https:
    column_names = ["class", "buying", "maint", "doors", "persons", "lug_boot", "safety"]
    return load_dataset(url, column_names)
if __name__ == "__main__":
    datasets = {
        "Iris Dataset": load_iris(),
        "Adult Dataset": load_adult(),
        "Cardiotocography Dataset": load_ctg(),
        "Car Evaluation Dataset": load_cars()
    }
    for name, df in datasets.items():
        print(f"\n{name}:")
        print(df.head())
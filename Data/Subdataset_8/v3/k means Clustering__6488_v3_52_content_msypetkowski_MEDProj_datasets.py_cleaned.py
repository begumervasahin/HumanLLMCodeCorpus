import pandas as pd
def load_iris_dataset():
    iris_url = 'https:
    return pd.read_csv(iris_url)
def load_adult_dataset():
    adult_url = 'https:
    column_names = ["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
                    "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
                    "Hours per week", "Country", "Target"]
    return pd.read_csv(adult_url, names=column_names, sep=r'\s*,\s*', engine='python', na_values="?")
def load_ctg_dataset():
    ctg_url = 'http:
    ctg_data = pd.read_csv(ctg_url)
    return ctg_data.drop('Unnamed: 0', axis=1)
def load_cars_dataset():
    cars_url = 'https:
    column_names = ["class", "buying", "maint", "doors", "persons", "lug_boot", "safety"]
    return pd.read_csv(cars_url, names=column_names)
if __name__ == "__main__":
    iris_df = load_iris_dataset()
    print("IRIS dataset loaded successfully.")
    print(iris_df.head())
    adult_df = load_adult_dataset()
    print("\nADULT dataset loaded successfully.")
    print(adult_df.head())
    ctg_df = load_ctg_dataset()
    print("\nCTG dataset loaded successfully.")
    print(ctg_df.head())
    cars_df = load_cars_dataset()
    print("\nCARS dataset loaded successfully.")
    print(cars_df.head())
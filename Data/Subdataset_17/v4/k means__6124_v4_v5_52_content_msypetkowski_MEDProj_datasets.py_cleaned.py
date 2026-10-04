
import pandas as pd
def load_iris():
    url = 'https:
    return pd.read_csv(url)
def load_adult():
    url = 'https:
    column_names = [
        "Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Marital Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"
    ]
    return pd.read_csv(
        url,
        names=column_names,
        sep=r'\s*,\s*',
        engine='python',
        na_values="?"
    )
def load_ctg():
    url = 'http:
    ctg_data = pd.read_csv(url)
    return ctg_data.drop('Unnamed: 0', axis=1)
def load_cars():
    url = 'https:
    column_names = ["class", "buying", "maint", "doors", "persons", "lug_boot", "safety"]
    return pd.read_csv(url, names=column_names)
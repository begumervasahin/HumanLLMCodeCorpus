
import pandas as pd
def load_iris():
    return pd.read_csv('https:
def load_adult():
    column_names = ["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
                    "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
                    "Hours per week", "Country", "Target"]
    return pd.read_csv('https:
                       names=column_names,
                       sep=r'\s*,\s*',
                       engine='python',
                       na_values="?")
def load_ctg():
    ctg_data = pd.read_csv('http:
    return ctg_data.drop('Unnamed: 0', axis=1)
def load_cars():
    column_names = ["class", "buying", "maint", "doors", "persons", "lug_boot", "safety"]
    return pd.read_csv('https:
                       names=column_names)
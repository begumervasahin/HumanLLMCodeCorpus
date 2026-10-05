
import pandas as pd
def load_iris():
    return pd.read_csv('https:
def load_adult():
    return pd.read_csv('https:
                       names=["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
                              "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
                              "Hours per week", "Country", "Target"],
                       sep=r'\s*,\s*',
                       engine='python',
                       na_values="?")
def load_ctg():
    ret = pd.read_csv('http:
    ret = ret.drop('Unnamed: 0', 1)
    return ret
def load_cars():
    return pd.read_csv('https:
                       names=["class", "buying", "maint", "doors", "persons", "lug_boot", "safety"])


import pandas as pd
def fonk1(b3, b1 = None, b4=',', na_values=None, b5=None):
    b2 = pd.read_csv(b3, names=b1, b4=b4, na_values=na_values, engine='python')
    if b5:
        b2 = b2.drop(b5, axis=1)
    return b2
def fonk2():
    b3 = 'https:
    return fonk1(b3)
def fonk3():
    b3 = 'https:
    b1 = ["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Marital Status",
                    "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
                    "Hours per week", "Country", "Target"]
    return fonk1(b3, b1, b4 = r'\s*,\s*', na_values="?")
def fonk4():
    b3 = 'http:
    return fonk1(b3, b5 = 'Unnamed: 0')
def fonk5():
    b3 = 'https:
    b1 = ["class", "buying", "maint", "doors", "persons", "lug_boot", "safety"]
    return fonk1(b3, b1)
if b6 = = "__main__":
    b7 = {
        "Iris Dataset": fonk2(),
        "Adult Dataset": fonk3(),
        "Cardiotocography Dataset": fonk4(),
        "Car Evaluation Dataset": fonk5()
    }
    for name, b2 in b7.items():
        print(f"\n{name}:")
        print(b2.head())
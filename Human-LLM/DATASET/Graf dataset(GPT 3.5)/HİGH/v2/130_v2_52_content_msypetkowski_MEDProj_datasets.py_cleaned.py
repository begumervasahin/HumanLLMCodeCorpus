import pandas as pd
def fonk1():
    return pd.read_csv('https:
def fonk2():
    return pd.read_csv('https:
                       b1 = ["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
                              "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
                              "Hours per week", "Country", "Target"],
                       b2 = r'\s*,\s*', engine='python', na_values="?")
def fonk3():
    b3 = pd.read_csv('http:
    b3 = b3.drop('Unnamed: 0', axis=1)
    return b3
def fonk4():
    return pd.read_csv('https:
                       b1 = ["class", "buying", "maint", "doors", "persons", "lug_boot", "safety"])
if b4 = = "__main__":
    b5 = fonk1()
    print("IRIS dataset loaded successfully.")
    print(b5.head())
    b6 = fonk2()
    print("\nADULT dataset loaded successfully.")
    print(b6.head())
    b7 = fonk3()
    print("\nCTG dataset loaded successfully.")
    print(b7.head())
    b8 = fonk4()
    print("\nCARS dataset loaded successfully.")
    print(b8.head())
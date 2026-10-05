import pandas as pd
b1 = './tenYears.xlsx'
b2 = pd.read_excel(b1)
b2.to_pickle('./pickle/tenYears.pkl')
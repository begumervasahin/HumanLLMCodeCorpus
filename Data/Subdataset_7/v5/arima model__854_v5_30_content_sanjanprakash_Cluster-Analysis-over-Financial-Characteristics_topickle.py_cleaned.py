
import pandas as pd
b1 = './tenYears.xlsx'
b2 = './pickle/tenYears.pkl'
b3 = pd.read_excel(b1)
b3.to_pickle(b2)
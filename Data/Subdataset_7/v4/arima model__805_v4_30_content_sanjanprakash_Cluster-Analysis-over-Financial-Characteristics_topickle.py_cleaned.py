
import pandas as pd
b1 = './tenYears.xlsx'
b2 = pd.read_excel(b1)
b3 = './pickle/tenYears.pkl'
b2.to_pickle(b3)
w
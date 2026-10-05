import pandas as pd
excel_path = './tenYears.xlsx'
df = pd.read_excel(excel_path)
pickle_path = './pickle/tenYears.pkl'
df.to_pickle(pickle_path)
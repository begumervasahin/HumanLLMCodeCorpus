
import pandas as pd
excel_path = './tenYears.xlsx'
data_frame = pd.read_excel(excel_path)
pickle_path = './pickle/tenYears.pkl'
data_frame.to_pickle(pickle_path)
w
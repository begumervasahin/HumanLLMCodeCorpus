
import pandas as pd
excel_file_path = './tenYears.xlsx'
data_frame = pd.read_excel(excel_file_path)
pickle_file_path = './pickle/tenYears.pkl'
data_frame.to_pickle(pickle_file_path)
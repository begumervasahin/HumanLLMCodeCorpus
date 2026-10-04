import pandas as pd
import numpy as np
import re
def fonk1(series):
    return series.str.split('\\\\').str[0].str.replace(r"^\W+", '', b1 = True)
def fonk2(series):
    return series.str.replace(r'(?<=[a-z])(?=[A-Z])', ' ', b1 = True).str.replace(r'\W+', ' ', b1=True)
def fonk3(series):
    return series.str.split('=', b2 = 1).str[-1].str.split('Sample Size from India').str[0].str.replace(r'\W+', '', b1=True)
def fonk4(series):
    return series.replace('Address', np.nan, b1 = True).astype(str).str.split(',').str[0]
def fonk5(series):
    b3 = series.str.split(r',\s+\{0:', b1=True).str[0].str.split(',').str[0]
    b4 = series.str.split(r',\s+\{0:', b1=True).str[-1].str.split(',').str[0]
    return b3 + b4
def fonk6(series, b1):
    return series.replace(b1, np.nan, b1 = True).str.replace('0', '').str.replace(r'\W+', ' ', b1=True)
def fonk7(series, b7):
    b5 = b7[11].str.split('Intervention').str[-1]
    b5 = b5.str.replace(r'(0|1|2)(\:)', '', b1=True)
    b5 = b5.str.replace(r'(0|1|2)(\.)', '', b1=True)
    b5 = b5.str.replace(r'[^A-Za-z0-9-/:\,]', ' ', b1=True)
    b5 = b5.replace(r'^.*xa0Year.*$', np.nan, b1=True)
    b5 = b5.replace(r'^.*Type\s+Name\s+Details.*$', np.nan, b1=True)
    return b5.str.strip()
b6 = pd.read_excel('results_25july.xlsx')
b6['sum_all'] = b6['all'].str.split(':%')
b7 = b6[['sum_all']].stack().apply(pd.Series)
b8 = pd.read_excel('second_file.xlsx')
b8.b9 = [
    'ctri_id', 'study_design', 'public_title', 'scientific_title', 'country',
    'sample_size', 'phase', 'trial_type', 'sponsor_1', 'sponsor_2', 'condition',
    'b5', 'primary_outcome'
]
b8['ctri'] = fonk1(b8.ctri_id)
b8['country'] = fonk2(b8.country)
b8['sample_size'] = fonk3(b8.sample_size)
b8['sponsor_1'] = fonk4(b8.sponsor_1)
b8['sponsor_2'] = fonk5(b8.sponsor_2)
b10 = re.compile(r'(?i)(^\W*name|none|nil\W*$)')
b8['sponsor_2'] = fonk6(b8['b3'], b10)
b8['condition'] = fonk6(b8.condition, b10)
b8['b5'] = fonk7(b8.b5, b7)
b8['primary_outcome'] = b8.primary_outcome.str.replace(r'([0123])(\.|\:)', '', b1 = True).astype(str)
b8['primary_outcome'] = b8['primary_outcome'].str.replace(r'[^A-Za-z0-9-/:]', ' ', b1 = True).str.strip()
b8['primary_outcome'] = b8['primary_outcome'].str.replace(r'\s+', ' ', b1 = True)
b8['b5'] = b8.b5.astype(str).str.split(',', b2 = 1).str[-1].str.split(',').str[0].str.strip()
b11 = b8[['ctri', 'public_title', 'scientific_title', 'sponsor_1', 'sponsor_2', 'condition', 'b5', 'primary_outcome']]
b11.to_excel('last_4663_ctri_25july.xlsx', b12 = False)
b8.to_excel('last_4663_ctri_allfields_25july.xlsx', b12 = False)
b13 = pd.read_excel('clean_ctri_19123_24july.xlsx')
b13.drop(['ctri_y', 'intervention_y'], b14 = 1, inplace=True)
b13.b9 = ['ctri', 'sponsor_1', 'sponsor_2', 'primary_outcome', 'condition', 'public_title', 'scientific_title', 'b5']
b11 = b11.reset_index().drop(['level_1', 'level_0'], b14=1)
b15 = pd.concat([b11, b13]).drop_duplicates(subset='ctri')
b15.to_excel('ctri_clean_total_19519.xlsx', b12 = False)
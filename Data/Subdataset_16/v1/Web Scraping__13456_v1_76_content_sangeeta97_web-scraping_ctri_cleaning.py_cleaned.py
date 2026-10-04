import pandas as pd
import numpy as np
import re
b1 = pd.read_excel('results_25july.xlsx')
b1['sum_all'] = b1['all'].str.split(':%')
b2 = b1[['sum_all']].stack().apply(pd.Series)
b3 = pd.read_excel('second_file.xlsx')
b3.b4 = [
    'ctri_id', 'study_design', 'public_title', 'scientific_title', 'country',
    'sample_size', 'phase', 'trial_type', 'sponsor_1', 'sponsor_2', 'condition',
    'intervention', 'primary_outcome'
]
b3['ctri'] = b3.ctri_id.str.split('\\\\').map(lambda x: x[0]).str.replace(r"^\W+", '', b5 = True)
b3['country'] = b3.country.str.replace(r'(?<=[a-z])(?=[A-Z])', ' ', b5 = True).str.replace(r'\W+', ' ', b5=True).values
b3['sample_size'] = b3.sample_size.str.split('=', b6 = 1).map(lambda x: x[-1]).str.split('Sample Size from India').map(lambda x: x[0]).str.replace(r'\W+', '', b5=True).values
b3['sponsor_1'] = b3.sponsor_1.replace('Address', np.nan, b5 = True).astype(str).str.split(',').map(lambda x: x[0])
b3['sponsor_20'] = b3.sponsor_2.str.split(r',\s+\{0:', b5 = True).map(lambda x: x[0]).str.split(',').map(lambda x: x[0]).values
b3['sponsor_21'] = b3.sponsor_2.str.split(r',\s+\{0:', b5 = True).map(lambda x: x[-1]).str.split(',').map(lambda x: x[0]).values
b3['sponsor_2'] = b3['sponsor_20'] + b3['sponsor_21']
b7 = re.compile(r'(?i)(^\W*name|none|nil\W*$)')
b8 = re.compile(r'(?i)(^\W*name|none|NIL\W*\w+$)')
b3['sponsor_2'] = b3['sponsor_20'].str.replace('0', '').str.replace(r'\W+', ' ', b5 = True).replace(b7, np.nan, b5=True)
b3['condition'] = b3.condition.replace(b7, np.nan, b5 = True)
b3['intervention'] = b2[11].str.split('Intervention').map(lambda x: x[-1]).str.replace(r'(0|1|2)(\:)', '', b5 = True).str.replace(r'(0|1|2)(\.)', '', b5=True).str.replace(r'[^A-Za-z0-9-/:\,]', ' ', b5=True).replace(r'^.*xa0Year.*$', np.nan, b5=True).replace(r'^.*Type\s+Name\s+Details.*$', np.nan, b5=True).str.strip()
b3['primary_outcome'] = b3.primary_outcome.str.replace(r'([0123])(\.|\:)', '', b5 = True).astype(str).str.replace(r'[^A-Za-z0-9-/:]', ' ', b5=True).str.strip().str.replace(r'\s+', ' ', b5=True).values
b3['intervention'] = b3.intervention.astype(str).str.split(',', b6 = 1).map(lambda x: x[-1]).str.split(',').map(lambda x: x[0]).str.strip().values
b9 = b3[['ctri', 'public_title', 'scientific_title', 'sponsor_1', 'sponsor_2', 'condition', 'intervention', 'primary_outcome']]
b9.to_excel('last_4663_ctri_25july.xlsx', b10 = False)
b3.to_excel('last_4663_ctri_allfields_25july.xlsx', b10 = False)
b11 = pd.read_excel('clean_ctri_19123_24july.xlsx')
b11.drop(['ctri_y', 'intervention_y'], b12 = 1, inplace=True)
b11.b4 = ['ctri', 'sponsor_1', 'sponsor_2', 'primary_outcome', 'condition', 'public_title', 'scientific_title', 'intervention']
b9 = b9.reset_index()
b9.drop(['level_1', 'level_0'], b12 = 1, inplace=True)
b13 = pd.concat([b9, b11]).drop_duplicates(subset='ctri')
b13.to_excel('ctri_clean_total_19519.xlsx', b10 = False)
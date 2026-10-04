import pandas as pd
import numpy as np
import re
df1 = pd.read_excel('results_25july.xlsx')
df1['sum_all'] = df1['all'].str.split(':%')
dfn = df1[['sum_all']].stack().apply(pd.Series)
df2 = pd.read_excel('second_file.xlsx')
df2.columns = [
    'ctri_id', 'study_design', 'public_title', 'scientific_title', 'country',
    'sample_size', 'phase', 'trial_type', 'sponsor_1', 'sponsor_2', 'condition',
    'intervention', 'primary_outcome'
]
df2['ctri'] = df2.ctri_id.str.split('\\\\').str[0].str.replace(r"^\W+", '', regex=True)
df2['country'] = df2.country.str.replace(r'(?<=[a-z])(?=[A-Z])', ' ', regex=True).str.replace(r'\W+', ' ', regex=True)
df2['sample_size'] = df2.sample_size.str.split('=', n=1).str[-1].str.split('Sample Size from India').str[0].str.replace(r'\W+', '', regex=True)
df2['sponsor_1'] = df2.sponsor_1.replace('Address', np.nan, regex=True).astype(str).str.split(',').str[0]
df2['sponsor_20'] = df2.sponsor_2.str.split(r',\s+\{0:', regex=True).str[0].str.split(',').str[0]
df2['sponsor_21'] = df2.sponsor_2.str.split(r',\s+\{0:', regex=True).str[-1].str.split(',').str[0]
df2['sponsor_2'] = df2['sponsor_20'] + df2['sponsor_21']
io = re.compile(r'(?i)(^\W*name|none|nil\W*$)')
df2['sponsor_2'] = df2['sponsor_20'].str.replace('0', '').str.replace(r'\W+', ' ', regex=True).replace(io, np.nan, regex=True)
df2['condition'] = df2.condition.replace(io, np.nan, regex=True)
df2['intervention'] = dfn[11].str.split('Intervention').str[-1].str.replace(r'(0|1|2)(\:)', '', regex=True).str.replace(r'(0|1|2)(\.)', '', regex=True).str.replace(r'[^A-Za-z0-9-/:\,]', ' ', regex=True).replace(r'^.*xa0Year.*$', np.nan, regex=True).replace(r'^.*Type\s+Name\s+Details.*$', np.nan, regex=True).str.strip()
df2['primary_outcome'] = df2.primary_outcome.str.replace(r'([0123])(\.|\:)', '', regex=True).astype(str).str.replace(r'[^A-Za-z0-9-/:]', ' ', regex=True).str.strip().str.replace(r'\s+', ' ', regex=True)
df2['intervention'] = df2.intervention.astype(str).str.split(',', n=1).str[-1].str.split(',').str[0].str.strip()
df3 = df2[['ctri', 'public_title', 'scientific_title', 'sponsor_1', 'sponsor_2', 'condition', 'intervention', 'primary_outcome']]
df3.to_excel('last_4663_ctri_25july.xlsx', index=False)
df2.to_excel('last_4663_ctri_allfields_25july.xlsx', index=False)
df4 = pd.read_excel('clean_ctri_19123_24july.xlsx')
df4.drop(['ctri_y', 'intervention_y'], axis=1, inplace=True)
df4.columns = ['ctri', 'sponsor_1', 'sponsor_2', 'primary_outcome', 'condition', 'public_title', 'scientific_title', 'intervention']
df3 = df3.reset_index().drop(['level_1', 'level_0'], axis=1)
ctri_19519 = pd.concat([df3, df4]).drop_duplicates(subset='ctri')
ctri_19519.to_excel('ctri_clean_total_19519.xlsx', index=False)
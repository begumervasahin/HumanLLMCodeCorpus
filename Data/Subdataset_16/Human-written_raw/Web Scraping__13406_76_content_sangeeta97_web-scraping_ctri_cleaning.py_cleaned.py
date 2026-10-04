import pandas as pd
import numpy as np
import re
b1 = pd.read_excel('results_25july.xlsx')
b1['sum_all']= b1['all'].str.split(':%')
b2 = b1[['sum_all']]
b2 = b2.stack().apply(pd.Series)
b1['all'].values[0]
df2.b3 = ['ctri_id', 'study_design', 'public_title', 'scientific_title', 'country', 'sample_size', 'phase', 'trial_type', 'sponsor_1', 'sponsor_2', 'condition', 'intervention', 'primary_outcome']
df2['ctri']= df2.ctri_id.str.split('\\\\').map(lambda x: x[0]).str.replace("^\W+", '')
df2['country']= df2.country.str.replace('(?<=[a-z])(?=[A-Z])', ' ').str.replace('\W+', ' ').values
df2['sample_size']= df2.sample_size.str.split('\=', b4 = 1).map(lambda x: x[-1]).str.split('Sample Size from India').map(lambda x: x[0]).str.replace('\W+', '').values
df2.sponsor_1.values[1211]
df2['sponsor_1']= df2.sponsor_1.replace('Address', np.nan, b5 = True).astype(str).str.split(',').map(lambda x: x[0])
df2.ctri_id.values[6]
df2['sponsor_20']= df2.sponsor_2.str.split('\,\s+\{0:').map(lambda x: x[0]).str.split(',').map(lambda x: x[0]).values
df2['sponsor_21']= df2.sponsor_2.str.split('\,\s+\{0:').map(lambda x: x[-1]).str.split(',').map(lambda x: x[0]).values
df2['sponsor_2']= df2['sponsor_20']+ df2['sponsor_21']
b6 = re.compile('(?i)(^\W*name|none|nil\W*$)')
b7 = re.compile('(?i)(^\W*name|none|NIL\W*\w+$)')
df2['sponsor_2']= df2['sponsor_20'].str.replace('0', '').str.replace('\W+', ' ').replace(b6, np.nan, b5 = True)
df2['condition']= df2.condition.replace(b6, np.nan, b5 = True)
df2['intervention']= b2[11].str.split('Intervention').map(lambda x: x[-1]).str.replace('(0|1|2)(\:)', '').str.replace('(0|1|2)(\.)', '').str.replace('[^A-Za-z0-9-/:\,]', ' ').replace('^.*xa0Year.*$', np.nan, b5 = True).replace('^.*Type\s+Name\s+Details.*$', np.nan, b5= True).str.strip()
df2['primary_outcome']= df2.primary_outcome.str.replace('([0123])(\.|\:)', '').astype(str).str.replace('[^A-Za-z0-9-/:]', ' ').str.strip().str.replace('\s+', ' ').values
df2['intervention']= df2.intervention.astype(str).str.split(',', b4 = 1).map(lambda x:x[-1]).str.split(',').map(lambda x: x[0]).str.strip().values
df2.b3
b8 = df2[['ctri', 'public_title', 'scientific_title', 'sponsor_1',
       'sponsor_2', 'condition', 'intervention', 'primary_outcome']]
b8.index.size
import pandas_profiling
b8.to_excel('last_4663_ctri_25july.xlsx')
df2.to_excel('last_4663_ctri_allfields_25july.xlsx')
b9 = pd.read_excel('clean_ctri_19123_24july.xlsx')
b9.drop('ctri_y', b10 = 1, inplace= True)
b9.drop('intervention_y', b10 = 1, inplace= True)
b9.b3 = ['ctri', 'sponsor_1', 'sponsor_2', 'primary_outcome', 'condition', 'public_title', 'scientific_title', 'intervention']
b8.b3
b8 = b8.reset_index()
b8.drop(['level_1', 'level_0'], b10 = 1, inplace= True)
b11 = pd.concat([b8, b9]).drop_duplicates(subset= 'ctri')
b11.to_excel('ctri_clean_total_19519.xlsx')
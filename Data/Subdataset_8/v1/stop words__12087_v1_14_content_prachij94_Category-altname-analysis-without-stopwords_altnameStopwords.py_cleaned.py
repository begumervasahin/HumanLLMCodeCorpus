import pandas as pd
df1 = pd.read_excel("C:/Users/IMART/Downloads/Altname_data.xlsx", sheet_name="Export Worksheet")
df2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
df3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
df3["HIGH FREQUENCY WORDS"] = df3["HIGH FREQUENCY WORDS"].str.lower()
df2["GLCAT_MCAT_NAME"] = df2["GLCAT_MCAT_NAME"].str.lower()
df1["GLCAT_ALTMCAT_NAME"] = df1["GLCAT_ALTMCAT_NAME"].str.lower()
highfreqdict = df3.set_index('SUBCAT ID').T.to_dict('list')
mergedkwdict = df2.merge(df1, left_on='SUBCAT_ID', right_on='FK_GLCAT_CAT_ID', how='inner')
mergedkwdict = mergedkwdict[['SUBCAT_ID', 'GLCAT_MCAT_NAME', 'GLCAT_ALTMCAT_NAME']].set_index('SUBCAT_ID').T.to_dict('list')
def process_alt_names(row):
    subcatid = row['FK_GLCAT_CAT_ID']
    alt_name = row['GLCAT_ALTMCAT_NAME']
    mcat_name = row['GLCAT_MCAT_NAME']
    if subcatid in mergedkwdict:
        stopwords = highfreqdict[subcatid][0] if subcatid in highfreqdict else mergedkwdict[subcatid][1]
        alt_name_split = alt_name.split(" ")
        attribute = " ".join(word for word in alt_name_split if word not in stopwords.split(" "))
        return attribute.strip()
    else:
        return alt_name.strip()
df1['Attribute'] = df1.apply(process_alt_names, axis=1)
df1.to_csv("stopwordsremovedaltnames.csv", index=False)
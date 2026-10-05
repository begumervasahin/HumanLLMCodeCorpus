import pandas as pd
df1 = pd.read_excel("C:/Users/IMART/Downloads/Altname_data.xlsx", sheet_name="Export Worksheet")
df2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
df3 = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
df3["HIGH FREQUENCY WORDS"] = df3["HIGH FREQUENCY WORDS"].str.lower()
df2["GLCAT_MCAT_NAME"] = df2["GLCAT_MCAT_NAME"].str.lower()
df1["GLCAT_ALTMCAT_NAME"] = df1["GLCAT_MCAT_NAME"].str.lower()
high_freq_dict = df3.set_index('SUBCAT ID')["HIGH FREQUENCY WORDS"].to_dict()
merged_df1 = pd.DataFrame(columns=['MCAT_Name', 'Subcat_ID', 'MCAT_Name&HighFrequencyWords'])
for _, group in df2.groupby("SUBCAT_ID"):
    subcat_id = group["SUBCAT_ID"].iloc[0]
    if subcat_id in high_freq_dict:
        unique_words = set(' '.join(group["GLCAT_MCAT_NAME"]).split())
        high_freq_words = high_freq_dict[subcat_id]
        merged_row = {
            'MCAT_Name': group["GLCAT_MCAT_NAME"].iloc[0],
            'Subcat_ID': subcat_id,
            'MCAT_Name&HighFrequencyWords': ' '.join(unique_words) + ' ' + high_freq_words
        }
    else:
        merged_row = {
            'MCAT_Name': group["GLCAT_MCAT_NAME"].iloc[0],
            'Subcat_ID': subcat_id,
            'MCAT_Name&HighFrequencyWords': group["GLCAT_MCAT_NAME"].iloc[0]
        }
    merged_df1 = merged_df1.append(merged_row, ignore_index=True)
merged_kw_dict = merged_df1.set_index('Subcat_ID')["MCAT_Name&HighFrequencyWords"].to_dict()
merged_df2_columns = ['MCAT_ID', 'MCAT_Name', 'Alt_Name', 'Subcat_ID', 'Stopword', 'Attribute']
merged_df2 = pd.DataFrame(columns=merged_df2_columns)
for index, row in df1.iterrows():
    subcat_id = row["FK_GLCAT_CAT_ID"]
    if subcat_id in merged_kw_dict:
        stopwords = merged_kw_dict[subcat_id]
        mcat_name = row["GLCAT_ALTMCAT_NAME"]
        attribute = ' '.join([word for word in mcat_name.split() if word not in stopwords.split()])
        merged_row = {
            'MCAT_ID': row["GLCAT_MCAT_ID"],
            'MCAT_Name': row["GLCAT_MCAT_NAME"],
            'Alt_Name': row["GLCAT_ALTMCAT_NAME"],
            'Subcat_ID': subcat_id,
            'Stopword': stopwords,
            'Attribute': attribute.strip()
        }
    else:
        merged_row = {
            'MCAT_ID': row["GLCAT_MCAT_ID"],
            'MCAT_Name': row["GLCAT_MCAT_NAME"],
            'Alt_Name': row["GLCAT_ALTMCAT_NAME"],
            'Subcat_ID': subcat_id,
            'Attribute': ''
        }
    merged_df2 = merged_df2.append(merged_row, ignore_index=True)
merged_df2.to_csv("stopwordsremovedaltnames.csv", index=False)
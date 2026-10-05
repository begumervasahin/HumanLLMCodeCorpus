import pandas as pd
df_altname = pd.read_excel("C:/Users/IMART/Downloads/Altname_data.xlsx", sheet_name="Export Worksheet")
df_subcat = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
df_wordfreq = pd.read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", sheet_name="wordfrequencyfinal")
df_wordfreq["HIGH FREQUENCY WORDS"] = df_wordfreq["HIGH FREQUENCY WORDS"].str.lower()
df_subcat["GLCAT_MCAT_NAME"] = df_subcat["GLCAT_MCAT_NAME"].str.lower()
df_altname["GLCAT_ALTMCAT_NAME"] = df_altname["GLCAT_MCAT_NAME"].str.lower()
high_freq_dict = df_wordfreq.set_index('SUBCAT ID')["HIGH FREQUENCY WORDS"].to_dict()
merged_df = pd.DataFrame(columns=['MCAT_ID', 'MCAT_Name', 'Alt_Name', 'Subcat_ID', 'Stopword', 'Attribute'])
for _, group in df_subcat.groupby("SUBCAT_ID"):
    subcat_id = group["SUBCAT_ID"].iloc[0]
    if subcat_id in high_freq_dict:
        unique_words = set(' '.join(group["GLCAT_MCAT_NAME"]).split())
        high_freq_words = high_freq_dict[subcat_id]
        merged_df = merged_df.append({
            'MCAT_Name': group["GLCAT_MCAT_NAME"].iloc[0],
            'Subcat_ID': subcat_id,
            'Stopword': high_freq_words,
            'Attribute': ' '.join(unique_words) + ' ' + high_freq_words
        }, ignore_index=True)
    else:
        merged_df = merged_df.append({
            'MCAT_Name': group["GLCAT_MCAT_NAME"].iloc[0],
            'Subcat_ID': subcat_id,
            'Stopword': '',
            'Attribute': group["GLCAT_MCAT_NAME"].iloc[0]
        }, ignore_index=True)
for index, row in df_altname.iterrows():
    subcat_id = row["FK_GLCAT_CAT_ID"]
    if subcat_id in merged_df["Subcat_ID"].values:
        stopwords = merged_df.loc[merged_df["Subcat_ID"] == subcat_id, "Stopword"].iloc[0]
        mcat_name = row["GLCAT_ALTMCAT_NAME"]
        attribute = ' '.join([word for word in mcat_name.split() if word not in stopwords.split()])
    else:
        stopwords = ''
        attribute = ''
    merged_df = merged_df.append({
        'MCAT_ID': row["GLCAT_MCAT_ID"],
        'MCAT_Name': row["GLCAT_MCAT_NAME"],
        'Alt_Name': row["GLCAT_ALTMCAT_NAME"],
        'Subcat_ID': subcat_id,
        'Stopword': stopwords,
        'Attribute': attribute.strip()
    }, ignore_index=True)
merged_df.to_csv("stopwordsremovedaltnames.csv", index=False)
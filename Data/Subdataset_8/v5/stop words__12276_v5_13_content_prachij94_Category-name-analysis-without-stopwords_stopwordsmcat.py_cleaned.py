import pandas as pd
def read_excel(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name=sheet_name)
def convert_to_lowercase(data_frame, column_name):
    if column_name in data_frame.columns:
        data_frame[column_name] = data_frame[column_name].str.lower()
df1 = read_excel("C:/Users/IMART/Downloads/Working MCAT_subcat.xlsx", "Sheet2")
df2 = read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", "Export Worksheet")
df3 = read_excel("C:/Users/IMART/Downloads/wordfrequencyfinal.xlsx", "wordfrequencyfinal")
convert_to_lowercase(df1, "GLCAT_MCAT_NAME")
convert_to_lowercase(df2, "GLCAT_MCAT_NAME")
convert_to_lowercase(df3, "HIGH FREQUENCY WORDS")
mergedf1_columns = ['MCAT_Name', 'Subcat_ID', 'MCAT_Name&HighFrequencyWords']
mergedf2_columns = ['MCAT_ID', 'PMCAT', 'MCAT_Name', 'Subcat_ID', 'Stopword', 'Attribute']
mergedf1 = pd.DataFrame(columns=mergedf1_columns)
mergedf2 = pd.DataFrame(columns=mergedf2_columns)
highfreqdict = df3.set_index('SUBCAT ID')['HIGH FREQUENCY WORDS'].to_dict()
row = 0
for i in range(len(df2)):
    subcat_id = df2.at[i, "SUBCAT_ID"]
    if subcat_id in highfreqdict:
        j = i
        concat_string = " ".join(set(df2.at[i, "GLCAT_MCAT_NAME"] for i in range(i, len(df2)) if df2.at[i, "SUBCAT_ID"] == subcat_id))
        merged_string = " ".join(set(concat_string.split(' ')))
        mergedf1.loc[row] = [df2.at[j, "GLCAT_MCAT_NAME"], subcat_id, f"{merged_string} {highfreqdict[subcat_id]}"]
    else:
        mergedf1.loc[row] = [df2.at[i, "GLCAT_MCAT_NAME"], subcat_id, df2.at[i, "GLCAT_MCAT_NAME"]]
    row += 1
mergedkwdict = mergedf1.set_index('Subcat_ID')['MCAT_Name&HighFrequencyWords'].to_dict()
row = 0
for i in range(len(df1)):
    subcat_id = df1.at[i, "FK_GLCAT_CAT_ID"]
    if subcat_id in mergedkwdict:
        stopwords = mergedkwdict[subcat_id].split()[1]
    else:
        stopwords = ""
    attribute = " ".join(word for word in df1.at[i, "GLCAT_MCAT_NAME"].split() if word not in stopwords.split())
    mergedf2.loc[row] = [df1.at[i, "GLCAT_MCAT_ID"], df1.at[i, "PMCAT"], df1.at[i, "GLCAT_MCAT_NAME"], subcat_id, stopwords, attribute]
    row += 1
mergedf2['Attribute'] = mergedf2['Attribute'].str.strip()
mergedf2.to_csv("stopwordsremovedmcats.csv", index=False)
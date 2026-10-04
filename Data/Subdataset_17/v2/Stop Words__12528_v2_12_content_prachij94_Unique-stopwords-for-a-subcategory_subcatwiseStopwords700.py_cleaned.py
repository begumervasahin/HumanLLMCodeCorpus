import pandas as pd
df2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
df3 = pd.read_csv("C:/Users/IMART/Desktop/My_Data/Himanshu Stopwords/wordfrequencyfinal.csv")
merged_df = pd.DataFrame(columns=['Subcat_ID', 'Stopwords'])
unique_subcats = df2['SUBCAT_ID'].unique()
df3["HIGH FREQUENCY WORDS"] = df3["HIGH FREQUENCY WORDS"].str.lower()
df2["GLCAT_MCAT_NAME"] = df2["GLCAT_MCAT_NAME"].str.lower()
high_freq_dict = df3.set_index('SUBCAT ID').T.to_dict('list')
df3_index = 0
df2_index = 0
row_index = 0
while df3_index < len(df3):
    subcat_id = df3.iloc[df3_index]["SUBCAT ID"]
    if subcat_id in unique_subcats:
        concat_string = ""
        while df2_index < len(df2) and df2.iloc[df2_index]["SUBCAT_ID"] == subcat_id:
            concat_string += df2.iloc[df2_index]["GLCAT_MCAT_NAME"] + " "
            df2_index += 1
        unique_words = set(concat_string.split())
        stopwords_string = " ".join(unique_words)
        stopwords_string += " " + high_freq_dict[subcat_id][0]
        merged_df.loc[row_index, 'Subcat_ID'] = subcat_id
        merged_df.loc[row_index, 'Stopwords'] = stopwords_string
    else:
        merged_df.loc[row_index, 'Subcat_ID'] = subcat_id
        merged_df.loc[row_index, 'Stopwords'] = df3.iloc[df3_index]["HIGH FREQUENCY WORDS"]
    row_index += 1
    df3_index += 1
merged_df.to_csv("700subcatwisefinalstopwords.csv", index=False)
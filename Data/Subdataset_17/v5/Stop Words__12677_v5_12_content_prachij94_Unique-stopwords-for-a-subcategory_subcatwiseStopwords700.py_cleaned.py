
import pandas as pd
df2 = pd.read_excel("C:/Users/IMART/Downloads/Subcat_super_PMCAT.xlsx", sheet_name="Export Worksheet")
df3 = pd.read_csv("C:/Users/IMART/Desktop/My_Data/Himanshu Stopwords/wordfrequencyfinal.csv")
merged_df = pd.DataFrame(columns=['Subcat_ID', 'Stopwords'])
unique_subcats = df2['SUBCAT_ID'].unique()
df3["HIGH FREQUENCY WORDS"] = df3["HIGH FREQUENCY WORDS"].str.lower()
df2["GLCAT_MCAT_NAME"] = df2["GLCAT_MCAT_NAME"].str.lower()
high_freq_dict = df3.set_index('SUBCAT ID')['HIGH FREQUENCY WORDS'].to_dict()
a, i, row = 0, 0, 0
while a < len(df3):
    subcat_id = df3.iloc[a]["SUBCAT ID"]
    if subcat_id in unique_subcats:
        concat_string = ""
        while i < len(df2) and df2.iloc[i]["SUBCAT_ID"] == subcat_id:
            concat_string += df2.iloc[i]["GLCAT_MCAT_NAME"] + " "
            i += 1
        unique_words = set(concat_string.split())
        stopwords = " ".join(unique_words) + " " + high_freq_dict[subcat_id]
        merged_df.loc[row] = [subcat_id, stopwords]
        row += 1
    else:
        merged_df.loc[row] = [subcat_id, df3.iloc[a]["HIGH FREQUENCY WORDS"]]
        row += 1
    a += 1
merged_df.to_csv("700subcatwisefinalstopwords.csv", index=False)